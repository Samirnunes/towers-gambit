import pygame

class Entities:
    def __init__(self):
        self.entities = []

    def update(self):
        for entity in self.entities:
            entity.update()

    def draw(self, game):
        for entity in self.entities:
            entity.draw(game)

    def get_entities(self):
        return self.entities

    def append(self, entity):
        self.entities.append(entity)
