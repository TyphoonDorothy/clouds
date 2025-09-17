from my_project.database import db
from sqlalchemy import ForeignKey



class ProgramHasDish(db.Model):
    __tablename__ = "program_has_dish"
    
    program_id = db.Column(db.Integer, ForeignKey('program.id'), primary_key=True)
    dish_id = db.Column(db.Integer, ForeignKey('dish.id'), primary_key=True)

    program = db.relationship('Program', back_populates= 'dish')
    dish = db.relationship('Dish', back_populates= 'program')

    def to_dict(self):
        return {
            "program_id": self.program_id,
            "dish_id": self.dish_id,
        } 