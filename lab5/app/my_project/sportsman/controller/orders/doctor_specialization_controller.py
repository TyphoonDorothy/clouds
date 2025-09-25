from ..__init__ import DoctorSpecializationService
from ..general_controller import GeneralController


class DoctorSpecializationController(GeneralController):
    def __init__(self):
        super().__init__(DoctorSpecializationService())

    