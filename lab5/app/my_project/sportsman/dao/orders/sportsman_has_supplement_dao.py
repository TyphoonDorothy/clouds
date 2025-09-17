from my_project.sportsman.dao.general_dao import GeneralDAO


class SportsmanHasSupplementDAO(GeneralDAO):
    from my_project.sportsman.dao.__init__ import SportsmanHasSupplement
    def __init__(self):
        super().__init__(self.SportsmanHasSupplement)