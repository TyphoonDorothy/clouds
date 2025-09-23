from my_project.database import db


class Program(db.Model):
    __tablename__ = "program"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    sportsman = db.relationship('SportsmanHasProgram', back_populates= 'program')
    dish = db.relationship('ProgramHasDish', back_populates='program')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }

