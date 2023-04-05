import os
import pygame
from entity import Entity
from constants import *
from enum import Enum

class Pieces(Enum):
    
    PAWN = 'Pawn'
    BISHOP = 'Bishop'
    KNIGHT = 'Knight'
    TOWER = 'Tower'
    QUEEN = 'Queen'
    KING = 'King'

class Color(Enum):

    WHITE = 0
    BLACK = 1

class Ally(Entity):
    
    def __init__(self, game, width, height, point):
        super().__init__(game, width, height)
        self.x, self.y = point

class Chess(Ally):

    def __init__(self, game, width, height, point, piece, color):
        super().__init__(game, width, height, point)
        self.piece = piece
        self.color = color
        self.determine_image_based_on_piece_and_color()

    def determine_image_based_on_piece_and_color(self):
        '''
        Determines chess image based on piece and color atributes.
        '''
        png_str = ''
        color_str = ''
        if self.color == Color.WHITE:
            color_str = 'W'
        elif self.color == Color.BLACK:
            color_str = 'B'
        png_str = color_str + '_' + self.piece.value + '.png'

        self.animation_count = 0
        self.images = [pygame.image.load(os.path.join('assets', 'pixel_chess', '16x32_pieces', png_str))]

        

