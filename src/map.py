import os
import pygame
from ally import *
from constants import GAME, MAP, ALLY

class Map:

    def __init__(self, game, map_key):
        self.game = game
        self.map_key = map_key
        self.path = MAP.PATHS[self.map_key]
        self.is_king_drawn = False

    def draw(self):
        background_image = pygame.image.load(os.path.join('assets', 'maps', self.map_key + '.png'))
        background_image = pygame.transform.scale(background_image, (GAME.WIDTH, GAME.HEIGHT))
        self.game.window.blit(background_image, (0, 0))

        if not self.is_king_drawn:
            Piece(self.game, self.path[-1], ALLY.W_KING)
            self.is_king_drawn = True

    def get_path(self):
        '''
        Returns map's path.
        Path is the place where an enemy can walk through.
        '''
        return self.path