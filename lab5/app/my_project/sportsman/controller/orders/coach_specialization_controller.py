from ..__init__ import CoachSpecializationService
from ..general_controller import GeneralController


class CoachSpecializationController(GeneralController):
    def __init__(self):
        super().__init__(CoachSpecializationService())

    