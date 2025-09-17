from my_project.database import db


class DoctorSchedule(db.Model):
    __tablename__ = "doctor_schedule"

    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, nullable=False)  # No foreign key
    schedule_date = db.Column(db.Date, nullable=False)
    time_slot = db.Column(db.String(45), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "doctor_id": self.doctor_id,
            "schedule_date": str(self.schedule_date),
            "time_slot": self.time_slot,
        }
