from my_project.database import db
from sqlalchemy import ForeignKey



class SportsmanHasProgram(db.Model):
    __tablename__ = "sportsman_has_program"
    
    sportsman_id = db.Column(db.Integer, ForeignKey('sportsman.id'), primary_key=True)
    program_id = db.Column(db.Integer, ForeignKey('program.id'), primary_key=True)

    sportsman = db.relationship('Sportsman', back_populates= 'program')
    program = db.relationship('Program', back_populates= 'sportsman')

    def to_dict(self):
        return {
            "sportsman_id": self.sportsman_id,
            "program_id": self.program_id,
        } 