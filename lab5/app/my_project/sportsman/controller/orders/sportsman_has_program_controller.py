class SportsmanHasProgramController(GeneralController):
    def __init__(self):
        super().__init__(SportsmanHasProgramService())

    def insert_junction_entry(self):
        try:
            data = request.json
            sportsman_id = data.get("sportsman_id")
            program_id = data.get("program_id")

            if not sportsman_id or not program_id:
                return handle_error("Missing required fields: sportsman_id, program_id.", 400)

            self.service.insert_sportsman_program(sportsman_id, program_id)
            return handle_response({"message": "Junction entry created successfully."}, 201)
        except ValueError as ve:
            return handle_error(str(ve), 409)
        except Exception as e:
            return handle_error(f"Unexpected error: {str(e)}", 500)

    def get_by_id(self, sportsman_id, program_id):
        entity = self.service.dao.model.query.get((sportsman_id, program_id))
        if entity:
            return handle_response(entity.to_dict(), 200)
        return handle_error("Not found", 404)

    def update(self, sportsman_id, program_id):
        try:
            data = request.json
            new_sportsman_id = data.get("new_sportsman_id")
            new_program_id = data.get("new_program_id")

            entity = self.service.dao.model.query.get((sportsman_id, program_id))
            if not entity:
                return handle_error("Original relationship not found", 404)

            entity.sportsman_id = new_sportsman_id
            entity.program_id = new_program_id
            db.session.commit()
            return handle_response({"message": "Relationship updated successfully"}, 200)
        except Exception as e:
            return handle_error(f"Unexpected error: {str(e)}", 500)

    def delete(self, sportsman_id, program_id):
        entity = self.service.dao.model.query.get((sportsman_id, program_id))
        if not entity:
            return handle_error("Relationship not found", 404)
        db.session.delete(entity)
        db.session.commit()
        return handle_response({"message": "Relationship deleted successfully"}, 200)
