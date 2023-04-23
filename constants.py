import pygame
import os
from enum import Enum

class BULLET:
    class DEFAULT:
        SHOOT_RATE = 100
        SIZE = (55, 55)
        VELOCITY = 120
        DIRECTION = 0
        DAMAGE = 1
        PENETRATION = 1
        IMAGES = [pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_1.png')),
                  pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_2.png')),
                  pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_3.png')),
                  pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_4.png')),
                  pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_5.png')),
                  pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_6.png')),
                  pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_7.png')),
                  pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_8.png'))]

class ALLY:

    class PIECE:
        WIDTH = 25
        HEIGHT = 50

        class B_BISHOP:
            COST = 100
            BULLET = BULLET.DEFAULT
            IMAGES = [pygame.image.load(os.path.join('assets', 'chess', 'b_bishop.png'))]

        class B_KING:
            COST = 100
            BULLET = BULLET.DEFAULT
            IMAGES = [pygame.image.load(os.path.join('assets', 'chess', 'b_king.png'))]

        class B_KNIGHT:
            COST = 100
            BULLET = BULLET.DEFAULT
            IMAGES = [pygame.image.load(os.path.join('assets', 'chess', 'b_knight.png'))]

        class B_PAWN:
            COST = 100
            BULLET = BULLET.DEFAULT
            IMAGES = [pygame.image.load(os.path.join('assets', 'chess', 'b_pawn.png'))]

        class B_QUEEN:
            COST = 100
            BULLET = BULLET.DEFAULT
            IMAGES = [pygame.image.load(os.path.join('assets', 'chess', 'b_queen.png'))]

        class B_ROOK:
            COST = 100
            BULLET = BULLET.DEFAULT
            IMAGES = [pygame.image.load(os.path.join('assets', 'chess', 'b_rook.png'))]
