from my_project.database import db
from sqlalchemy import ForeignKey



class SportsmanHasSupplement(db.Model):
    __tablename__ = "sportsman_has_supplement"
    
    sportsman_id = db.Column(db.Integer, ForeignKey('sportsman.id'), primary_key=True)
    supplement_id = db.Column(db.Integer, ForeignKey('supplement.id'), primary_key=True)

    sportsman = db.relationship('Sportsman', back_populates= 'supplements')
    supplements = db.relationship('Supplement', back_populates= 'sportsman')

    def to_dict(self):
        return {
            "sportsman_id": self.sportsman_id,
            "supplement_id": self.supplement_id,
        } 