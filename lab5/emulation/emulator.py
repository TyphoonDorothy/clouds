import asyncio
import json
import random
from datetime import datetime, timezone
import aiohttp
import hashlib
import hmac
import base64
from urllib.parse import quote_plus

# ============= CONFIGURATION - EDIT THESE =============
IOT_HUB_NAME = "clouds-iot-hub-lab"

# Device keys for each sensor
TEMP_SENSOR_KEY = "dT9C9POBLkknpdpScOPf2Hhexgv1cpyGJwRecOOizoE="
HUMIDITY_SENSOR_KEY = "wsKs3uGMXC3/+vQp9RIfPnSOXygGm1p4JbPDrRkMYhg="
LIGHT_SENSOR_KEY = "ZFDZV6UNk/Yrok8GIIO/j9Lu+ElmL/3/UQkGRrCj/mg="

SERVICE_BUS_NAMESPACE = "clouds-service-bus"
SERVICE_BUS_QUEUE = "iot-telemetry"
SERVICE_BUS_KEY = "bO+xvv/Y3hELOiLg/WXqEFnZBCDKjTdLd+ASbAvazeE="

REQUEST_INTERVAL_MS = 100   # change this value (milliseconds)
REQUEST_INTERVAL = REQUEST_INTERVAL_MS / 1000

# ======================================================

def generate_sas_token(hostname, device_id, key):
    """Generate SAS token for authentication"""
    resource_uri = f"{hostname}/devices/{device_id}"
    resource_uri = quote_plus(resource_uri)
    expires = int(datetime.now(timezone.utc).timestamp()) + 3600
    to_sign = f"{resource_uri}\n{expires}"
    
    signature = hmac.new(
        base64.b64decode(key),
        to_sign.encode('utf-8'),
        hashlib.sha256
    ).digest()
    signature = quote_plus(base64.b64encode(signature).decode('utf-8'))
    
    return f"SharedAccessSignature sr={resource_uri}&sig={signature}&se={expires}"

async def send_to_iot_hub(device_id, data):
    """Send data to IoT Hub"""
    hostname = f"{IOT_HUB_NAME}.azure-devices.net"
    sas_token = generate_sas_token(hostname, device_id, DEVICE_KEY)
    
    url = f"https://{hostname}/devices/{device_id}/messages/events?api-version=2020-03-13"
    headers = {
        "Authorization": sas_token,
        "Content-Type": "application/json"
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, headers=headers) as response:
            if response.status in [200, 204]:
                print(f"✓ {data['sensor_type']}: {data['value']}")
            else:
                print(f"✗ Error {response.status}")

async def send_to_service_bus(data):
    """Send data to Service Bus Queue"""
    uri = f"https://{SERVICE_BUS_NAMESPACE}.servicebus.windows.net/{SERVICE_BUS_QUEUE}"
    encoded_uri = quote_plus(uri)
    expires = int(datetime.now(timezone.utc).timestamp()) + 3600
    to_sign = f"{encoded_uri}\n{expires}"
    
    signature = hmac.new(
        SERVICE_BUS_KEY.encode('utf-8'),
        to_sign.encode('utf-8'),
        hashlib.sha256
    ).digest()
    signature = quote_plus(base64.b64encode(signature).decode('utf-8'))
    
    sas_token = f"SharedAccessSignature sr={encoded_uri}&sig={signature}&se={expires}&skn=RootManageSharedAccessKey"
    
    url = f"{uri}/messages"
    headers = {
        "Authorization": sas_token,
        "Content-Type": "application/json"
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, headers=headers) as response:
            if response.status in [200, 201]:
                print(f"  → Service Bus")

async def temperature_sensor():
    """Temperature sensor - sends every 2 seconds"""
    device_id = "temp"
    hostname = f"{IOT_HUB_NAME}.azure-devices.net"
    temp = 22.0
    
    while True:
        temp += random.uniform(-0.5, 0.5)
        
        data = {
            "device_id": device_id,
            "sensor_type": "temperature",
            "value": round(temp, 2),
            "unit": "Celsius",
            "location": {"lat": 49.8397, "lon": 24.0297},
            "timestamp": datetime.now(timezone.utc).isoformat() + "Z"
        }
        
        sas_token = generate_sas_token(hostname, device_id, TEMP_SENSOR_KEY)
        url = f"https://{hostname}/devices/{device_id}/messages/events?api-version=2020-03-13"
        headers = {"Authorization": sas_token, "Content-Type": "application/json"}
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data, headers=headers) as response:
                if response.status in [200, 204]:
                    print(f"✓ {data['sensor_type']}: {data['value']}")
        
        await send_to_service_bus(data)
        await asyncio.sleep(REQUEST_INTERVAL)

async def humidity_sensor():
    """Humidity sensor - sends every 3 seconds"""
    device_id = "humidity"
    hostname = f"{IOT_HUB_NAME}.azure-devices.net"
    
    while True:
        humidity = random.uniform(45, 65)
        
        data = {
            "device_id": device_id,
            "sensor_type": "humidity",
            "value": round(humidity, 2),
            "unit": "percent",
            "location": {"lat": 49.8400, "lon": 24.0300},
            "timestamp": datetime.now(timezone.utc).isoformat() + "Z"
        }
        
        sas_token = generate_sas_token(hostname, device_id, HUMIDITY_SENSOR_KEY)
        url = f"https://{hostname}/devices/{device_id}/messages/events?api-version=2020-03-13"
        headers = {"Authorization": sas_token, "Content-Type": "application/json"}
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data, headers=headers) as response:
                if response.status in [200, 204]:
                    print(f"✓ {data['sensor_type']}: {data['value']}")
        
        await send_to_service_bus(data)
        await asyncio.sleep(REQUEST_INTERVAL)

async def light_sensor():
    """Light sensor - sends every 1.5 seconds"""
    device_id = "light"
    hostname = f"{IOT_HUB_NAME}.azure-devices.net"
    
    while True:
        hour = datetime.now(timezone.utc).hour
        base_lux = 500 if 6 <= hour <= 18 else 50
        lux = base_lux + random.uniform(-50, 50)
        
        data = {
            "device_id": device_id,
            "sensor_type": "illumination",
            "value": round(max(0, lux), 2),
            "unit": "lux",
            "location": {"lat": 49.8395, "lon": 24.0295},
            "timestamp": datetime.now(timezone.utc).isoformat() + "Z"
        }
        
        sas_token = generate_sas_token(hostname, device_id, LIGHT_SENSOR_KEY)
        url = f"https://{hostname}/devices/{device_id}/messages/events?api-version=2020-03-13"
        headers = {"Authorization": sas_token, "Content-Type": "application/json"}
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data, headers=headers) as response:
                if response.status in [200, 204]:
                    print(f"✓ {data['sensor_type']}: {data['value']}")
        
        await send_to_service_bus(data)
        await asyncio.sleep(REQUEST_INTERVAL)

async def main():
    print("Starting IoT Sensors...\n")
    
    # Run all 3 sensors concurrently
    await asyncio.gather(
        temperature_sensor(),
        humidity_sensor(),
        light_sensor()
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\nStopped.")