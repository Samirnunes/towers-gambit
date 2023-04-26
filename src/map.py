import os
import pygame
from ally import *
from constants import GAME, MAP, ALLY

class Map:

    def __init__(self, game, map_key):
        """
        Initializes a new instance of the Map class.

        Args:
        - game (Game): the current game instance.
        - map_key (str): the key that identifies the map to be loaded.
        """
        self.game = game
        self.map_key = map_key
        self.path = MAP.PATHS[self.map_key]
        self.is_king_drawn = False

    def draw(self):
        """
        Draws the map on the game window.
        """
        # Load and scale the background image
        background_image = pygame.image.load(os.path.join('assets', 'maps', self.map_key + '.png'))
        background_image = pygame.transform.scale(background_image, (GAME.WIDTH, GAME.HEIGHT))
        
        # Blit the background image onto the game window
        self.game.window.blit(background_image, (0, 0))

        # Add the king piece to the end of the map's path if it hasn't been added yet
        if not self.is_king_drawn:
            Piece(self.game, self.path[-1], ALLY.W_KING)
            self.is_king_drawn = True

    def get_path(self):
        """
        Returns the map's path.

        Returns:
        - path (list): a list of tuples representing the cells that an enemy can walk through.
        """
        return self.path