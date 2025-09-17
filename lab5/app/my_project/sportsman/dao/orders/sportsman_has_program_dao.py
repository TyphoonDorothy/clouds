from my_project.database import db
from sqlalchemy.sql import text
from my_project.sportsman.dao.general_dao import GeneralDAO
from sqlalchemy.exc import OperationalError


class SportsmanHasProgramDAO(GeneralDAO):
    from my_project.sportsman.domain.sportsman_has_program import SportsmanHasProgram

    def __init__(self):
        super().__init__(self.SportsmanHasProgram)

    def insert_sportsman_program(self, sportsman_id, program_id):
        query = text("CALL InsertSportsmanProgram(:sportsman_id, :program_id)")
        try:
            db.session.execute(query, {
                "sportsman_id": sportsman_id,
                "program_id": program_id
            })
            db.session.commit()
        except OperationalError as e:
            if "1644" in str(e.orig):
                raise ValueError(str(e.orig))  # Handle custom SIGNAL messages
            else:
                raise ValueError("Database error occurred while inserting the record.")