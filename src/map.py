import os
import pygame
from enum import Enum

class MapBackgrounds(Enum):

    BACKGROUND1 = pygame.image.load(os.path.join(os.path.join('game_assets', 'pixel_chess','boards', 'board_plain_04_modified.png')))

class MapPaths(Enum):

    PATH1 = [(5, 185), 
            (150, 185), (150, 285), (65, 285), (65, 455), (150, 455), 
            (150, 545), (110, 545), (110, 635), (440, 635), (440, 550), 
            (315, 550), (315, 460), (530, 460), (530, 590), (615, 590), 
            (615, 375), (650, 375),  (650, 200), (610, 200), (610, 155), 
            (525, 155), (525, 110), (350, 110), (359, 195), (395, 195), 
            (395, 330)]

class Map:

    def __init__(self, background, path):
        self.background = background.value
        self.path = path.value

    def get_background(self, width, height):
        '''
        Scales based on width and height and returns the map's background.
        '''
        background = pygame.transform.scale(self.background, (width, height))
        return background

    def get_path(self):
        '''
        Returns map's path.
        Path is the place where an enemy can walk through.
        '''
        return self.path