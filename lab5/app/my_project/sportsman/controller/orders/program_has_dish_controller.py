from ..__init__ import ProgramHasDishService
from ..general_controller import GeneralController


class ProgramHasDishController(GeneralController):
    def __init__(self):
        super().__init__(ProgramHasDishService())
