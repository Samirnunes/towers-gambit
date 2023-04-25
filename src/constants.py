import pygame
import os
import numpy as np

class GAME:
    FRAMERATE = 60
    WIDTH = 768
    HEIGHT = 768
    TILE_WIDTH = 48
    TILE_HEIGHT = 48
    LIVES = 5
    MONEY = 200

    LABEL_FONT = "Scriptina"
    LABEL_FONT_SIZE = 30
    LABEL_FONT_COLOR = (144, 238, 144)
    LIVES_LABEL_POSITION = (600, 35)
    MONEY_LABEL_POSITION = (600, 65)

# Bullet constants

class BULLET:

    class BULLET:
        def __init__(self, SIZE, DAMAGE, PENETRATION, VELOCITY, SPRITES):
            self.SIZE = SIZE
            self.DAMAGE = DAMAGE
            self.PENETRATION = PENETRATION
            self.VELOCITY = VELOCITY
            self.SPRITES = SPRITES

    # Velocity is [Vx, Vy].
    DEFAULT = BULLET(np.array([20, 20]), 1, 1, np.array([120, 0]), [pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_1.png'))])

    BISHOP = BULLET(np.array([20, 20]), 1, 1, np.array([120, -120]), [pygame.image.load(os.path.join('assets', 'arrows', 'arrow1_1.png'))])

# Ally constants

class ALLY:

    class ALLY:
        def __init__(self, TYPE, SIZE, COST, SHOOT_TIME, HEALTH, BULLET, SPRITES):
            self.TYPE = TYPE
            self.SIZE = SIZE
            self.COST = COST
            self.SHOOT_TIME = SHOOT_TIME
            self.HEALTH = HEALTH
            self.BULLET = BULLET
            self.SPRITES = SPRITES

    class PIECE(ALLY):
        def __init__(self, TYPE, SIZE, COST, SHOOT_TIME, HEALTH, BULLET, SPRITES):
            super().__init__(TYPE, SIZE, COST, SHOOT_TIME, HEALTH, BULLET, SPRITES)

    B_BISHOP = PIECE('BISHOP', np.array([25, 50]), 100, 100, 1, BULLET.BISHOP, [pygame.image.load(os.path.join('assets', 'chess', 'b_bishop.png'))])
    B_KING   = PIECE('KING', np.array([25, 50]), 100, 100, 9999, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'b_king.png'))])
    B_KNIGHT = PIECE('KNIGHT', np.array([25, 50]), 100, 100, 1, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'b_knight.png'))])
    B_PAWN   = PIECE('PAWN', np.array([25, 50]), 100, 100, 1, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'b_pawn.png'))])
    B_QUEEN  = PIECE('QUEEN', np.array([25, 50]), 100, 100, 1, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'b_queen.png'))])
    B_ROOK   = PIECE('ROOK', np.array([25, 50]), 100, 100, 1, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'b_rook.png'))])
    W_BISHOP = PIECE('BISHOP', np.array([25, 50]), 100, 100, 1, BULLET.BISHOP, [pygame.image.load(os.path.join('assets', 'chess', 'w_bishop.png'))])
    W_KING   = PIECE('KING', np.array([25, 50]), 100, 100, 9999, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'w_king.png'))])
    W_KNIGHT = PIECE('KNIGHT', np.array([25, 50]), 100, 100, 1, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'w_knight.png'))])
    W_PAWN   = PIECE('PAWN', np.array([25, 50]), 100, 100, 1, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'w_pawn.png'))])
    W_QUEEN  = PIECE('QUEEN', np.array([25, 50]), 100, 100, 1, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'w_queen.png'))])
    W_ROOK   = PIECE('ROOK', np.array([25, 50]), 100, 100, 1, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'w_rook.png'))])

class ENEMY:

    class CARD:

        class CARD:
            def __init__(self, SIZE, HEALTH, VELOCITY, SPRITES):
                self.SIZE = SIZE
                self.HEALTH = HEALTH
                self.VELOCITY = VELOCITY
                self.SPRITES = SPRITES

        S_A     = CARD(np.array([25, 30]),  1,  10, [pygame.image.load(os.path.join('assets', 'cards', 's_a.png'))])
        S_TWO   = CARD(np.array([25, 30]),  2,  10, [pygame.image.load(os.path.join('assets', 'cards', 's_two.png'))])
        S_THREE = CARD(np.array([25, 30]),  3,  10, [pygame.image.load(os.path.join('assets', 'cards', 's_three.png'))])
        S_FOUR  = CARD(np.array([25, 30]),  4,  10, [pygame.image.load(os.path.join('assets', 'cards', 's_four.png'))])
        S_FIVE  = CARD(np.array([25, 30]),  5,  10, [pygame.image.load(os.path.join('assets', 'cards', 's_five.png'))])
        S_SIX   = CARD(np.array([25, 30]),  6,  10, [pygame.image.load(os.path.join('assets', 'cards', 's_six.png'))])
        S_SEVEN = CARD(np.array([25, 30]),  7,  10, [pygame.image.load(os.path.join('assets', 'cards', 's_seven.png'))])
        S_EIGHT = CARD(np.array([25, 30]),  8,  10, [pygame.image.load(os.path.join('assets', 'cards', 's_eight.png'))])
        S_NINE  = CARD(np.array([25, 30]),  9,  10, [pygame.image.load(os.path.join('assets', 'cards', 's_nine.png'))])
        S_TEN   = CARD(np.array([25, 30]), 10,  10, [pygame.image.load(os.path.join('assets', 'cards', 's_ten.png'))])
        S_J     = CARD(np.array([25, 30]), 11,  10, [pygame.image.load(os.path.join('assets', 'cards', 's_j.png'))])
        S_Q     = CARD(np.array([25, 30]), 12,  10, [pygame.image.load(os.path.join('assets', 'cards', 's_q.png'))])
        S_K     = CARD(np.array([25, 30]), 13,  10, [pygame.image.load(os.path.join('assets', 'cards', 's_k.png'))])
        C_A     = CARD(np.array([25, 30]),  1, 200, [pygame.image.load(os.path.join('assets', 'cards', 'c_a.png'))])
        C_TWO   = CARD(np.array([25, 30]),  2, 200, [pygame.image.load(os.path.join('assets', 'cards', 'c_two.png'))])
        C_THREE = CARD(np.array([25, 30]),  3, 200, [pygame.image.load(os.path.join('assets', 'cards', 'c_three.png'))])
        C_FOUR  = CARD(np.array([25, 30]),  4, 200, [pygame.image.load(os.path.join('assets', 'cards', 'c_four.png'))])
        C_FIVE  = CARD(np.array([25, 30]),  5, 200, [pygame.image.load(os.path.join('assets', 'cards', 'c_five.png'))])
        C_SIX   = CARD(np.array([25, 30]),  6, 200, [pygame.image.load(os.path.join('assets', 'cards', 'c_six.png'))])
        C_SEVEN = CARD(np.array([25, 30]),  7, 200, [pygame.image.load(os.path.join('assets', 'cards', 'c_seven.png'))])
        C_EIGHT = CARD(np.array([25, 30]),  8, 200, [pygame.image.load(os.path.join('assets', 'cards', 'c_eight.png'))])
        C_NINE  = CARD(np.array([25, 30]),  9, 200, [pygame.image.load(os.path.join('assets', 'cards', 'c_nine.png'))])
        C_TEN   = CARD(np.array([25, 30]), 10, 200, [pygame.image.load(os.path.join('assets', 'cards', 'c_ten.png'))])
        C_J     = CARD(np.array([25, 30]), 11, 200, [pygame.image.load(os.path.join('assets', 'cards', 'c_j.png'))])
        C_Q     = CARD(np.array([25, 30]), 12, 200, [pygame.image.load(os.path.join('assets', 'cards', 'c_q.png'))])
        C_K     = CARD(np.array([25, 30]), 13, 200, [pygame.image.load(os.path.join('assets', 'cards', 'c_k.png'))])
        H_A     = CARD(np.array([25, 30]),  1,  30, [pygame.image.load(os.path.join('assets', 'cards', 'h_a.png'))])
        H_TWO   = CARD(np.array([25, 30]),  2,  30, [pygame.image.load(os.path.join('assets', 'cards', 'h_two.png'))])
        H_THREE = CARD(np.array([25, 30]),  3,  30, [pygame.image.load(os.path.join('assets', 'cards', 'h_three.png'))])
        H_FOUR  = CARD(np.array([25, 30]),  4,  30, [pygame.image.load(os.path.join('assets', 'cards', 'h_four.png'))])
        H_FIVE  = CARD(np.array([25, 30]),  5,  30, [pygame.image.load(os.path.join('assets', 'cards', 'h_five.png'))])
        H_SIX   = CARD(np.array([25, 30]),  6,  30, [pygame.image.load(os.path.join('assets', 'cards', 'h_six.png'))])
        H_SEVEN = CARD(np.array([25, 30]),  7,  30, [pygame.image.load(os.path.join('assets', 'cards', 'h_seven.png'))])
        H_EIGHT = CARD(np.array([25, 30]),  8,  30, [pygame.image.load(os.path.join('assets', 'cards', 'h_eight.png'))])
        H_NINE  = CARD(np.array([25, 30]),  9,  30, [pygame.image.load(os.path.join('assets', 'cards', 'h_nine.png'))])
        H_TEN   = CARD(np.array([25, 30]), 10,  30, [pygame.image.load(os.path.join('assets', 'cards', 'h_ten.png'))])
        H_J     = CARD(np.array([25, 30]), 11,  30, [pygame.image.load(os.path.join('assets', 'cards', 'h_j.png'))])
        H_Q     = CARD(np.array([25, 30]), 12,  30, [pygame.image.load(os.path.join('assets', 'cards', 'h_q.png'))])
        H_K     = CARD(np.array([25, 30]), 13,  30, [pygame.image.load(os.path.join('assets', 'cards', 'h_k.png'))])
        D_A     = CARD(np.array([25, 30]),  1,  40, [pygame.image.load(os.path.join('assets', 'cards', 'd_a.png'))])
        D_TWO   = CARD(np.array([25, 30]),  2,  40, [pygame.image.load(os.path.join('assets', 'cards', 'd_two.png'))])
        D_THREE = CARD(np.array([25, 30]),  3,  40, [pygame.image.load(os.path.join('assets', 'cards', 'd_three.png'))])
        D_FOUR  = CARD(np.array([25, 30]),  4,  40, [pygame.image.load(os.path.join('assets', 'cards', 'd_four.png'))])
        D_FIVE  = CARD(np.array([25, 30]),  5,  40, [pygame.image.load(os.path.join('assets', 'cards', 'd_five.png'))])
        D_SIX   = CARD(np.array([25, 30]),  6,  40, [pygame.image.load(os.path.join('assets', 'cards', 'd_six.png'))])
        D_SEVEN = CARD(np.array([25, 30]),  7,  40, [pygame.image.load(os.path.join('assets', 'cards', 'd_seven.png'))])
        D_EIGHT = CARD(np.array([25, 30]),  8,  40, [pygame.image.load(os.path.join('assets', 'cards', 'd_eight.png'))])
        D_NINE  = CARD(np.array([25, 30]),  9,  40, [pygame.image.load(os.path.join('assets', 'cards', 'd_nine.png'))])
        D_TEN   = CARD(np.array([25, 30]), 10,  40, [pygame.image.load(os.path.join('assets', 'cards', 'd_ten.png'))])
        D_J     = CARD(np.array([25, 30]), 11,  40, [pygame.image.load(os.path.join('assets', 'cards', 'd_j.png'))])
        D_Q     = CARD(np.array([25, 30]), 12,  40, [pygame.image.load(os.path.join('assets', 'cards', 'd_q.png'))])
        D_K     = CARD(np.array([25, 30]), 13,  40, [pygame.image.load(os.path.join('assets', 'cards', 'd_k.png'))])

class BUTTON:

    class BUTTON:
        
        def __init__(self, SIZE, POS, HOVER_SPRITES, IDLE_SPRITES):
            self.SIZE = SIZE
            self.POS = POS
            self.HOVER_SPRITES = HOVER_SPRITES
            self.IDLE_SPRITES = IDLE_SPRITES

    class BUYPIECEBUTTON(BUTTON):

        def __init__(self, SIZE, POS, HOVER_SPRITES, IDLE_SPRITES, PIECE):
            super().__init__(SIZE, POS, HOVER_SPRITES, IDLE_SPRITES)
            self.PIECE = PIECE

    BUY_BISHOP = BUYPIECEBUTTON(np.array([80, 80]), np.array([GAME.WIDTH - 40, 120]), 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button_clicked.png'))], 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button.png'))],
                                ALLY.W_BISHOP)
    BUY_KING   = BUYPIECEBUTTON(np.array([80, 80]), np.array([GAME.WIDTH - 120, 120]), 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button_clicked.png'))], 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button.png'))],
                                ALLY.W_KING)
    BUY_KNIGHT = BUYPIECEBUTTON(np.array([80, 80]), np.array([GAME.WIDTH - 40, 200]), 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button_clicked.png'))], 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button.png'))],
                                ALLY.W_KNIGHT)
    BUY_PAWN   = BUYPIECEBUTTON(np.array([80, 80]), np.array([GAME.WIDTH - 120, 200]), 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button_clicked.png'))], 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button.png'))],
                                ALLY.W_PAWN)
    BUY_QUEEN  = BUYPIECEBUTTON(np.array([80, 80]), np.array([GAME.WIDTH - 40, 280]), 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button_clicked.png'))], 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button.png'))],
                                ALLY.W_QUEEN)
    BUY_ROOK =   BUYPIECEBUTTON(np.array([80, 80]), np.array([GAME.WIDTH - 120, 280]), 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button_clicked.png'))], 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button.png'))],
                                ALLY.W_ROOK)

class INTERFACE:

    BUTTONS = [BUTTON.BUY_BISHOP, 
               BUTTON.BUY_KING, 
               BUTTON.BUY_KNIGHT, 
               BUTTON.BUY_PAWN, 
               BUTTON.BUY_QUEEN, 
               BUTTON.BUY_ROOK]

# Map constants

class MAP:
    PATHS = {'map1': ((4, 564), (293, 566), (290, 747), (496, 749), (492, 500), (633, 496), (631, 340), (764, 338)),
             'map2': ((0,0)), 
             'map3': ((0,0))}
    
    WAVES = {'map1': ((ENEMY.CARD.C_A, ENEMY.CARD.C_A),
                     (ENEMY.CARD.H_TWO, ENEMY.CARD.C_K, ENEMY.CARD.C_FOUR)),
             'map2': (),
             'map3': ()}
    
    ENEMY_SPAWN_FREQ = {'map1': 100,
                        'map2': 100,
                        'map3': 100}