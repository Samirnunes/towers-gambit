import pygame
import os

# General Game Constants

FRAMERATE = 60
WIDTH = 768
HEIGHT = 768
TILE_WIDTH = 48
TILE_HEIGHT = 48
LIVES = 5
MONEY = 200

LABEL_FONT = "Times New Roman"
LABEL_FONT_SIZE = 26
LABEL_FONT_COLOR = (255, 228, 196)
LIVES_LABEL_POSITION = (600, 20)
MONEY_LABEL_POSITION = (600, 50)

BUY_BUTTON_FONT = 'Times New Roman'
BUY_BUTTON_FONT_SIZE = 26
BUY_BUTTON_FONT_COLOR = (255, 228, 196)
BUY_BUTTON_POSITION = (600, 80)
BUY_BUTTON_DIMENSIONS = (150, 50)
BUY_BUTTON_LIGHT_COLOR = (170, 170, 170)
BUY_BUTTON_DARK_COLOR = (100, 100, 100)

# Allies Pieces Configurations

PIECES_WIDTH = 25
PIECES_HEIGHT = 50

PAWN_CONSTANTS = {'cost': 100
                  , 'bullet_shoot_rate': 100
                  , 'bullet_size': (55, 55)
                  , 'bullet_velocity': 120
                  , 'bullet_direction': 0
                  , 'bullet_damage': 1
                  , 'bullet_penetration_power': 1
                  , 'bullet_images': [pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_1.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_2.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_3.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_4.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_5.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_6.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_7.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_8.png'))]}

BISHOP_CONSTANTS = {'cost': 100
                   , 'bullet_shoot_rate': 100
                   , 'bullet_size': (55, 55)
                   , 'bullet_velocity': 120
                   , 'bullet_direction': 0
                   , 'bullet_damage': 1
                   , 'bullet_penetration_power': 1
                   , 'bullet_images': [pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_1.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_2.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_3.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_4.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_5.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_6.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_7.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_8.png'))]}

ROOK_CONSTANTS = {'cost': 100
                  , 'bullet_shoot_rate': 100
                  , 'bullet_size': (55, 55)
                  , 'bullet_velocity': 120
                  , 'bullet_direction': 0
                  , 'bullet_damage': 10
                  , 'bullet_penetration_power': 1
                  , 'bullet_images': [pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_1.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_2.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_3.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_4.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_5.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_6.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_7.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_8.png'))]}

KNIGHT_CONSTANTS = {'cost': 100
                    , 'bullet_shoot_rate': 100
                    , 'bullet_size': (55, 55)
                    , 'bullet_velocity': 120
                    , 'bullet_direction': 0
                    , 'bullet_damage': 1
                    , 'bullet_penetration_power': 1
                    , 'bullet_images': [pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_1.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_2.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_3.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_4.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_5.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_6.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_7.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_8.png'))]}

QUEEN_CONSTANTS = {'cost': 100
                   , 'bullet_shoot_rate': 100
                   , 'bullet_size': (55, 55)
                   , 'bullet_velocity': 120
                   , 'bullet_direction': 0
                   , 'bullet_damage': 200
                   , 'bullet_penetration_power': 1
                   , 'bullet_images': [pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_1.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_2.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_3.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_4.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_5.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_6.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_7.png')),
                                      pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_8.png'))]}

PIECES_CONSTANTS = {'Pawn': PAWN_CONSTANTS,
                    'Bishop': BISHOP_CONSTANTS,
                    'Rook': ROOK_CONSTANTS,
                    'Knight': KNIGHT_CONSTANTS,
                    'Queen': QUEEN_CONSTANTS}

# Enemies Cards Configurations

CARDS_WIDTH = 25
CARDS_HEIGHT = 30

SPADES_CONSTANTS = {'velocity': 10}

CLUBS_CONSTANTS = {'velocity': 200}

HEARTS_CONSTANTS = {'velocity': 30}

DIAMONDS_CONSTANTS = {'velocity': 40}

SUITS_CONSTANTS = {'Spades': SPADES_CONSTANTS,
                   'Clubs': CLUBS_CONSTANTS,
                   'Hearts': HEARTS_CONSTANTS,
                   'Diamonds': DIAMONDS_CONSTANTS}


