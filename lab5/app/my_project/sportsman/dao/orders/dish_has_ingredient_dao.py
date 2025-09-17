from my_project.sportsman.dao.general_dao import GeneralDAO


class DishHasIngredientDAO(GeneralDAO):
    from my_project.sportsman.dao.__init__ import DishHasIngredient
    def __init__(self):
        super().__init__(self.DishHasIngredient)