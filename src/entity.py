import pygame

class Entity:
    def __init__(self, game):
        self.game = game
        self.animation_clock = 0
        self.pos = None
        self.size = None
        self.sprite = None
        self.sprites = None

    def update(self):
        pass
    
    def draw(self):
        '''
        Draws the entity in the given Pygame's window.
        '''
        self.sprite = self.sprites[self.animation_clock]
        self.sprite = pygame.transform.scale(self.sprite, self.size)
        
        self.animation_clock += 1
        if self.animation_clock > len(self.sprites) - 1:
            self.animation_clock = 0

        self.game.window.blit(self.sprite, self.pos - self.size/2)

    def has_collided(self, other):
        '''
        Returns if position has hit the entity.
        '''
        bottom_left = self.pos - self.size/2
        top_right = self.pos + self.size/2

        other_bottom_left = other.pos - other.size/2
        other_top_right = other.pos + other.size/2
        
        return (all(top_right > other_bottom_left) and all(bottom_left < other_top_right))
