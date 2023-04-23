import os
import math
from entity import Entity
from constants import GAME, ENEMY

class Enemy(Entity):
    
    def __init__(self, game):
        super().__init__(game)
        self.health = None
        self.velocity = None
        self.path = game.map.get_path()
        self.path_index = 0
        self.pos = list(self.path[0])
        self.game.enemies.append(self)
    
    def update(self):
        super().update()
        if self.path_index == len(self.path) - 1:
            self.game.player.receive_damage()
            self.game.enemies.remove(self)
        if self.health <= 0:
            self.game.enemies.remove(self)
        self.move()


    def kill(self):
        '''
        Cleanup actions. 'alive' should be called before to check if the enmy is dead.
        '''
        self.health = 0
        if self.pos != list(self.path[-1]):
            money = 5*self.CARD.HEALTH + self.velocity #can be modified later to make it more playable
            self.game.player.add_money(money)
        self.game.enemies.remove(self)

    def move(self):
        '''
        Moves enemy in a iteration of the game loop.
        '''
        if self.path_index < len(self.path) - 1:
            dest_pos = list(self.path[self.path_index + 1])
            delta = self.velocity / GAME.FRAMERATE
            if dest_pos[0] > self.pos[0]:
                self.pos[0] += delta
                self.pos[0] = math.ceil(self.pos[0])
                if abs(dest_pos[0] - self.pos[0]) < delta:
                    self.pos[0] = dest_pos[0]
            elif dest_pos[0] < self.pos[0]:
                self.pos[0] -= delta
                self.pos[0] = math.floor(self.pos[0])
                if abs(dest_pos[0] - self.pos[0]) < delta:
                    self.pos[0] = dest_pos[0]
            elif dest_pos[1] > self.pos[1]:
                self.pos[1] += delta
                self.pos[1] = math.ceil(self.pos[1])
                if abs(dest_pos[1] - self.pos[1]) < delta:
                    self.pos[1] = dest_pos[1]
            elif dest_pos[1] < self.pos[1]:
                self.pos[1] -= delta
                self.pos[1] = math.floor(self.pos[1])
                if abs(dest_pos[1] - self.pos[1]) < delta:
                    self.pos[1] = dest_pos[1]        
        if self.path_index < len(self.path) - 1:
            if self.pos == dest_pos:
                self.path_index += 1

    def receive_damage(self, damage):
        '''
        Removes health from enemy equals to damage.
        '''
        self.health -= damage
          
class Card(Enemy):
    def __init__(self, game, CARD):
        super().__init__(game)
        self.sprites = CARD.SPRITES
        self.health = CARD.HEALTH
        self.velocity = CARD.VELOCITY
        self.size = CARD.SIZE
        self.CARD = CARD
