from my_project.database import db


class Dish(db.Model):
    __tablename__ = "dish"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    calories = db.Column(db.Float, nullable=False)

    ingredient = db.relationship('DishHasIngredient', back_populates= 'dish')
    program = db.relationship('ProgramHasDish', back_populates='dish')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "calories": self.calories,
        } 