from my_project.database import db
from sqlalchemy.exc import NoResultFound
from my_project.database import db


class GeneralDAO:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.query.all()

    def add(self, entity):
        db.session.add(entity)
        db.session.commit()

    def delete(self, composite_key):
        entity = db.session.get(self.model, composite_key)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False

    def get_by_id(self, composite_key):
        try:
            return db.session.get(self.model, composite_key)
        except NoResultFound:
            return None

    def update(self):
        db.session.commit()