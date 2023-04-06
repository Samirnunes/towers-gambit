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
    ROOK = 'Rook'
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

    def update(self):
        super().update()

class Chess(Ally):

    def __init__(self, game, size, pos, piece, color):
        super().__init__(game, size, pos)
        self.piece = piece
        self.color = color
        self.determine_image_based_on_piece_and_color()
        self.determine_constants_based_on_piece()

    def update(self):
        super().update()
        self.shoot()

    def shoot(self):
        if self.spawn_count == 100:
            Bullet(self.game, self.bullet_size, self.pos, self.bullet_velocity, self.bullet_direction, self.bullet_damage, self.bullet_penetration_power)
            self.spawn_count = 0
        self.spawn_count = self.spawn_count + 1

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

    def determine_constants_based_on_piece(self):

        if self.piece == Pieces.PAWN:
            self.bullet_size = PAWN_CONSTANTS['bullet_size']
            self.bullet_velocity = PAWN_CONSTANTS['bullet_velocity']
            self.bullet_direction = PAWN_CONSTANTS['bullet_direction']
            self.bullet_damage = PAWN_CONSTANTS['bullet_damage']
            self.bullet_penetration_power = PAWN_CONSTANTS['bullet_penetration_power']

        elif self.piece == Pieces.BISHOP:
            self.bullet_size = BISHOP_CONSTANTS['bullet_size']
            self.bullet_velocity = BISHOP_CONSTANTS['bullet_velocity']
            self.bullet_direction = BISHOP_CONSTANTS['bullet_direction']
            self.bullet_damage = BISHOP_CONSTANTS['bullet_damage']
            self.bullet_penetration_power = BISHOP_CONSTANTS['bullet_penetration_power']

        elif self.piece == Pieces.ROOK:
            self.bullet_size = ROOK_CONSTANTS['bullet_size']
            self.bullet_velocity = ROOK_CONSTANTS['bullet_velocity']
            self.bullet_direction = ROOK_CONSTANTS['bullet_direction']
            self.bullet_damage = ROOK_CONSTANTS['bullet_damage']
            self.bullet_penetration_power = ROOK_CONSTANTS['bullet_penetration_power']
        
        elif self.piece == Pieces.KNIGHT:
            self.bullet_size = KNIGHT_CONSTANTS['bullet_size']
            self.bullet_velocity = KNIGHT_CONSTANTS['bullet_velocity']
            self.bullet_direction = KNIGHT_CONSTANTS['bullet_direction']
            self.bullet_damage = KNIGHT_CONSTANTS['bullet_damage']
            self.bullet_penetration_power = KNIGHT_CONSTANTS['bullet_penetration_power']

        elif self.piece == Pieces.QUEEN: 
            self.bullet_size = QUEEN_CONSTANTS['bullet_size']
            self.bullet_velocity = QUEEN_CONSTANTS['bullet_velocity']
            self.bullet_direction = QUEEN_CONSTANTS['bullet_direction']
            self.bullet_damage = QUEEN_CONSTANTS['bullet_damage']
            self.bullet_penetration_power = QUEEN_CONSTANTS['bullet_penetration_power']
        

