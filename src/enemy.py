import os
import math
from entity import Entity
from constants import GAME, ENEMY

class Enemy(Entity):
    """
    A class representing an enemy that moves along a pre-defined path.

    Attributes:
    - health (int): the health of the enemy.
    - velocity (float): the speed at which the enemy moves.
    - path (list of tuples): the path that the enemy follows.
    - path_index (int): the current index of the path that the enemy is at.
    - pos (list of floats): the position of the enemy.
    - game (Game): the game object.
    """
    
    def __init__(self, game):
        """
        Initializes an instance of the Enemy class.

        Args:
        - game (Game): the game object.
        """
        super().__init__(game)
        self.health = None
        self.velocity = None
        self.path = game.map.get_path()
        self.path_index = 0
        self.pos = list(self.path[0])
        self.game.enemies.append(self)
    
    def update(self):
        """
        Updates the state of the enemy. This includes checking for collision
        with allies, moving the enemy, and checking if the enemy has reached
        the end of the path or if its health has gone to zero.
        """
        super().update()
        if self.path_index == len(self.path) - 1:
            self.game.player.receive_damage()
            self.game.enemies.remove(self)
        if self.health <= 0:
            self.kill()
        self.find_and_react_after_collision()
        self.move()

    def find_and_react_after_collision(self): # This function is faster here in enemy! So, don't put it in ally.
        """
        Checks if the enemy has collided with an ally and reacts accordingly.
        This function should not be in the ally class because it is faster to
        execute it here.
        """
        for ally in self.game.allies.get_entities():
            if self.has_collided(ally):
                if ally.type == 'PAWN':
                    self.receive_damage(1)
                if ally.type != 'KING': # King doesn't receive damage because the damage is inflicted on the player.
                    ally.receive_damage(1)
                break

    def move(self):
        """
        Moves the enemy in a single iteration of the game loop.
        """
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
        Removes health from the enemy by the amount of damage.

        Parameters:
        damage (int): the amount of damage to remove
        '''
        self.health -= damage
          
class Card(Enemy):
    def __init__(self, game, CARD):
        '''
        Constructor for the Card class.

        Parameters:
        game (Game): the current Game instance
        CARD (class): a class containing information about the card type
        '''
        super().__init__(game)
        self.sprites = CARD.SPRITES
        self.health = CARD.HEALTH
        self.velocity = CARD.VELOCITY
        self.size = CARD.SIZE
        self.suit = CARD.SUIT
        self.prize = CARD.PRIZE
        self.CARD = CARD

    def receive_damage(self, damage):
        '''
        Reduces enemy health by the specified damage amount.

        Args:
        - damage (int): The amount of health to remove from the enemy.
        '''
        super().receive_damage(damage)
        self.transform()

    def __index_lookup(self, possible_transformations):
        '''
        Searches for the index of the first card in the provided list of possible transformations
        with the same health as this card.

        Args:
        - possible_transformations (list): A list of `Card` objects representing possible
        transformations of this card.

        Returns:
        - int: The index of the first card in `possible_transformations` with the same health as
        this card, or `None` if no such card exists.
        '''
        index = 0
        for card in possible_transformations:
            if card.HEALTH == self.health:
                return index
            index += 1

    def transform(self):
        '''
        Changes the card's image based on its remaining health. If there is a card with the same
        health in the same suit in `ENEMY.CARD.ALL_CARDS`, replaces the current card with that card.
        '''
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
        Cleans up after the enemy is killed. Updates the player's money if this card has not yet
        reached the end of the path, then removes the enemy from the game.
        '''
        self.health = 0
        if self.pos != list(self.path[-1]):
            self.game.player.add_money(self.prize)
        self.game.enemies.remove(self)
        del self
