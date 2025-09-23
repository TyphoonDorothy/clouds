from my_project.database import db


class CoachesContact(db.Model):
    __tablename__ = "coach_contact"


    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    coaches = db.relationship('Coach', back_populates= 'contact')

    def to_dict(self):
        return {
            "id": self.id,
            "phone": self.phone,
            "email": self.email,
        }
