import pygame

class Enemies:
    def __init__(self):
        self.enemies = []

    def update(self):
        for enemy in self.enemies:
            enemy.update()

    def draw(self):
        for enemy in self.enemies:
            enemy.draw()

    def get_enemies(self):
        return self.enemies

    def append(self, enemy):
        self.enemies.append(enemy)
