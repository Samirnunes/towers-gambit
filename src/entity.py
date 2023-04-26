import pygame

class Entity:
    def __init__(self, game):
        '''
        Initializes a new instance of the Entity class.
        
        :param game: The game object
        '''
        self.game = game
        self.animation_clock = 0
        self.pos = None
        self.size = None
        self.sprite = None
        self.sprites = None

    def update(self):
        '''
        Updates the entity.
        '''
        pass
    
    def draw(self):
        '''
        Draws the entity in the given Pygame's window.
        '''
        # Set the sprite to the current animation frame
        self.sprite = self.sprites[self.animation_clock]
        
        # Scale the sprite to the correct size
        self.sprite = pygame.transform.scale(self.sprite, self.size)
        
        # Advance the animation frame
        self.animation_clock += 1
        if self.animation_clock > len(self.sprites) - 1:
            self.animation_clock = 0

        # Draw the sprite on the window
        self.game.window.blit(self.sprite, self.pos - self.size/2)

    def has_collided(self, other):
        '''
        Returns whether the entity collides with another entity.

        :param other: The entity to check collision against
        '''
        # Get the position of the corners of both entities
        bottom_left = self.pos - self.size/2
        top_right = self.pos + self.size/2

        other_bottom_left = other.pos - other.size/2
        other_top_right = other.pos + other.size/2
        
        # Check if the entities intersect in any direction
        return (all(top_right > other_bottom_left) and all(bottom_left < other_top_right))
