from my_project.database import db
from ..__init__ import DoctorSchedule, DoctorScheduleDAO
from ..genral_service import GeneralService


class DoctorScheduleService(GeneralService):
    def __init__(self):
        super().__init__(DoctorScheduleDAO(), DoctorSchedule)
        self.model = DoctorSchedule

    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False
