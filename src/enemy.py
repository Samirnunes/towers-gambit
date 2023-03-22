import os
import pygame

class Enemy():
    imgs = [pygame.image.load(os.path.join(os.path.join('game_assets', 'cards','PNG', 'French_cards', 'French-Clover-3.png')))]
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.health = 2
        self.velocity = 1
        self.path = None
    
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
        self.animation_count += 1
        
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