class Entities:
    def __init__(self):
        self.entities = []

    def update(self):
        for entity in self.entities:
            entity.update()

    def draw(self):
        for entity in self.entities:
            entity.draw()

    def get_entities(self):
        return self.entities

    def append(self, entity):
        self.entities.append(entity)

    def remove(self, entity):
        self.entities.remove(entity)
