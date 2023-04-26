class Entities:
    def __init__(self):
        '''
        Initializes an empty collection of entities.
        '''
        self.entities = []

    def update(self):
        '''
        Updates all entities in the collection.
        '''
        for entity in self.entities:
            entity.update()

    def draw(self):
        '''
        Draws all entities in the collection.
        '''
        for entity in self.entities:
            entity.draw()

    def get_entities(self):
        '''
        Returns the list of entities in the collection.
        '''
        return self.entities

    def append(self, entity):
        '''
        Adds an entity to the collection.
        '''
        self.entities.append(entity)

    def remove(self, entity):
        '''
        Removes an entity from the collection.
        '''
        self.entities.remove(entity)

    def empty(self):
        '''
        Returns True if the collection is empty, False otherwise.
        '''
        return len(self.entities) == 0
    
    def __len__(self):
        '''
        Returns the number of entities in the collection.
        '''
        return len(self.entities)
