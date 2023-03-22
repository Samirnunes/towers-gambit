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
        self.path = [(5, 195), (151, 195), (150, 284), (64, 287), (62, 454), (149, 459), (151, 545), (110, 547), 
                     (107, 633), (442, 636), (440, 549), (315, 546), (309, 459), (527, 459), (531, 591), (614, 590), 
                     (611, 374), (652, 372), (653, 198), (613, 198), (608, 157), (523, 155), (523, 113), (348, 109), 
                     (347, 192), (391, 194), (395, 328)]
        self.img = None
    
    def draw(self, window):
        '''
        Draws the enemy with the given images.
        '''
        self.animation_count +=1
        self.img = self.imgs[self.animation_count]
        
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
            
        window.blit(self.img, (self.x, self.y))
        self.move()
        
    def collide(self, X, Y):
        '''
        Returns if position has hit enemy.
        '''
        
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True        
        return False
        
    def move(self):
        '''
        Moves enemy.
        '''
        
        pass
    
    def hit(self):
        '''
        Returns if an enemy has died and for each call removes 1 HP.
        '''
        self.health -= 1
        if self.health <= 0:
            return True