import pygame
import math
import os
from entity import Entity
from constants import *

class Bullets:
    def __init__(self):
        self.bullets = []

    def update(self):
        for bullet in self.bullets:
            bullet.update()

    def draw(self):
        for bullet in self.bullet:
            bullet.draw()

    def get_bullets(self):
        return self.bullets

    def append(self, bullet):
        self.bullets.append(bullet)


class Bullet(Entity):
    
    def __init__(self, game, size, pos, velocity, direction):
        super().__init__(game, size)
        self.animation_count = 0
        self.images = [pygame.image.load(os.path.join('assets', 'arrow.png'))]
        self.pos = pos
        self.velocity = velocity
        self.direction = direction
        game.bullets.append(self)

    def update(self):
        super().update()
        self.move()
    
    def move(self):
        '''
        Moves enemy in a iteration of the game loop.
        '''
        self.pos = (self.pos[0] + self.velocity * math.cos(self.direction) / FRAMERATE, self.pos[1] + self.velocity * math.sin(self.direction) / FRAMERATE)
