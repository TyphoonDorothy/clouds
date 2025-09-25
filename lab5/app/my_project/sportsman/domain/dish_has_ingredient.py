from my_project.database import db
from sqlalchemy import ForeignKey



class DishHasIngredient(db.Model):
    __tablename__ = "dish_ingredient"
    
    dish_id = db.Column(db.Integer, ForeignKey('dish.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, ForeignKey('ingredient.id'), primary_key=True)

    dish = db.relationship('Dish', back_populates= 'ingredient')
    ingredient = db.relationship('Ingredient', back_populates= 'dish')

    def to_dict(self):
        return {
            "dish_id": self.dish_id,
            "ingredient_id": self.ingredient_id,
        } 