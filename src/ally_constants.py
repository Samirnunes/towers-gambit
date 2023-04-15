import pygame
import os

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