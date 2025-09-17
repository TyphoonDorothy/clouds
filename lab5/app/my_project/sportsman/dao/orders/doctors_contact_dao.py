from my_project.sportsman.dao.general_dao import GeneralDAO


class DoctorsContactDAO(GeneralDAO):
    from my_project.sportsman.dao.__init__ import DoctorsContact
    def __init__(self):
        super().__init__(self.DoctorsContact)