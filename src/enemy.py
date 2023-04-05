import os
import pygame
import math
from entity import Entity
from constants import *
from enum import Enum

class Suits(Enum):

    SPADES = 0
    CLUBS = 1
    HEARTS = 2
    DIAMONDS = 3

class Numbers(Enum):

    A = 'A'
    J = 'J'
    K = 'K'
    Q = 'Q'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'

class Enemy(Entity):
    
    def __init__(self, game, size):
        super().__init__(game, size)
        self.health = None
        self.velocity = None
        self.path = game.map.get_path()
        self.path_index = 0
        self.pos = list(self.path[0])
        game.enemies.append(self)

    def update(self):
        super().update()
        self.move()
        if not self.alive():
            self.kill()
    
    def move(self):
        '''
        Moves enemy in a iteration of the game loop.
        '''
        if self.path_index < len(self.path) - 1:
            dest_pos = list(self.path[self.path_index + 1])
            delta = self.velocity / FRAMERATE
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

    def damage(self, damage):
        '''
        Removes health from enemy equals to damage.
        '''
        self.health -= damage
          
    def alive(self):
        '''
        Returns if enemy's alive.
        '''
        return self.health > 0 and self.path_index != len(self.path) - 1
    
        
        

class Card(Enemy):
    def __init__(self, game, size, suit, number):
            super().__init__(game, size)
            self.suit = suit
            self.number = number
            self.determine_health_based_on_number()
            self.determine_velocity_based_on_suit()
            self.determine_image_based_on_suit_and_number()
            self.starting_health = self.health

    def determine_health_based_on_number(self):
        '''
        Determines card's health based on number atribute.
        '''
        if self.number == Numbers.A:
            self.health = 1
        elif self.number == Numbers.J:
            self.health = 11
        elif self.number == Numbers.Q:
            self.health = 12
        elif self.number == Numbers.K:
            self.health = 13
        else:
            self.health = int(self.number.value)
    
    def determine_velocity_based_on_suit(self):
        '''
        Determines card's velocity based on suit atribute.
        '''
        if self.suit == Suits.SPADES:
            self.velocity = 10
        elif self.suit == Suits.CLUBS:
            self.velocity = 20
        elif self.suit == Suits.HEARTS:
            self.velocity = 30
        elif self.suit == Suits.DIAMONDS:
            self.velocity = 40
    
    def determine_image_based_on_suit_and_number(self):
        '''
        Determine card's image based on suit and number atributes.
        '''
        png_str = ''
        if self.suit == Suits.SPADES:
            png_str = 'French-' + 'Spade' + '-' + self.number.value + '.png'
        elif self.suit == Suits.CLUBS:
            png_str = 'French-' + 'Clover' + '-' + self.number.value + '.png'
        elif self.suit == Suits.HEARTS:
            png_str = 'French-' + 'Heart' + '-' + self.number.value + '.png'
        elif self.suit == Suits.DIAMONDS:
            png_str = 'French-' + 'Diamond' + '-' + self.number.value + '.png'
        self.animation_count = 0
        self.images = [pygame.image.load(os.path.join('assets', 'cards', 'PNG', 'French_cards', png_str))]
        
    def kill(self):
        '''
        Cleanup actions. 'alive' should be called before to check if the enmy is dead.
        '''
        self.health = 0
        money = 5*self.starting_health + self.velocity #can be modified later to make it more playable
        self.game.player.add_money(money)
        self.game.enemies.remove(self)
        self.game.entities.remove(self)
