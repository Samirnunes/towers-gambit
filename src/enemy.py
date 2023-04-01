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
    
    def __init__(self, width, height):
        super().__init__(width, height)
        self.health = None
        self.velocity = None
        self.path = None
        self.path_index = None
    
    def set_path(self, map):
        '''
        Sets enemy's path based on a map.
        '''
        self.path = map.get_path()

    def set_initial_position(self):
        '''
        Sets enemy's initial position based on its path.
        '''
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.path_index = 0

    def set_on_map(self, map):
        '''
        Determines enemy's path based on a map and sets it's initial position.
        '''
        self.set_path(map)
        self.set_initial_position()
        
    def move(self):
        '''
        Moves enemy in a iteration of the game loop.
        '''
        if self.path_index < len(self.path) - 1:
            dest_x = self.path[self.path_index + 1][0]
            dest_y = self.path[self.path_index + 1][1]
            delta = self.velocity * ITERATION_TIME
            if dest_x > self.x:
                self.x += delta
                self.x = math.ceil(self.x)
                if abs(dest_x - self.x) < delta:
                    self.x = dest_x
            elif dest_x < self.x:
                self.x -= delta
                self.x = math.floor(self.x)
                if abs(dest_x - self.x) < delta:
                    self.x = dest_x
            elif dest_y > self.y:
                self.y += delta
                self.y = math.ceil(self.y)
                if abs(dest_y - self.y) < delta:
                    self.y = dest_y
            elif dest_y < self.y:
                self.y -= delta
                self.y = math.floor(self.y)
                if abs(dest_y - self.y) < delta:
                    self.y = dest_y        

    def correct_destination(self):
        '''
        Corrects enemy's destination based on its position.
        '''
        if self.path_index < len(self.path) - 1:
            if (self.x, self.y) == self.path[self.path_index + 1]:
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
        return self.health > 0

class Card(Enemy):
    def __init__(self, width, height, suit, number):
            super().__init__(width, height)
            self.suit = suit
            self.number = number
            self.determine_health_based_on_number()
            self.determine_velocity_based_on_suit()
            self.determine_image_based_on_suit_and_number()

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
        self.imgs = [pygame.image.load(os.path.join('game_assets', 'cards', 'PNG', 'French_cards', png_str))]