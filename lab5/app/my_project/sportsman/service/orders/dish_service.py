from ..__init__ import Dish, DishDAO
from ..genral_service import GeneralService
from my_project.database import db


class DishService(GeneralService):
    def __init__(self):
        super().__init__(DishDAO(), Dish)
        self.model = Dish
    
    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False

    def insert_dish(self, name, calories):
        self.dao.insert_dish(name, calories)

    def get_dish_aggregate(self, operation):
        valid_operations = {"MAX", "MIN", "SUM", "AVG"}
        if operation.upper() not in valid_operations:
            raise ValueError(f"Invalid operation '{operation}'. Valid options are: {valid_operations}")
        return self.dao.get_aggregate(operation.upper())
        