import pygame
import os

class Enemy:
    imgs = []
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.animation_count = 0
        self.health = 2
        self.velocity = 1
        self.path = [(5, 195), (151, 195), (150, 284), (64, 287), (62, 454), (149, 459), (151, 545), (110, 547), 
                     (107, 633), (442, 636), (440, 549), (315, 546), (309, 459), (527, 459), (531, 591), (614, 590), 
                     (611, 374), (652, 372), (653, 198), (613, 198), (608, 157), (523, 155), (523, 113), (348, 109), 
                     (347, 192), (391, 194), (395, 328)]
    
    def draw(self, window):
        '''
        Draws the enemy with the given images.
        '''
        self.animation_count += 1
        img = self.imgs[self.animation_count]
        
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
            
        window.blit(img, (self.x, self.y))
        
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
        
    def move(self):
        '''
        Moves enemy.
        '''
        
        
    
    def hit(self, damage):
        '''
        Returns if an enemy has died and for each call removes 1 HP.
        '''
        self.health -= damage
          
    def alive(self):
        return self.health > 0