from ..__init__ import ProgramHasDish, ProgramHasDishDAO
from ..genral_service import GeneralService
from my_project.database import db


class ProgramHasDishService(GeneralService):
    def __init__(self):
        super().__init__(ProgramHasDishDAO(), ProgramHasDish)
        self.model = ProgramHasDish
    
    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False
        