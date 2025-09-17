from ..__init__ import CoachService
from ..general_controller import GeneralController


class CoachController(GeneralController):
    def __init__(self):
        super().__init__(CoachService())
