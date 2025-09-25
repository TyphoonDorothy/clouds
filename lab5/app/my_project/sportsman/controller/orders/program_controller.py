from ..__init__ import ProgramService
from ..general_controller import GeneralController


class ProgramController(GeneralController):
    def __init__(self):
        super().__init__(ProgramService())
