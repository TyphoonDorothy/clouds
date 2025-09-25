from my_project.database import db


class DoctorSpecialization(db.Model):
    __tablename__ = "doctor_specialization"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    doctors = db.relationship('Doctor', back_populates= 'specialization')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }
