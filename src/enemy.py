import os
import pygame
import math
from constants import *

class Enemy():
    imgs = [pygame.image.load(os.path.join(os.path.join('game_assets', 'cards','PNG', 'French_cards', 'French-Clover-3.png')))]
    
    def __init__(self, width, height):
        self.x = None
        self.y = None
        self.width = width
        self.height = height
        self.animation_count = 0
        self.health = 2
        self.velocity = 300
        self.path = None
        self.path_index = None
    
    def draw(self, window):
        '''
        Draws the enemy with the given images.
        '''
        img = self.imgs[self.animation_count]
        img = pygame.transform.scale(img, (self.width, self.height))
        
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
            
        window.blit(img, (self.x, self.y))
        pygame.display.update()
        #self.animation_count += 1
        
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