from my_project.database import db
from sqlalchemy import ForeignKey


class Coach(db.Model):
    __tablename__ = "coach"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    coach_specialization_id = db.Column(db.Integer, ForeignKey('coach_specialization.id'), nullable=False)
    contact_id = db.Column(db.Integer, ForeignKey('coach_contact.id'), unique=True, nullable=False)


    specialization = db.relationship('CoachSpecialization', back_populates='coaches')
    contact = db.relationship('CoachesContact', back_populates='coaches')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "specialization_id": self.coach_specialization_id,
            "contact_id": self.contact_id,
        } 
