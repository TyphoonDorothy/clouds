from my_project.sportsman.dao.general_dao import GeneralDAO


class UserDAO(GeneralDAO):
    from my_project.sportsman.dao.__init__ import User
    def __init__(self):
        super().__init__(self.User)