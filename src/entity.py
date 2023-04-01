import pygame

class Entity:
    def __init__(self, width, height):
        self.x = None
        self.y = None
        self.imgs = None
        self.animation_count = None
        self.width = width
        self.height = height
    
    def draw(self, window):
        '''
        Draws the entity in the given Pygame's window.
        '''
        img = self.imgs[self.animation_count]
        img = pygame.transform.scale(img, (self.width, self.height))
        
        self.animation_count += 1
        if self.animation_count > len(self.imgs) - 1:
            self.animation_count = 0
        window.blit(img, (self.x, self.y))
        pygame.display.update()

    def collide(self, other_x, other_y, other_width, other_height):
        '''
        Returns if position has hit the entity.
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