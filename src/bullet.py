import pygame
import math
import os
from entity import Entity
from constants import *

class Bullet(Entity):
    
    def __init__(self, game, size, pos, velocity, direction, damage, penetration_power):
        super().__init__(game, size)
        self.animation_count = 0
        self.images = [pygame.image.load(os.path.join('assets', 'arrow.png'))]
        self.pos = pos
        self.velocity = velocity
        self.direction = direction
        self.damage = damage
        self.penetration_power = penetration_power
        self.collided_enemies = []
        game.bullets.append(self)

    def update(self):
        super().update()
        self.move()
        valid_collision = self.find_collision()
        if valid_collision:
            self.do_damage()
        if len(self.collided_enemies) >= self.penetration_power:
            self.remove()
    
    def move(self):
        '''
        Moves bullet in a iteration of the game loop.
        '''
        self.pos = (self.pos[0] + self.velocity * math.cos(self.direction) / FRAMERATE, self.pos[1] + self.velocity * math.sin(self.direction) / FRAMERATE)

    def find_collision(self):
        '''
        Returns if an enemy has been collided and saves the enemy which was hit in the collided enemies list.
        Each bullet can hit only one enemy.
        '''
        collided = False
        for enemy in self.game.enemies.get_entities():
            collided = self.collide(enemy.pos[0], enemy.pos[1], enemy.size[0], enemy.size[1])
            if collided and enemy not in self.collided_enemies:
                self.collided_enemies.append(enemy)
                break
        return collided

    def do_damage(self):
        '''
        Does bullet damage to the last collided enemy.
        '''
        self.collided_enemies[-1].damage(self.damage)

    def remove(self):
        '''
        Removes bullet from game.
        '''
        self.game.bullets.remove(self)
        self.game.entities.remove(self)
