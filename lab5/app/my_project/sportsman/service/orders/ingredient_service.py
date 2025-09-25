from ..__init__ import Ingredient, IngredientDAO
from ..genral_service import GeneralService
from my_project.database import db


class IngredientService(GeneralService):
    def __init__(self):
        super().__init__(IngredientDAO(), Ingredient)
        self.model = Ingredient
    
    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False
        