from ..__init__ import DoctorSpecialization, DoctorSpecializationDAO
from ..genral_service import GeneralService
from my_project.database import db
from my_project.sportsman.dao.__init__ import Doctor  # Додайте імпорт класу Doctor

class DoctorSpecializationService(GeneralService):
    def __init__(self):
        super().__init__(DoctorSpecializationDAO(), DoctorSpecialization)
        self.model = DoctorSpecialization
    
    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False
    
    def get_doctors_by_specialization(self, specialization_id):
        doctors = db.session.query(Doctor).filter(Doctor.coach_specialization_id == specialization_id).all()
        return [doctor.to_dict() for doctor in doctors]
