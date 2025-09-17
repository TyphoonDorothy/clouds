from my_project.sportsman.dao.general_dao import GeneralDAO
from sqlalchemy import text
from my_project.database import db

class SportsmanDAO(GeneralDAO):
    from my_project.sportsman.dao.__init__ import Sportsman
    def __init__(self):
        super().__init__(self.Sportsman)

    def insert_noname_sportsmen(self):
        # Call the stored procedure to insert 10 Noname technicians
        query = text("CALL InsertNonameRows()")
        db.session.execute(query)
        db.session.commit()