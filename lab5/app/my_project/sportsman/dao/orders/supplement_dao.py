from my_project.sportsman.dao.general_dao import GeneralDAO


class SupplementDAO(GeneralDAO):
    from my_project.sportsman.dao.__init__ import Supplement
    def __init__(self):
        super().__init__(self.Supplement)