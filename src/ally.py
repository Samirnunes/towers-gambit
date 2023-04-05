import os
import pygame
from entity import *
from bullet import *
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
    
    def __init__(self, game, size, pos):
        super().__init__(game, size)
        self.pos = pos
        self.spawn_count = 99
        self.bullet_size = (20, 20)
        self.bullet_velocity = 120
        self.bullet_direction = 0

    def update(self):
        super().update()
        self.shoot()

    def shoot(self):
        if self.spawn_count == 100:
            Bullet(self.game, self.bullet_size, self.pos, self.bullet_velocity, self.bullet_direction)
            self.spawn_count = 0
        self.spawn_count = self.spawn_count + 1

class Chess(Ally):

    def __init__(self, game, size, pos, piece, color):
        super().__init__(game, size, pos)
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

        

