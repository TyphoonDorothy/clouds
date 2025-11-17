
from my_project.database import db

class User(db.Model):
    __tablename__ = "user"   # change this if your table name is different

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"
