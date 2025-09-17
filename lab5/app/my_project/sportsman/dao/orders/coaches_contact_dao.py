from my_project.sportsman.dao.general_dao import GeneralDAO


class CoachesContactDAO(GeneralDAO):
    from my_project.sportsman.dao.__init__ import CoachesContact
    def __init__(self):
        super().__init__(self.CoachesContact)