from ..__init__ import DoctorsContactService
from ..general_controller import GeneralController


class DoctorsContactController(GeneralController):
    def __init__(self):
        super().__init__(DoctorsContactService())
