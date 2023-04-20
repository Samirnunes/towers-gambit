import pygame
import math
from entity import Entity
from general_game_constants import *
from ally_constants import *

class Bullet(Entity):
    
    def __init__(self, game, ally, size, pos, velocity, direction, damage, penetration_power):
        super().__init__(game, size)
        self.animation_count = 0
        self.ally = ally
        self.determine_images_based_on_ally()
        self.pos = pos
        self.velocity = velocity
        self.direction = direction
        self.damage = damage
        self.penetration_power = penetration_power
        self.collided_enemies = []
        game.bullets.append(self)

    def determine_images_based_on_ally(self):
        self.images = PIECES_CONSTANTS[self.ally.piece.value]['bullet_images']

    def update(self):
        super().update()
        self.move()
        valid_collision = self.find_collision()
        if valid_collision:
            self.do_damage()
        if len(self.collided_enemies) >= self.penetration_power and self.animation_count == len(self.images) - 1:
            self.remove()

    def draw(self):
        '''
        Draws the bullet in the given Pygame's window.
        '''

        # Precisa ser melhorada para fazer uma animação de "perfuração" no inimigo.
        # Também é interessante fazer uma animação de "morte" do inimigo em outra função, na classe "Enemy".

        if self.find_collision():
            self.animation_count = 3
            while self.animation_count != len(self.images) - 1:
                image = self.images[self.animation_count]
                image = pygame.transform.scale(image, self.size)
                self.game.window.blit(image, (self.pos[0] - self.size[0] / 2, self.pos[1] - self.size[1] / 2))
                self.animation_count += 1
        else:
            image = self.images[self.animation_count]
            image = pygame.transform.scale(image, self.size)
            self.game.window.blit(image, (self.pos[0] - self.size[0] / 2, self.pos[1] - self.size[1] / 2))
            self.animation_count += 1
            if self.animation_count > 2:
                self.animation_count = 0
    
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
