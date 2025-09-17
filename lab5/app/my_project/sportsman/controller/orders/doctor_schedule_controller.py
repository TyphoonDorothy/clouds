from ..__init__ import DoctorScheduleService
from ..general_controller import GeneralController


class DoctorScheduleController(GeneralController):
    def __init__(self):
        super().__init__(DoctorScheduleService())
