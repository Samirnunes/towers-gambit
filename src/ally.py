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
    
    def __init__(self, width, height):
        super().__init__(width, height)

    def set_initial_position(self, initial_x, initial_y):
        '''
        Sets ally's initial position.
        '''
        self.x = initial_x
        self.y = initial_y

class Chess(Ally):

    def __init__(self, width, height, piece, color):
        super().__init__(width, height)
        self.piece = piece
        self.color = color
        self.determine_image_based_on_piece_and_color()

    def determine_image_based_on_piece_and_color(self):
        png_str = ''
        color_str = ''
        if self.color == Color.WHITE:
            color_str = 'W'
        elif self.color == Color.BLACK:
            color_str = 'B'
        png_str = color_str + '_' + self.piece.value + '.png'

        self.animation_count = 0
        self.imgs = [pygame.image.load(os.path.join('game_assets', 'pixel_chess', '16x32_pieces', png_str))]

        

