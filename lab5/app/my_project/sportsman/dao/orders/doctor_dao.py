from my_project.sportsman.dao.general_dao import GeneralDAO

from my_project.database import db
from sqlalchemy import text

class DoctorDAO(GeneralDAO):
    from my_project.sportsman.dao.__init__ import Doctor
    def __init__(self):
        super().__init__(self.Doctor)

    def execute_generate_databases_and_tables(self):
        try:
            db.session.execute(text("CALL GenerateDatabasesAndTables()"))
            db.session.commit()
            return {"message": "Databases and tables generated successfully"}
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}