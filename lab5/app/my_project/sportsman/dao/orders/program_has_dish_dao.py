from my_project.sportsman.dao.general_dao import GeneralDAO


class ProgramHasDishDAO(GeneralDAO):
    from my_project.sportsman.dao.__init__ import ProgramHasDish
    def __init__(self):
        super().__init__(self.ProgramHasDish)