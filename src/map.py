import os
import pygame
from constants import GAME, MAP

class Map:

    def __init__(self, game, map_key):
        self.game = game
        self.map_key = map_key
        self.path = MAP.PATHS[self.map_key]

    def draw(self):
        image = pygame.image.load(os.path.join('assets', 'maps', self.map_key + '.png'))
        image = pygame.transform.scale(image, (GAME.WIDTH, GAME.HEIGHT))
        self.game.window.blit(image, (0, 0))

    def get_path(self):
        '''
        Returns map's path.
        Path is the place where an enemy can walk through.
        '''
        return self.path