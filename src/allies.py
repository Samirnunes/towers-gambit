import pygame

class Allies:
    def __init__(self):
        self.allies = []

    def update(self):
        for ally in self.allies:
            ally.update()

    def draw():
        for ally in self.allies:
            ally.draw()

    def get_allies(self):
        return self.allies

    def append(self, ally):
        self.allies.append(ally)
