from my_project.database import db


class Sportsman(db.Model):
    __tablename__ = "sportsman"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False, name="sportsman_surname")  # map to DB column
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)

    program = db.relationship('SportsmanHasProgram', back_populates='sportsman')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
        }
