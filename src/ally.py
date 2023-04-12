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

    WHITE = 'W'
    BLACK = 'B'

class Ally(Entity):
    
    def __init__(self, game, size, pos):
        super().__init__(game, size)
        self.pos = pos
        self.cost = None
        self.spawn_count = None

    def update(self):
        super().update()

class Chess(Ally):

    def __init__(self, game, size, pos, piece, color):
        super().__init__(game, size, pos)
        self.piece = piece
        self.color = color
        self.determine_image_based_on_piece_and_color()
        self.determine_bullet_based_on_piece()
        self.spawn_count = self.bullet_shoot_rate
        self.determine_cost_based_on_piece()

    def update(self):
        super().update()
        self.shoot()

    def shoot(self):
        if self.spawn_count == self.bullet_shoot_rate:
            Bullet(self.game, self, self.bullet_size, self.pos, self.bullet_velocity, 
                   self.bullet_direction, self.bullet_damage, self.bullet_penetration_power)
            self.spawn_count = 0
        self.spawn_count = self.spawn_count + 1

    def determine_image_based_on_piece_and_color(self):
        '''
        Determines chess image based on piece and color atributes.
        '''
        png_str = self.color.value + '_' + self.piece.value + '.png'
        self.animation_count = 0
        self.images = [pygame.image.load(os.path.join('assets', 'pixel_chess', '16x32_pieces', png_str))]

    def determine_bullet_based_on_piece(self):

        self.bullet_shoot_rate = PIECES_CONSTANTS[self.piece.value]['bullet_shoot_rate']
        self.bullet_size = PIECES_CONSTANTS[self.piece.value]['bullet_size']
        self.bullet_velocity = PIECES_CONSTANTS[self.piece.value]['bullet_velocity']
        self.bullet_direction = PIECES_CONSTANTS[self.piece.value]['bullet_direction']
        self.bullet_damage = PIECES_CONSTANTS[self.piece.value]['bullet_damage']
        self.bullet_penetration_power = PIECES_CONSTANTS[self.piece.value]['bullet_penetration_power']
        
    def determine_cost_based_on_piece(self):
        self.cost = PIECES_CONSTANTS[self.piece.value]['cost']
