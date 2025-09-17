from my_project.sportsman.dao.general_dao import GeneralDAO
from my_project.database import db
from my_project.sportsman.dao.__init__ import Coach


class CoachSpecializationDAO(GeneralDAO):
    from my_project.sportsman.dao.__init__ import CoachSpecialization
    def __init__(self):
        super().__init__(self.CoachSpecialization)

    def get_coaches_by_specialization(specialization_id):
        coaches = db.Session.query(Coach).filter(Coach.specialization_id == specialization_id).all()
        return [coach.to_dict() for coach in coaches]