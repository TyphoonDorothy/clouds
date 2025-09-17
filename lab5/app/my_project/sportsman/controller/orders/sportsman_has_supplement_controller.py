from ..__init__ import SportsmanHasSupplementService
from ..general_controller import GeneralController


class SportsmanHasSupplementController(GeneralController):
    def __init__(self):
        super().__init__(SportsmanHasSupplementService())
