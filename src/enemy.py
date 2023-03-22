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
        self.path = []
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