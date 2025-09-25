from my_project.sportsman.service.genral_service import GeneralService
from my_project.sportsman.service.__init__ import SportsmanHasProgram, SportsmanHasProgramDAO
from sqlalchemy.exc import IntegrityError


class SportsmanHasProgramService(GeneralService):
    def __init__(self):
        super().__init__(SportsmanHasProgramDAO(), SportsmanHasProgram)

    def insert_sportsman_program(self, sportsman_id, program_id):
        try:
            self.dao.insert_sportsman_program(sportsman_id, program_id)
        except ValueError as e:
            raise ValueError(f"Validation error: {e}")
        except IntegrityError as e:
            if "Duplicate entry" in str(e.orig):
                raise ValueError(
                    f"A record with sportsman_id={sportsman_id} and program_id={program_id} already exists."
                )
            else:
                raise