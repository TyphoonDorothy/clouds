from ..__init__ import DishHasIngredientService
from ..general_controller import GeneralController


class DishHasIngredientController(GeneralController):
    def __init__(self):
        super().__init__(DishHasIngredientService())
