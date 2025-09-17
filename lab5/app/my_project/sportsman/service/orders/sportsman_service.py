from ..__init__ import Sportsman, SportsmanDAO
from ..genral_service import GeneralService
from my_project.database import db


class SportsmanService(GeneralService):
    def __init__(self):
        super().__init__(SportsmanDAO(), Sportsman)
        self.model = Sportsman
    
    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False

    def insert_noname_sportsmen(self):
        # Call DAO to execute the stored procedure
        self.dao.insert_noname_sportsmen()
        