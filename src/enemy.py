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
            png_str = 'French-' + 'Spade' + '-' + number + '.png'
        elif suit == Suits.CLUBS:
            png_str = 'French-' + 'Clover' + '-' + number + '.png'
        elif suit == Suits.HEARTS:
            png_str = 'French-' + 'Heart' + '-' + number + '.png'
        elif suit == Suits.DIAMONDS:
            png_str = 'French-' + 'Diamond' + '-' + number + '.png'
        return pygame.image.load(os.path.join('game_assets', 'cards', 'PNG', 'French_cards', png_str)) 
        
    
class CardAce(Enemy):
    def __init__(self, width, height, suit):
        super().__init__(width, height)
        self.health = 1
        self.suit = suit
        self.velocity = Enemy.determine_velocity_based_on_suit(suit)
        self.img = Enemy.determine_image_based_on_suit_and_number(suit, 'A')

class CardTwo(Enemy):
    def __init__(self, width, height, suit):
        super().__init__(width, height)
        self.health = 2
        self.suit = suit
        self.velocity = Enemy.determine_velocity_based_on_suit(suit)
        self.img = Enemy.determine_image_based_on_suit_and_number(suit, str(self.health))

class CardThree(Enemy):
    def __init__(self, width, height, suit):
        super().__init__(width, height)
        self.health = 3
        self.suit = suit
        self.velocity = Enemy.determine_velocity_based_on_suit(suit)
        self.img = Enemy.determine_image_based_on_suit_and_number(suit, str(self.health))

class CardFour(Enemy):
    def __init__(self, width, height, suit):
        super().__init__(width, height)
        self.health = 4
        self.suit = suit
        self.velocity = Enemy.determine_velocity_based_on_suit(suit)
        self.img = Enemy.determine_image_based_on_suit_and_number(suit, str(self.health))

class CardFive(Enemy):
    def __init__(self, width, height, suit):
        super().__init__(width, height)
        self.health = 5
        self.suit = suit
        self.velocity = Enemy.determine_velocity_based_on_suit(suit)
        self.img = Enemy.determine_image_based_on_suit_and_number(suit, str(self.health))
class CardSix(Enemy):
    def __init__(self, width, height, suit):
        super().__init__(width, height)
        self.health = 6
        self.suit = suit
        self.velocity = Enemy.determine_velocity_based_on_suit(suit)
        self.img = Enemy.determine_image_based_on_suit_and_number(suit, str(self.health))

class CardSeven(Enemy):
    def __init__(self, width, height, suit):
        super().__init__(width, height)
        self.health = 7
        self.suit = suit
        self.velocity = Enemy.determine_velocity_based_on_suit(suit)
        self.img = Enemy.determine_image_based_on_suit_and_number(suit, str(self.health))

class CardEight(Enemy):
    def __init__(self, width, height, suit):
        super().__init__(width, height)
        self.health = 8
        self.suit = suit
        self.velocity = Enemy.determine_velocity_based_on_suit(suit)
        self.img = Enemy.determine_image_based_on_suit_and_number(suit, str(self.health))

class CardNine(Enemy):
    def __init__(self, width, height, suit):
        super().__init__(width, height)
        self.health = 9
        self.suit = suit
        self.velocity = Enemy.determine_velocity_based_on_suit(suit)
        self.img = Enemy.determine_image_based_on_suit_and_number(suit, str(self.health))

class CardTen(Enemy):
    def __init__(self, width, height, suit):
        super().__init__(width, height)
        self.health = 10
        self.suit = suit
        self.velocity = Enemy.determine_velocity_based_on_suit(suit)
        self.img = Enemy.determine_image_based_on_suit_and_number(suit, str(self.health))

