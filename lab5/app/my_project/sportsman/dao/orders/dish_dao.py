from my_project.sportsman.dao.general_dao import GeneralDAO
from sqlalchemy import text
from my_project.database import db


class DishDAO(GeneralDAO):
    from my_project.sportsman.dao.__init__ import Dish
    def __init__(self):
        super().__init__(self.Dish)

    def insert_dish(self, name, calories):
        query = text("""
            CALL InsertDish(
                :name_param,
                :calories_param
            )
        """)
        db.session.execute(query, {
            "name_param": name,
            "calories_param": calories,
        })
        db.session.commit()

    def get_aggregate(self, operation):
        """
        Call the stored procedure to get an aggregate value for the specified column.
        """
        query = text("CALL GetDishAggregate(:operation, @result)")
        db.session.execute(query, {"operation": operation})
        result_query = text("SELECT @result AS result")
        result = db.session.execute(result_query).fetchone()
        return result[0]