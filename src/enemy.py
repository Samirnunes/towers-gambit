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
            self.kill()
        self.find_and_react_after_collision()
        self.move()

    def find_and_react_after_collision(self): # This function is faster here in enemy! So, don't put it in ally.
        for ally in self.game.allies.get_entities():
            if self.has_collided(ally):
                if ally.type == 'PAWN':
                    self.receive_damage(1)
                if ally.type != 'KING': # King doesn't receive damage because the damage is inflicted on the player.
                    ally.receive_damage(1)
                break

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
        self.suit = CARD.SUIT
        self.prize = CARD.PRIZE
        self.CARD = CARD

    def receive_damage(self, damage):
        super().receive_damage(damage)
        self.transform()

    def __index_lookup(self, possible_transformations):
        index = 0
        for card in possible_transformations:
            if card.HEALTH == self.health:
                return index
            index += 1

    def transform(self):
        '''Changes card's image based on its health.'''

        possible_transformations = ENEMY.CARD.ALL_CARDS[self.suit]
        transform_index = self.__index_lookup(possible_transformations)
        current_pos = self.pos
        current_path_index = self.path_index
        current_prize = self.prize
        if not transform_index == None: # Não mudar essa condição, porque se transform_index = 0, retorna False!
            self.game.enemies.remove(self)
            self = Card(self.game, possible_transformations[transform_index])
            self.pos = current_pos
            self.path_index = current_path_index
            self.prize = current_prize
            
    def kill(self):
        '''
        Cleanup actions. 'alive' should be called before to check if the enmy is dead.
        '''
        self.health = 0
        if self.pos != list(self.path[-1]):
            self.game.player.add_money(self.prize)
        self.game.enemies.remove(self)
