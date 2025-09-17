from ..__init__ import CoachesContactService
from ..general_controller import GeneralController


class CoachesContactController(GeneralController):
    def __init__(self):
        super().__init__(CoachesContactService())
