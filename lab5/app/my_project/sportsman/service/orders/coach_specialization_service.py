from ..__init__ import CoachSpecialization, CoachSpecializationDAO
from ..genral_service import GeneralService
from my_project.database import db


class CoachSpecializationService(GeneralService):
    def __init__(self):
        super().__init__(CoachSpecializationDAO(), CoachSpecialization)
        self.model = CoachSpecialization
    
    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False
    
    def get_coaches_by_specialization(self, specialization_id):
        coaches = db.session.query(Coach).filter(Coach.coach_specialization_id == specialization_id).all()
        return [coach.to_dict() for coach in coaches]