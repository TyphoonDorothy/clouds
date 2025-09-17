from my_project.database import db


class Supplement(db.Model):
    __tablename__ = "supplement"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)

    sportsman = db.relationship('SportsmanHasSupplement', back_populates= 'supplements')


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        } 