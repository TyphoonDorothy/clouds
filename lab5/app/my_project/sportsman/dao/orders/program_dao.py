from my_project.sportsman.dao.general_dao import GeneralDAO


class ProgramDAO(GeneralDAO):
    from my_project.sportsman.dao.__init__ import Program
    def __init__(self):
        super().__init__(self.Program)