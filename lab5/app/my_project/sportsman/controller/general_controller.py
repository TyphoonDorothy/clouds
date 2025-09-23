from flask import jsonify, request
from my_project.sportsman.controller.utils import handle_error, handle_response

class GeneralController:
    def __init__(self, service):
        self.service = service

    def get_all(self):
        data = self.service.get_all()
        return handle_response(data)
    
    def get_by_id(self, entity_id):
        entity = self.service.get_by_id(entity_id)

        if entity:
            return handle_response(entity.to_dict())
        return handle_error("Resource not found", 404)
    
    def create(self):
        try:
            data = request.json
            entity = self.service.create(**data)
            return handle_response(entity.to_dict(), 201)
        except KeyError as e:
            return handle_error(f"Missing required field: {str(e)}", 404)
        except Exception as e:
            return handle_error(f"Failed to create resourse: {str(e)}", 500)
        
    def update(self, entity_id):
        data = request.json
        entity = self.service.update(entity_id, **data)
        if entity:
            return handle_response(entity.to_dict())
        return handle_error("Resource not found", 404)
    
    def delete(self, entity_id):
        success = self.service.delete(entity_id)
        if success:
            return handle_response({"message": "Resource deleted successfully"})
        return handle_error("Resource not found", 404)