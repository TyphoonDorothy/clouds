class GeneralService:
    def __init__(self, dao, domain_class):
        self.dao = dao
        self.domain_class = domain_class

    def create(self, **kwargs):
        entity = self.domain_class(**kwargs)
        self.dao.add(entity)
        return entity
    
    def get_all(self):
        return [entity.to_dict() for entity in self.dao.get_all()]
    
    def get_by_id(self, entity_id):
        return self.dao.get_by_id(entity_id)
    
    def update(self, entity_id, **kwargs):
        entity = self.dao.get_by_id(entity_id)
        if not entity:
            return None
        

        for key, value in kwargs.items():
            if hasattr(entity, key) and value is not None:
                setattr(entity, key, value)

        self.dao.update()
        return entity

    def delete(self, entity_id):
        entity = self.dao.get_by_id(entity_id)
        if not entity:
            return False
        self.dao.delete(entity)
        return True