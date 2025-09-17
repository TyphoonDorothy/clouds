from ..__init__ import SportsmanHasSupplement, SportsmanHasSupplementDAO
from ..genral_service import GeneralService
from my_project.database import db


class SportsmanHasSupplementService(GeneralService):
    def __init__(self):
        super().__init__(SportsmanHasSupplementDAO(), SportsmanHasSupplement)
        self.model = SportsmanHasSupplement
    
    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False
        