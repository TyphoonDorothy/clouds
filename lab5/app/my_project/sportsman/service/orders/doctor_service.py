from ..__init__ import Doctor, DoctorDAO
from ..genral_service import GeneralService
from my_project.database import db


class DoctorService(GeneralService):
    def __init__(self):
        super().__init__(DoctorDAO(), Doctor)
        self.model = Doctor
    
    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False

    def generate_databases_and_tables(self):
        return self.dao.execute_generate_databases_and_tables()