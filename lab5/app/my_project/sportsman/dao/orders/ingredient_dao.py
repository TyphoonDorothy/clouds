from my_project.sportsman.dao.general_dao import GeneralDAO


class IngredientDAO(GeneralDAO):
    from my_project.sportsman.dao.__init__ import Ingredient
    def __init__(self):
        super().__init__(self.Ingredient)