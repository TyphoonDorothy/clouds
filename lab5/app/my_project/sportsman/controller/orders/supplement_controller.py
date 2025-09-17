from ..__init__ import SupplementService
from ..general_controller import GeneralController


class SupplementController(GeneralController):
    def __init__(self):
        super().__init__(SupplementService())
