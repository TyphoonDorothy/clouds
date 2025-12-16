import logging
import json
import os
from datetime import datetime
import azure.functions as func
import pyodbc

app = func.FunctionApp()

# ---------- helpers ----------
def parse_timestamp(ts):
    """
    Parse various timestamp formats robustly and return a datetime.
    Accepts:
      - datetime.datetime (returns as-is)
      - ISO-8601 strings with or without timezone, with 'Z', with '+hh:mm', or with '+hh:mmZ'
    Raises ValueError on failure.
    """
    if ts is None:
        raise ValueError("timestamp is None")
    if isinstance(ts, datetime):
        return ts
    if not isinstance(ts, str):
        raise ValueError("timestamp has unsupported type")
    s = ts.strip()
    # If ends with 'Z' (UTC designator), remove the 'Z' so fromisoformat can accept offsets properly.
    if s.endswith("Z"):
        s = s[:-1]
    try:
        return datetime.fromisoformat(s)
    except Exception:
        pass
    # Fallback attempts for common patterns (no timezone)
    fmts = [
        "%Y-%m-%dT%H:%M:%S.%f",  # 2025-12-10T13:36:33.918674
        "%Y-%m-%dT%H:%M:%S"      # 2025-12-10T13:36:33
    ]
    for fmt in fmts:
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            continue
    # last resort: raise clear error
    raise ValueError(f"timestamp not in a supported ISO-8601 format: {ts}")

def get_db_connection():
    conn_str = os.environ.get("SqlConnectionString")
    if not conn_str:
        raise RuntimeError("SqlConnectionString not set")
    
    # pyodbc handles the standard Azure connection string format natively
    # but we often need to specify the driver explicitly for Linux environments
    driver = '{ODBC Driver 18 for SQL Server}'
    
    # If the connection string doesn't have the driver, append it
    if 'Driver=' not in conn_str:
        conn_str += f';Driver={driver}'

    return pyodbc.connect(conn_str)

def insert_sensor_reading(reading: dict):
    """
    Insert into sensor_data (Id is identity).
    Expected keys (normalized): device_id, sensor_type, value, unit, latitude, longitude, timestamp
    """
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        sql = """
        INSERT INTO sensor_data
          (DeviceId, SensorType, Value, Unit, Latitude, Longitude, Timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        # Prepare values
        device_id = reading.get("device_id")
        sensor_type = reading.get("sensor_type")
        value = reading.get("value")
        unit = reading.get("unit")
        latitude = reading.get("latitude")
        longitude = reading.get("longitude")
        ts = reading.get("timestamp")
        
        # Validate required
        if not all([device_id, sensor_type, value, ts]):
            raise ValueError("Missing required reading fields (device_id, sensor_type, value, timestamp)")
        
        # Normalize types
        try:
            value = float(value)
        except Exception:
            raise ValueError(f"value is not numeric: {value}")
        
        # Parse timestamp robustly
        if isinstance(ts, str) or isinstance(ts, datetime):
            ts = parse_timestamp(ts)
        else:
            raise ValueError("timestamp has unsupported type")
        
        # Allow None lat/lon (DB accepts NULL)
        cur.execute(sql, (device_id, sensor_type, value, unit, latitude, longitude, ts))
        conn.commit()
    except Exception:
        if conn:
            try:
                conn.rollback()
            except Exception:
                pass
        raise
    finally:
        if conn:
            conn.close()

# ---------- Service Bus trigger ----------
@app.service_bus_queue_trigger(
    arg_name="msg",
    queue_name="iot-telemetry",
    connection="ServiceBusConnection"
)
def process_iot_telemetry(msg: func.ServiceBusMessage):
    """
    Service Bus queue trigger: parses json, runs simple sensor checks, then stores the reading in Azure SQL.
    Raises on failure so messages are retried / dead-lettered by Service Bus.
    """
    try:
        payload = msg.get_body().decode("utf-8")
        data = json.loads(payload)
    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error: {e}; payload: {msg.get_body()}")
        # re-raise so runtime can handle retries/poison
        raise
    
    # helper to accept snake_case or camelCase keys
    def norm(d, *candidates):
        for k in candidates:
            if k in d:
                return d[k]
        return None
    
    # normalize fields
    device_id = norm(data, "device_id", "deviceId", "device")
    sensor_type = norm(data, "sensor_type", "sensorType", "type")
    value = norm(data, "value", "val")
    unit = norm(data, "unit")
    location_data = norm(data, "location", "Location") # Get the nested location object first
    latitude = norm(location_data or {}, "latitude", "lat") # Get lat from location, default to empty dict if location is None
    longitude = norm(location_data or {}, "longitude", "lon") # Get lon from location
    timestamp = norm(data, "timestamp", "time")
    
    # attach normalized names back
    data["device_id"] = device_id
    data["sensor_type"] = sensor_type
    data["value"] = value
    data["unit"] = unit
    data["latitude"] = latitude
    data["longitude"] = longitude
    data["timestamp"] = timestamp
    
    logging.info(f"Processing device={device_id} sensor={sensor_type}")
    
    # run sensor-specific logic (side-effects like alerts)
    try:
        if sensor_type in ("temperature", "temp"):
            _process_temperature(data)
        elif sensor_type == "humidity":
            _process_humidity(data)
        elif sensor_type in ("illumination", "light"):
            _process_illumination(data)
        else:
            logging.warning(f"Unknown sensor type '{sensor_type}' — still storing reading")
        
        # store to SQL
        insert_sensor_reading(data)
        logging.info("Inserted reading into sensor_data")
    except Exception as e:
        logging.exception(f"Failed processing/inserting reading: {e}")
        # re-raise to trigger retry/poison handling in Service Bus
        raise

# ---------- per-sensor processors ----------
def _process_temperature(d):
    try:
        temp = float(d.get("value"))
    except Exception:
        logging.warning("Temperature value not numeric")
        return
    loc = f"{d.get('latitude')},{d.get('longitude')}"
    logging.info(f"Temp {temp}° from {d.get('device_id')} at {loc}")
    if temp > 30:
        logging.warning(f"High temperature alert: {temp}° at {loc}")
    elif temp < 15:
        logging.warning(f"Low temperature alert: {temp}° at {loc}")

def _process_humidity(d):
    try:
        h = float(d.get("value"))
    except Exception:
        logging.warning("Humidity value not numeric")
        return
    loc = f"{d.get('latitude')},{d.get('longitude')}"
    logging.info(f"Humidity {h}% from {d.get('device_id')} at {loc}")
    if h > 70:
        logging.warning(f"High humidity alert: {h}% at {loc}")
    elif h < 30:
        logging.warning(f"Low humidity alert: {h}% at {loc}")

def _process_illumination(d):
    try:
        lux = float(d.get("value"))
    except Exception:
        logging.warning("Illumination value not numeric")
        return
    loc = f"{d.get('latitude')},{d.get('longitude')}"
    logging.info(f"Illumination {lux} lux from {d.get('device_id')} at {loc}")
    if lux < 100:
        logging.info(f"Low light detected: {lux} lux at {loc}")
    elif lux > 800:
        logging.info(f"Bright light detected: {lux} lux at {loc}")

def retrieve_sensor_data(device_id: str) -> list:
    """
    Queries the sensor_data table for history of a given device ID.
    """
    conn = None
    results = []
    
    # Simple query to get the last 100 readings for the device
    sql = """
    SELECT TOP 100 
        SensorType, Value, Unit, Latitude, Longitude, Timestamp 
    FROM 
        sensor_data 
    WHERE 
        DeviceId = ? 
    ORDER BY 
        Timestamp DESC
    """
    
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Execute the query, passing the device_id parameter
        cur.execute(sql, (device_id,))
        
        # Get column names for building the dictionary
        columns = [column[0] for column in cur.description]
        
        # Fetch all rows and map them to dictionaries
        for row in cur.fetchall():
            results.append(dict(zip(columns, row)))
            
    except Exception as e:
        # Log the full traceback if retrieval fails
        logging.exception(f"Error querying sensor data: {e}")
        raise
        
    finally:
        if conn:
            conn.close()
            
    return results

@app.route(route="sensorhistory/{device_id}", methods=["GET"])
def get_sensor_history(req: func.HttpRequest) -> func.HttpResponse:
    """
    HTTP GET endpoint to retrieve historical sensor data for a specific device.
    Example URL: /api/sensorhistory/temp-sensor-001
    """
    device_id = req.route_params.get("device_id")
    
    if not device_id:
        return func.HttpResponse(
             "Please pass a device_id in the route.",
             status_code=400
        )
    
    logging.info(f"Retrieving history for Device ID: {device_id}")
    
    try:
        data = retrieve_sensor_data(device_id)
        
        if not data:
             return func.HttpResponse(
                f"No data found for device: {device_id}",
                status_code=404
             )
        
        return func.HttpResponse(
            json.dumps(data, indent=4, default=str),  
            mimetype="application/json",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"Database error while retrieving data: {e}")
        return func.HttpResponse(
             "Error retrieving data from the database.",
             status_code=500
        )