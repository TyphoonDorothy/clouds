from ..__init__ import DishHasIngredientService
from ..general_controller import GeneralController


class DishHasIngredientController(GeneralController):
    def __init__(self):
        super().__init__(DishHasIngredientService())

    def get_by_id(self, dish_id, ingredient_id):
        entity = self.service.dao.model.query.get((dish_id, ingredient_id))
        if entity:
            return entity.to_dict(), 200
        return {"error": "Not found"}, 404
