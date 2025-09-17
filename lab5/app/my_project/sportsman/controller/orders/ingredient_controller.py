from ..__init__ import IngredientService
from ..general_controller import GeneralController


class IngredientController(GeneralController):
    def __init__(self):
        super().__init__(IngredientService())
