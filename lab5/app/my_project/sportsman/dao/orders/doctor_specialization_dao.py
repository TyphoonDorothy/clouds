from my_project.sportsman.dao.general_dao import GeneralDAO
from my_project.database import db
from my_project.sportsman.dao.__init__ import Doctor, DoctorSpecialization


class DoctorSpecializationDAO(GeneralDAO):
    def __init__(self):
        super().__init__(DoctorSpecialization)

    def get_doctors_by_specialization(self, specialization_id):
        doctors = db.session.query(Doctor).filter(Doctor.specialization_id == specialization_id).all()
        return [doctor.to_dict() for doctor in doctors]
