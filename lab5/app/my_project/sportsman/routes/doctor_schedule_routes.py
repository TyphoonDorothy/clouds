from flask import Blueprint
from flasgger import swag_from
from ..controller.orders.doctor_schedule_controller import DoctorScheduleController

doctor_schedule_bp = Blueprint("doctor_schedule", __name__)
doctor_schedule_controller = DoctorScheduleController()


@doctor_schedule_bp.route("/doctor_schedule", methods=['GET'])
@swag_from({
    'tags': ['DoctorSchedule'],
    'responses': {
        200: {
            'description': 'List of all doctor schedules',
            'examples': {
                'application/json': [
                    {"id": 1, "doctor_id": 3, "schedule_date": "2025-09-23", "time_slot": "09:00-10:00"}
                ]
            }
        }
    }
})
def get_all_schedules():
    return doctor_schedule_controller.get_all()


@doctor_schedule_bp.route("/doctor_schedule/<int:schedule_id>", methods=['GET'])
@swag_from({
    'tags': ['DoctorSchedule'],
    'parameters': [
        {'name': 'schedule_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the schedule'}
    ],
    'responses': {
        200: {
            'description': 'Schedule details',
            'examples': {'application/json': {"id": 1, "doctor_id": 3, "schedule_date": "2025-09-23", "time_slot": "09:00-10:00"}}
        },
        404: {'description': 'Schedule not found'}
    }
})
def get_schedule_by_id(schedule_id):
    return doctor_schedule_controller.get_by_id(schedule_id)


@doctor_schedule_bp.route("/doctor_schedule", methods=['POST'])
@swag_from({
    'tags': ['DoctorSchedule'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'properties': {
                    'doctor_id': {'type': 'integer'},
                    'schedule_date': {'type': 'string', 'format': 'date'},
                    'time_slot': {'type': 'string'}
                },
                'required': ['doctor_id', 'schedule_date', 'time_slot']
            }
        }
    ],
    'responses': {
        201: {'description': 'Schedule created successfully'}
    }
})
def add_schedule():
    return doctor_schedule_controller.create()


@doctor_schedule_bp.route("/doctor_schedule/<int:schedule_id>", methods=['PATCH'])
@swag_from({
    'tags': ['DoctorSchedule'],
    'parameters': [
        {'name': 'schedule_id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'properties': {
                    'doctor_id': {'type': 'integer'},
                    'schedule_date': {'type': 'string', 'format': 'date'},
                    'time_slot': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Schedule updated successfully'},
        404: {'description': 'Schedule not found'}
    }
})
def update_schedule(schedule_id):
    return doctor_schedule_controller.update(schedule_id)


@doctor_schedule_bp.route("/doctor_schedule/<int:schedule_id>", methods=['DELETE'])
@swag_from({
    'tags': ['DoctorSchedule'],
    'parameters': [
        {'name': 'schedule_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Schedule deleted successfully'},
        404: {'description': 'Schedule not found'}
    }
})
def delete_schedule(schedule_id):
    return doctor_schedule_controller.delete(schedule_id)
