from ..__init__ import SportsmanService
from ..general_controller import GeneralController
from flask import jsonify


class SportsmanController(GeneralController):
    def __init__(self):
        super().__init__(SportsmanService())

    def insert_noname_rows(self):
        try:
            self.service.insert_noname_sportsmen()
            return jsonify({"message": "10 Noname sportsmen added successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
