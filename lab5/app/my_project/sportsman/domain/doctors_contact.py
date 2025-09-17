from my_project.database import db


class DoctorsContact(db.Model):
    __tablename__ = "doctors_contact"


    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    doctors = db.relationship('Doctor', back_populates= 'contact')

    def to_dict(self):
        return {
            "id": self.id,
            "phone": self.phone,
            "email": self.email,
        }
