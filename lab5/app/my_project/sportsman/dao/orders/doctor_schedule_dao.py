from my_project.database import db
from ..__init__ import DoctorSchedule
from my_project.sportsman.dao.general_dao import GeneralDAO


class DoctorScheduleDAO(GeneralDAO):
    def __init__(self):
        super().__init__(DoctorSchedule)
