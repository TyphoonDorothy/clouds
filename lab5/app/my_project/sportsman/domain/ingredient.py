from my_project.database import db


class Ingredient(db.Model):
    __tablename__ = "ingredient"


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    calories = db.Column(db.Float, nullable=False)

    dish = db.relationship('DishHasIngredient', back_populates= 'ingredient')



    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "calories": self.calories,
        } 