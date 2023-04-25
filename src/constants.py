import pygame
import os
import numpy as np

class GAME:
    FRAMERATE = 60
    WIDTH = 768
    HEIGHT = 768
    TILE_WIDTH = 48
    TILE_HEIGHT = 48
    TILE_DISCRETE_DIMENSION = 48
    LIVES = 5
    MONEY = 3000

class LABELS:
    LABEL_BACKGROUND_POSITION = (5, 0)
    LABEL_BACKGROUND_SIZE = (150, 100)
    LABEL_FONT = "Scriptina"
    LABEL_FONT_SIZE = 28
    LABEL_FONT_COLOR = (144, 238, 144)
    LIVES_LABEL_POSITION = (25, 20)
    MONEY_LABEL_POSITION = (25, 50)

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
    DEFAULT = BULLET(np.array([20, 20]), 1, 1, np.array([120, 0]), [pygame.image.load(os.path.join('assets', 'fire_bullets', 'bullet1.png')),
                                                                    pygame.image.load(os.path.join('assets', 'fire_bullets', 'bullet2.png')),
                                                                    pygame.image.load(os.path.join('assets', 'fire_bullets', 'bullet3.png')),
                                                                    pygame.image.load(os.path.join('assets', 'fire_bullets', 'bullet4.png')),
                                                                    pygame.image.load(os.path.join('assets', 'fire_bullets', 'bullet5.png')),
                                                                    ])

    BISHOP = BULLET(np.array([20, 20]), 1, 1, np.array([120, -120]),[pygame.image.load(os.path.join('assets', 'fire_bullets', 'bullet1.png')),
                                                                    pygame.image.load(os.path.join('assets', 'fire_bullets', 'bullet2.png')),
                                                                    pygame.image.load(os.path.join('assets', 'fire_bullets', 'bullet3.png')),
                                                                    pygame.image.load(os.path.join('assets', 'fire_bullets', 'bullet4.png')),
                                                                    pygame.image.load(os.path.join('assets', 'fire_bullets', 'bullet5.png')),
                                                                    ])

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
            def __init__(self, SUIT, SIZE, HEALTH, VELOCITY, PRIZE, SPRITES):
                self.SUIT = SUIT
                self.SIZE = SIZE
                self.HEALTH = HEALTH
                self.VELOCITY = VELOCITY
                self.PRIZE = PRIZE
                self.SPRITES = SPRITES

        S_A     = CARD('S', np.array([25, 30]),  1,  10, 10, [pygame.image.load(os.path.join('assets', 'cards', 's_a.png'))])
        S_TWO   = CARD('S', np.array([25, 30]),  2,  10, 20, [pygame.image.load(os.path.join('assets', 'cards', 's_two.png'))])
        S_THREE = CARD('S', np.array([25, 30]),  3,  10, 30, [pygame.image.load(os.path.join('assets', 'cards', 's_three.png'))])
        S_FOUR  = CARD('S', np.array([25, 30]),  4,  10, 40, [pygame.image.load(os.path.join('assets', 'cards', 's_four.png'))])
        S_FIVE  = CARD('S', np.array([25, 30]),  5,  10, 50, [pygame.image.load(os.path.join('assets', 'cards', 's_five.png'))])
        S_SIX   = CARD('S', np.array([25, 30]),  6,  10, 60, [pygame.image.load(os.path.join('assets', 'cards', 's_six.png'))])
        S_SEVEN = CARD('S', np.array([25, 30]),  7,  10, 70, [pygame.image.load(os.path.join('assets', 'cards', 's_seven.png'))])
        S_EIGHT = CARD('S', np.array([25, 30]),  8,  10, 80, [pygame.image.load(os.path.join('assets', 'cards', 's_eight.png'))])
        S_NINE  = CARD('S', np.array([25, 30]),  9,  10, 90, [pygame.image.load(os.path.join('assets', 'cards', 's_nine.png'))])
        S_TEN   = CARD('S', np.array([25, 30]), 10,  10, 100, [pygame.image.load(os.path.join('assets', 'cards', 's_ten.png'))])
        S_J     = CARD('S', np.array([25, 30]), 11,  10, 110, [pygame.image.load(os.path.join('assets', 'cards', 's_j.png'))])
        S_Q     = CARD('S', np.array([25, 30]), 12,  10, 120, [pygame.image.load(os.path.join('assets', 'cards', 's_q.png'))])
        S_K     = CARD('S', np.array([25, 30]), 13,  10, 130, [pygame.image.load(os.path.join('assets', 'cards', 's_k.png'))])
        C_A     = CARD('C', np.array([25, 30]),  1, 200, 140, [pygame.image.load(os.path.join('assets', 'cards', 'c_a.png'))])
        C_TWO   = CARD('C', np.array([25, 30]),  2, 200, 150, [pygame.image.load(os.path.join('assets', 'cards', 'c_two.png'))])
        C_THREE = CARD('C', np.array([25, 30]),  3, 200, 160, [pygame.image.load(os.path.join('assets', 'cards', 'c_three.png'))])
        C_FOUR  = CARD('C', np.array([25, 30]),  4, 200, 170, [pygame.image.load(os.path.join('assets', 'cards', 'c_four.png'))])
        C_FIVE  = CARD('C', np.array([25, 30]),  5, 200, 180, [pygame.image.load(os.path.join('assets', 'cards', 'c_five.png'))])
        C_SIX   = CARD('C', np.array([25, 30]),  6, 200, 190, [pygame.image.load(os.path.join('assets', 'cards', 'c_six.png'))])
        C_SEVEN = CARD('C', np.array([25, 30]),  7, 200, 200, [pygame.image.load(os.path.join('assets', 'cards', 'c_seven.png'))])
        C_EIGHT = CARD('C', np.array([25, 30]),  8, 200, 210, [pygame.image.load(os.path.join('assets', 'cards', 'c_eight.png'))])
        C_NINE  = CARD('C', np.array([25, 30]),  9, 200, 220, [pygame.image.load(os.path.join('assets', 'cards', 'c_nine.png'))])
        C_TEN   = CARD('C', np.array([25, 30]), 10, 200, 230, [pygame.image.load(os.path.join('assets', 'cards', 'c_ten.png'))])
        C_J     = CARD('C', np.array([25, 30]), 11, 200, 240, [pygame.image.load(os.path.join('assets', 'cards', 'c_j.png'))])
        C_Q     = CARD('C', np.array([25, 30]), 12, 200, 250, [pygame.image.load(os.path.join('assets', 'cards', 'c_q.png'))])
        C_K     = CARD('C', np.array([25, 30]), 13, 200, 260, [pygame.image.load(os.path.join('assets', 'cards', 'c_k.png'))])
        H_A     = CARD('H', np.array([25, 30]),  1,  30, 270, [pygame.image.load(os.path.join('assets', 'cards', 'h_a.png'))])
        H_TWO   = CARD('H', np.array([25, 30]),  2,  30, 280, [pygame.image.load(os.path.join('assets', 'cards', 'h_two.png'))])
        H_THREE = CARD('H', np.array([25, 30]),  3,  30, 290, [pygame.image.load(os.path.join('assets', 'cards', 'h_three.png'))])
        H_FOUR  = CARD('H', np.array([25, 30]),  4,  30, 300, [pygame.image.load(os.path.join('assets', 'cards', 'h_four.png'))])
        H_FIVE  = CARD('H', np.array([25, 30]),  5,  30, 310, [pygame.image.load(os.path.join('assets', 'cards', 'h_five.png'))])
        H_SIX   = CARD('H', np.array([25, 30]),  6,  30, 320, [pygame.image.load(os.path.join('assets', 'cards', 'h_six.png'))])
        H_SEVEN = CARD('H', np.array([25, 30]),  7,  30, 330, [pygame.image.load(os.path.join('assets', 'cards', 'h_seven.png'))])
        H_EIGHT = CARD('H', np.array([25, 30]),  8,  30, 340, [pygame.image.load(os.path.join('assets', 'cards', 'h_eight.png'))])
        H_NINE  = CARD('H', np.array([25, 30]),  9,  30, 350, [pygame.image.load(os.path.join('assets', 'cards', 'h_nine.png'))])
        H_TEN   = CARD('H', np.array([25, 30]), 10,  30, 360, [pygame.image.load(os.path.join('assets', 'cards', 'h_ten.png'))])
        H_J     = CARD('H', np.array([25, 30]), 11,  30, 370, [pygame.image.load(os.path.join('assets', 'cards', 'h_j.png'))])
        H_Q     = CARD('H', np.array([25, 30]), 12,  30, 380, [pygame.image.load(os.path.join('assets', 'cards', 'h_q.png'))])
        H_K     = CARD('H', np.array([25, 30]), 13,  30, 390, [pygame.image.load(os.path.join('assets', 'cards', 'h_k.png'))])
        D_A     = CARD('D', np.array([25, 30]),  1,  40, 400, [pygame.image.load(os.path.join('assets', 'cards', 'd_a.png'))])
        D_TWO   = CARD('D', np.array([25, 30]),  2,  40, 410, [pygame.image.load(os.path.join('assets', 'cards', 'd_two.png'))])
        D_THREE = CARD('D', np.array([25, 30]),  3,  40, 420, [pygame.image.load(os.path.join('assets', 'cards', 'd_three.png'))])
        D_FOUR  = CARD('D', np.array([25, 30]),  4,  40, 430, [pygame.image.load(os.path.join('assets', 'cards', 'd_four.png'))])
        D_FIVE  = CARD('D', np.array([25, 30]),  5,  40, 440, [pygame.image.load(os.path.join('assets', 'cards', 'd_five.png'))])
        D_SIX   = CARD('D', np.array([25, 30]),  6,  40, 450, [pygame.image.load(os.path.join('assets', 'cards', 'd_six.png'))])
        D_SEVEN = CARD('D', np.array([25, 30]),  7,  40, 460, [pygame.image.load(os.path.join('assets', 'cards', 'd_seven.png'))])
        D_EIGHT = CARD('D', np.array([25, 30]),  8,  40, 470, [pygame.image.load(os.path.join('assets', 'cards', 'd_eight.png'))])
        D_NINE  = CARD('D', np.array([25, 30]),  9,  40, 480, [pygame.image.load(os.path.join('assets', 'cards', 'd_nine.png'))])
        D_TEN   = CARD('D', np.array([25, 30]), 10,  40, 490, [pygame.image.load(os.path.join('assets', 'cards', 'd_ten.png'))])
        D_J     = CARD('D', np.array([25, 30]), 11,  40, 500, [pygame.image.load(os.path.join('assets', 'cards', 'd_j.png'))])
        D_Q     = CARD('D', np.array([25, 30]), 12,  40, 510, [pygame.image.load(os.path.join('assets', 'cards', 'd_q.png'))])
        D_K     = CARD('D', np.array([25, 30]), 13,  40, 520, [pygame.image.load(os.path.join('assets', 'cards', 'd_k.png'))])

        S_CARDS = [S_A, S_TWO, S_THREE, S_FOUR, S_FIVE, S_SIX, S_SEVEN, S_EIGHT, S_NINE, S_TEN, S_J, S_Q, S_K]
        C_CARDS = [C_A, C_TWO, C_THREE, C_FOUR, C_FIVE, C_SIX, C_SEVEN, C_EIGHT, C_NINE, C_TEN, C_J, C_Q, C_K]
        H_CARDS = [H_A, H_TWO, H_THREE, H_FOUR, H_FIVE, H_SIX, H_SEVEN, H_EIGHT, H_NINE, H_TEN, H_J, H_Q, H_K]
        D_CARDS = [D_A, D_TWO, D_THREE, D_FOUR, D_FIVE, D_SIX, D_SEVEN, D_EIGHT, D_NINE, D_TEN, D_J, D_Q, D_K]

        ALL_CARDS = {'S': S_CARDS, 'C': C_CARDS, 'H': H_CARDS, 'D': D_CARDS}

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

    DEFAULT_SIZE = np.array([80, 80])

    BUY_BISHOP = BUYPIECEBUTTON(DEFAULT_SIZE, np.array([40, 140]), 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button_clicked.png'))], 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button.png'))],
                                ALLY.W_BISHOP)
    BUY_KING   = BUYPIECEBUTTON(DEFAULT_SIZE, np.array([120, 140]), 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button_clicked.png'))], 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button.png'))],
                                ALLY.W_KING)
    BUY_KNIGHT = BUYPIECEBUTTON(DEFAULT_SIZE, np.array([40, 220]), 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button_clicked.png'))], 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button.png'))],
                                ALLY.W_KNIGHT)
    BUY_PAWN   = BUYPIECEBUTTON(DEFAULT_SIZE, np.array([120, 220]), 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button_clicked.png'))], 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button.png'))],
                                ALLY.W_PAWN)
    BUY_QUEEN  = BUYPIECEBUTTON(DEFAULT_SIZE, np.array([40, 300]), 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button_clicked.png'))], 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button.png'))],
                                ALLY.W_QUEEN)
    BUY_ROOK =   BUYPIECEBUTTON(DEFAULT_SIZE, np.array([120, 300]), 
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
    
    # Mantenha tuplas de listas em waves para não dar erro no caso em que a wave só tiver 1 inimigo!
    # Pois quando tem tupla de tupla de 1 só elemento, Python interpreta como tupla de 1 elemento.
    WAVES = {'map1': ([ENEMY.CARD.S_TWO],
                     [ENEMY.CARD.S_TWO, ENEMY.CARD.S_TWO]), 
             'map2': (),
             'map3': ()}
    
    ENEMY_SPAWN_FREQ = {'map1': 100,
                        'map2': 100,
                        'map3': 100}