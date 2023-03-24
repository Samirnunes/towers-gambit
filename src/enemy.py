import os
import pygame
import math
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

class Enemy():
    
    def __init__(self, width, height):
        self.x = None
        self.y = None
        self.img = None
        self.suit = None
        self.width = width
        self.height = height
        self.health = None
        self.velocity = None
        self.path = None
        self.path_index = None
    
    def draw(self, window):
        '''
        Draws the enemy with the given images.
        '''
        img = self.img
        img = pygame.transform.scale(img, (self.width, self.height))
            
        window.blit(img, (self.x, self.y))
        pygame.display.update()

    def collide(self, other_x, other_y, other_width, other_height):
        '''
        Returns if position has hit enemy.
        '''
        rect1_left = self.x - self.width/2
        rect1_right = self.x + self.width/2
        rect1_top = self.y + self.height/2
        rect1_bottom = self.y - self.height/2
        
        rect2_left = other_x - other_width/2
        rect2_right = other_x + other_width/2
        rect2_top = other_y + other_height/2
        rect2_bottom = other_y - other_height/2
        
        if ((rect1_right > rect2_left) and
            (rect1_left < rect2_right) and
            (rect1_bottom < rect2_top) and
            (rect1_top > rect2_bottom)):
          return True
        
        return False
    
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
        if self.path_index < len(self.path) - 1:
            if (self.x, self.y) == self.path[self.path_index + 1]:
                self.path_index += 1
    
    def hit(self, damage):
        '''
        Returns if an enemy has died and for each call removes 1 HP.
        '''
        self.health -= damage
          
    def alive(self):
        return self.health > 0

class Card(Enemy):
    def __init__(self, width, height, suit, number):
            super().__init__(width, height)
            self.suit = suit
            self.health = Card.determine_health_based_on_number(number)
            self.velocity = Card.determine_velocity_based_on_suit(suit)
            self.img = Card.determine_image_based_on_suit_and_number(suit, number)

    @staticmethod
    def determine_health_based_on_number(number):
        health = 0
        if number == Numbers.A:
            health = 1
        elif number == Numbers.J:
            health = 11
        elif number == Numbers.Q:
            health = 12
        elif number == Numbers.K:
            health = 13
        else:
            health = int(number.value)
        return health
    
    @staticmethod
    def determine_velocity_based_on_suit(suit):
        velocity = 0
        if suit == Suits.SPADES:
            velocity = 10
        elif suit == Suits.CLUBS:
            velocity = 20
        elif suit == Suits.HEARTS:
            velocity = 30
        elif suit == Suits.DIAMONDS:
            velocity = 40
        return velocity
    
    @staticmethod
    def determine_image_based_on_suit_and_number(suit, number):
        png_str = ''
        if suit == Suits.SPADES:
            png_str = 'French-' + 'Spade' + '-' + number.value + '.png'
        elif suit == Suits.CLUBS:
            png_str = 'French-' + 'Clover' + '-' + number.value + '.png'
        elif suit == Suits.HEARTS:
            png_str = 'French-' + 'Heart' + '-' + number.value + '.png'
        elif suit == Suits.DIAMONDS:
            png_str = 'French-' + 'Diamond' + '-' + number.value + '.png'
        return pygame.image.load(os.path.join('game_assets', 'cards', 'PNG', 'French_cards', png_str)) 