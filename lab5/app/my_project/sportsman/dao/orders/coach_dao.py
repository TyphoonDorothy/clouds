from my_project.sportsman.dao.general_dao import GeneralDAO


class CoachDAO(GeneralDAO):
    from my_project.sportsman.dao.__init__ import Coach
    def __init__(self):
        super().__init__(self.Coach)