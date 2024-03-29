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
    MONEY = 300
    INTERWAVE_COUNT = 600

class LABELS:
    LABEL_BACKGROUND_POSITION = (5, 0)
    LABEL_BACKGROUND_SIZE = (160, 110)
    LABEL_FONT = "Scriptina"
    LABEL_FONT_SIZE = 24
    LABEL_FONT_COLOR = (255, 255, 255)
    LIVES_LABEL_POSITION = (25, 30)
    MONEY_LABEL_POSITION = (25, 60)
    INTERWAVE_LABEL_POSITION = (625, 20)

# Bullet constants

class BULLET:

    class BULLET:
        def __init__(self, SIZE, DAMAGE, PENETRATION, VELOCITY, SPRITES):
            self.SIZE = SIZE
            self.DAMAGE = DAMAGE
            self.PENETRATION = PENETRATION
            self.VELOCITY = VELOCITY
            self.SPRITES = SPRITES
    
    BULLETASSET = [pygame.image.load(os.path.join('assets', 'fire_bullets', 'bullet1.png')),
                    pygame.image.load(os.path.join('assets', 'fire_bullets', 'bullet2.png')),
                    pygame.image.load(os.path.join('assets', 'fire_bullets', 'bullet3.png')),
                    pygame.image.load(os.path.join('assets', 'fire_bullets', 'bullet4.png')),
                    pygame.image.load(os.path.join('assets', 'fire_bullets', 'bullet5.png')),
                    ]

    # Velocity is [Vx, Vy].
    DEFAULT = BULLET(np.array([20, 20]), 1, 1, np.array([120, 0]), BULLETASSET)
    BISHOP = BULLET(np.array([20, 20]), 1, 1, np.array([120, -120]), BULLETASSET)

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

    B_BISHOP = PIECE('BISHOP', np.array([40, 40]), 200, 120, 1, BULLET.BISHOP, [pygame.image.load(os.path.join('assets', 'chess', 'b_bishop.png'))])
    B_KING   = PIECE('KING', np.array([40, 40]), 10000, 300, 9999, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'b_king.png'))])
    B_KNIGHT = PIECE('KNIGHT', np.array([40, 40]), 100, 120, 1, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'b_knight.png'))])
    B_PAWN   = PIECE('PAWN', np.array([40, 40]), 50, 60, 1, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'b_pawn.png'))])
    B_QUEEN  = PIECE('QUEEN', np.array([40, 40]), 500, 240, 1, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'b_queen.png'))])
    B_ROOK   = PIECE('ROOK', np.array([40, 40]), 200, 180, 1, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'b_rook.png'))])
    W_BISHOP = PIECE('BISHOP', np.array([40, 40]), 200, 120, 1, BULLET.BISHOP, [pygame.image.load(os.path.join('assets', 'chess', 'w_bishop.png'))])
    W_KING   = PIECE('KING', np.array([40, 40]), 10000, 120, 9999, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'w_king.png'))])
    W_KNIGHT = PIECE('KNIGHT', np.array([40, 40]), 100, 120, 1, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'w_knight.png'))])
    W_PAWN   = PIECE('PAWN', np.array([40, 40]), 50, 60, 1, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'w_pawn.png'))])
    W_QUEEN  = PIECE('QUEEN', np.array([40, 40]), 500, 240, 1, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'w_queen.png'))])
    W_ROOK   = PIECE('ROOK', np.array([40, 40]), 200, 180, 1, BULLET.DEFAULT, [pygame.image.load(os.path.join('assets', 'chess', 'w_rook.png'))])

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

        S_A     = CARD('S', np.array([25, 30]),  1,  20, 10, [pygame.image.load(os.path.join('assets', 'cards', 's_a.png'))])
        S_TWO   = CARD('S', np.array([25, 30]),  2,  20, 20, [pygame.image.load(os.path.join('assets', 'cards', 's_two.png'))])
        S_THREE = CARD('S', np.array([25, 30]),  3,  20, 30, [pygame.image.load(os.path.join('assets', 'cards', 's_three.png'))])
        S_FOUR  = CARD('S', np.array([25, 30]),  4,  20, 40, [pygame.image.load(os.path.join('assets', 'cards', 's_four.png'))])
        S_FIVE  = CARD('S', np.array([25, 30]),  5,  20, 50, [pygame.image.load(os.path.join('assets', 'cards', 's_five.png'))])
        S_SIX   = CARD('S', np.array([25, 30]),  6,  15, 60, [pygame.image.load(os.path.join('assets', 'cards', 's_six.png'))])
        S_SEVEN = CARD('S', np.array([25, 30]),  7,  15, 70, [pygame.image.load(os.path.join('assets', 'cards', 's_seven.png'))])
        S_EIGHT = CARD('S', np.array([25, 30]),  8,  15, 80, [pygame.image.load(os.path.join('assets', 'cards', 's_eight.png'))])
        S_NINE  = CARD('S', np.array([25, 30]),  9,  15, 90, [pygame.image.load(os.path.join('assets', 'cards', 's_nine.png'))])
        S_TEN   = CARD('S', np.array([25, 30]), 10,  10, 100, [pygame.image.load(os.path.join('assets', 'cards', 's_ten.png'))])
        S_J     = CARD('S', np.array([25, 30]), 11,  10, 110, [pygame.image.load(os.path.join('assets', 'cards', 's_j.png'))])
        S_Q     = CARD('S', np.array([25, 30]), 12,  10, 120, [pygame.image.load(os.path.join('assets', 'cards', 's_q.png'))])
        S_K     = CARD('S', np.array([25, 30]), 13,  10, 130, [pygame.image.load(os.path.join('assets', 'cards', 's_k.png'))])
        C_A     = CARD('C', np.array([25, 30]),  1, 70, 30, [pygame.image.load(os.path.join('assets', 'cards', 'c_a.png'))])
        C_TWO   = CARD('C', np.array([25, 30]),  2, 70, 40, [pygame.image.load(os.path.join('assets', 'cards', 'c_two.png'))])
        C_THREE = CARD('C', np.array([25, 30]),  3, 70, 50, [pygame.image.load(os.path.join('assets', 'cards', 'c_three.png'))])
        C_FOUR  = CARD('C', np.array([25, 30]),  4, 70, 60, [pygame.image.load(os.path.join('assets', 'cards', 'c_four.png'))])
        C_FIVE  = CARD('C', np.array([25, 30]),  5, 70, 70, [pygame.image.load(os.path.join('assets', 'cards', 'c_five.png'))])
        C_SIX   = CARD('C', np.array([25, 30]),  6, 60, 80, [pygame.image.load(os.path.join('assets', 'cards', 'c_six.png'))])
        C_SEVEN = CARD('C', np.array([25, 30]),  7, 60, 90, [pygame.image.load(os.path.join('assets', 'cards', 'c_seven.png'))])
        C_EIGHT = CARD('C', np.array([25, 30]),  8, 60, 100, [pygame.image.load(os.path.join('assets', 'cards', 'c_eight.png'))])
        C_NINE  = CARD('C', np.array([25, 30]),  9, 60, 110, [pygame.image.load(os.path.join('assets', 'cards', 'c_nine.png'))])
        C_TEN   = CARD('C', np.array([25, 30]), 10, 50, 120, [pygame.image.load(os.path.join('assets', 'cards', 'c_ten.png'))])
        C_J     = CARD('C', np.array([25, 30]), 11, 50, 130, [pygame.image.load(os.path.join('assets', 'cards', 'c_j.png'))])
        C_Q     = CARD('C', np.array([25, 30]), 12, 50, 140, [pygame.image.load(os.path.join('assets', 'cards', 'c_q.png'))])
        C_K     = CARD('C', np.array([25, 30]), 13, 50, 150, [pygame.image.load(os.path.join('assets', 'cards', 'c_k.png'))])
        H_A     = CARD('H', np.array([25, 30]),  1,  180, 50, [pygame.image.load(os.path.join('assets', 'cards', 'h_a.png'))])
        H_TWO   = CARD('H', np.array([25, 30]),  2,  180, 60, [pygame.image.load(os.path.join('assets', 'cards', 'h_two.png'))])
        H_THREE = CARD('H', np.array([25, 30]),  3,  180, 70, [pygame.image.load(os.path.join('assets', 'cards', 'h_three.png'))])
        H_FOUR  = CARD('H', np.array([25, 30]),  4,  150, 80, [pygame.image.load(os.path.join('assets', 'cards', 'h_four.png'))])
        H_FIVE  = CARD('H', np.array([25, 30]),  5,  150, 90, [pygame.image.load(os.path.join('assets', 'cards', 'h_five.png'))])
        H_SIX   = CARD('H', np.array([25, 30]),  6,  150, 100, [pygame.image.load(os.path.join('assets', 'cards', 'h_six.png'))])
        H_SEVEN = CARD('H', np.array([25, 30]),  7,  120, 110, [pygame.image.load(os.path.join('assets', 'cards', 'h_seven.png'))])
        H_EIGHT = CARD('H', np.array([25, 30]),  8,  120, 120, [pygame.image.load(os.path.join('assets', 'cards', 'h_eight.png'))])
        H_NINE  = CARD('H', np.array([25, 30]),  9,  120, 130, [pygame.image.load(os.path.join('assets', 'cards', 'h_nine.png'))])
        H_TEN   = CARD('H', np.array([25, 30]), 10,  100, 140, [pygame.image.load(os.path.join('assets', 'cards', 'h_ten.png'))])
        H_J     = CARD('H', np.array([25, 30]), 11,  100, 150, [pygame.image.load(os.path.join('assets', 'cards', 'h_j.png'))])
        H_Q     = CARD('H', np.array([25, 30]), 12,  100, 160, [pygame.image.load(os.path.join('assets', 'cards', 'h_q.png'))])
        H_K     = CARD('H', np.array([25, 30]), 13,  100, 170, [pygame.image.load(os.path.join('assets', 'cards', 'h_k.png'))])
        D_A     = CARD('D', np.array([25, 30]),  1,  350, 60, [pygame.image.load(os.path.join('assets', 'cards', 'd_a.png'))])
        D_TWO   = CARD('D', np.array([25, 30]),  2,  350, 70, [pygame.image.load(os.path.join('assets', 'cards', 'd_two.png'))])
        D_THREE = CARD('D', np.array([25, 30]),  3,  350, 80, [pygame.image.load(os.path.join('assets', 'cards', 'd_three.png'))])
        D_FOUR  = CARD('D', np.array([25, 30]),  4,  300, 90, [pygame.image.load(os.path.join('assets', 'cards', 'd_four.png'))])
        D_FIVE  = CARD('D', np.array([25, 30]),  5,  300, 100, [pygame.image.load(os.path.join('assets', 'cards', 'd_five.png'))])
        D_SIX   = CARD('D', np.array([25, 30]),  6,  300, 110, [pygame.image.load(os.path.join('assets', 'cards', 'd_six.png'))])
        D_SEVEN = CARD('D', np.array([25, 30]),  7,  250, 120, [pygame.image.load(os.path.join('assets', 'cards', 'd_seven.png'))])
        D_EIGHT = CARD('D', np.array([25, 30]),  8,  250, 130, [pygame.image.load(os.path.join('assets', 'cards', 'd_eight.png'))])
        D_NINE  = CARD('D', np.array([25, 30]),  9,  250, 140, [pygame.image.load(os.path.join('assets', 'cards', 'd_nine.png'))])
        D_TEN   = CARD('D', np.array([25, 30]), 10,  200, 150, [pygame.image.load(os.path.join('assets', 'cards', 'd_ten.png'))])
        D_J     = CARD('D', np.array([25, 30]), 11,  200, 160, [pygame.image.load(os.path.join('assets', 'cards', 'd_j.png'))])
        D_Q     = CARD('D', np.array([25, 30]), 12,  200, 170, [pygame.image.load(os.path.join('assets', 'cards', 'd_q.png'))])
        D_K     = CARD('D', np.array([25, 30]), 13,  200, 180, [pygame.image.load(os.path.join('assets', 'cards', 'd_k.png'))])

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

    BUY_BISHOP = BUYPIECEBUTTON(DEFAULT_SIZE, np.array([210, 40]), 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button_clicked.png'))], 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button.png'))],
                                ALLY.W_BISHOP)
    BUY_KNIGHT = BUYPIECEBUTTON(DEFAULT_SIZE, np.array([300, 40]), 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button_clicked.png'))], 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button.png'))],
                                ALLY.W_KNIGHT)
    BUY_PAWN   = BUYPIECEBUTTON(DEFAULT_SIZE, np.array([390, 40]), 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button_clicked.png'))], 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button.png'))],
                                ALLY.W_PAWN)
    BUY_QUEEN  = BUYPIECEBUTTON(DEFAULT_SIZE, np.array([480, 40]), 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button_clicked.png'))], 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button.png'))],
                                ALLY.W_QUEEN)
    BUY_ROOK =   BUYPIECEBUTTON(DEFAULT_SIZE, np.array([570, 40]), 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button_clicked.png'))], 
                               [pygame.image.load(os.path.join('assets', 'user_interface', 'button.png'))],
                                ALLY.W_ROOK)
    
    STARTGAME  = BUTTON(np.array([400, 100]), np.array([384, 350]),
                        [pygame.image.load(os.path.join('assets', 'user_interface', 'start_game_button.png'))],
                        [pygame.image.load(os.path.join('assets', 'user_interface', 'start_game_button.png'))])
    
    INSTRUCTIONS  = BUTTON(np.array([400, 100]), np.array([384, 500]),
                    [pygame.image.load(os.path.join('assets', 'user_interface', 'instructions_button.png'))],
                    [pygame.image.load(os.path.join('assets', 'user_interface', 'instructions_button.png'))])
    
    CREDITS  = BUTTON(np.array([400, 100]), np.array([384, 650]),
                    [pygame.image.load(os.path.join('assets', 'user_interface', 'credits_button.png'))],
                    [pygame.image.load(os.path.join('assets', 'user_interface', 'credits_button.png'))])
    
    EXIT = BUTTON(np.array([200, 50]), np.array([100, 50]),
                    [pygame.image.load(os.path.join('assets', 'user_interface', 'exit_button.png'))],
                    [pygame.image.load(os.path.join('assets', 'user_interface', 'exit_button.png'))])

class INTERFACE_ALLIES:
    EXTENSION = '.png'

    BISHOP = pygame.image.load(os.path.join('assets', 'chess', 'w_bishop' + EXTENSION))
    KNIGHT = pygame.image.load(os.path.join('assets', 'chess', 'w_knight' + EXTENSION))
    PAWN = pygame.image.load(os.path.join('assets', 'chess', 'w_pawn' + EXTENSION))
    QUEEN = pygame.image.load(os.path.join('assets', 'chess', 'w_queen' + EXTENSION))
    ROOK = pygame.image.load(os.path.join('assets', 'chess', 'w_rook' + EXTENSION))

    IMAGES = [BISHOP, KNIGHT, PAWN, QUEEN, ROOK]

    IMAGE_POSITIONS = (np.array([190, 15]),
                       np.array([280, 15]),
                       np.array([370, 18]),
                       np.array([460, 15]),
                       np.array([550, 15]))

    IMAGE_SIZE = (40, 40)
    
    BISHOP_TEXT = f'{ALLY.W_BISHOP.COST}'
    KNIGHT_TEXT = f'{ALLY.W_KNIGHT.COST}'
    PAWN_TEXT = f'{ALLY.W_PAWN.COST}'
    QUEEN_TEXT = f'{ALLY.W_QUEEN.COST}'
    ROOK_TEXT = f'{ALLY.W_ROOK.COST}'

    LABEL_FONT = "Scriptina"
    LABEL_FONT_SIZE = 20
    LABEL_FONT_COLOR = (255, 255, 255)

    COST_TEXTS = [BISHOP_TEXT, KNIGHT_TEXT, PAWN_TEXT, QUEEN_TEXT, ROOK_TEXT]

    COST_TEXT_POSITIONS = tuple((position + np.array([10, 40]) for position in IMAGE_POSITIONS))

class INTERFACE:

    BUTTONS = [BUTTON.BUY_BISHOP,  
               BUTTON.BUY_KNIGHT, 
               BUTTON.BUY_PAWN, 
               BUTTON.BUY_QUEEN, 
               BUTTON.BUY_ROOK]

# Map constants

class MAP:
    PATHS = {'map1': ((1, 310), (124, 314), (126, 599), (269, 598), (271, 360), (460, 357), (464, 215), (558, 216), (558, 122), (700, 125), (700, 306), (611, 310), (608, 500), (761, 508)),
             'map2': ((0,0)), 
             'map3': ((0,0))}
    
    # Mantenha tuplas de listas em waves para não dar erro no caso em que a wave só tiver 1 inimigo!
    # Pois quando tem tupla de tupla de 1 só elemento, Python interpreta como tupla de 1 elemento.
    WAVES = {'map1': ([ENEMY.CARD.S_A, ENEMY.CARD.S_A, ENEMY.CARD.S_TWO, ENEMY.CARD.S_TWO, ENEMY.CARD.S_THREE, ENEMY.CARD.C_A, ENEMY.CARD.C_TWO, ENEMY.CARD.C_FIVE],
                     [ENEMY.CARD.S_TWO, ENEMY.CARD.S_TWO, ENEMY.CARD.S_THREE, ENEMY.CARD.S_THREE, ENEMY.CARD.S_FOUR, ENEMY.CARD.S_FOUR, ENEMY.CARD.S_TEN],
                     [ENEMY.CARD.S_FOUR, ENEMY.CARD.S_FIVE, ENEMY.CARD.S_SIX, ENEMY.CARD.C_A, ENEMY.CARD.C_A, ENEMY.CARD.C_TWO, ENEMY.CARD.S_SEVEN, ENEMY.CARD.S_SEVEN, ENEMY.CARD.S_EIGHT, ENEMY.CARD.H_A, ENEMY.CARD.S_J],
                     [ENEMY.CARD.S_NINE, ENEMY.CARD.S_TEN, ENEMY.CARD.C_FOUR, ENEMY.CARD.C_FOUR, ENEMY.CARD.C_FIVE, ENEMY.CARD.C_SIX, ENEMY.CARD.C_SEVEN, ENEMY.CARD.C_EIGHT, ENEMY.CARD.H_A, ENEMY.CARD.H_TWO, ENEMY.CARD.H_THREE, ENEMY.CARD.H_FOUR, ENEMY.CARD.S_Q],
                     [ENEMY.CARD.H_TWO, ENEMY.CARD.D_THREE, ENEMY.CARD.D_FIVE, ENEMY.CARD.C_NINE, ENEMY.CARD.C_K, ENEMY.CARD.H_TEN, ENEMY.CARD.D_J, ENEMY.CARD.D_FOUR, ENEMY.CARD.D_SEVEN, ENEMY.CARD.H_NINE, ENEMY.CARD.D_NINE, ENEMY.CARD.D_TEN, ENEMY.CARD.D_J, ENEMY.CARD.D_Q, ENEMY.CARD.D_K]), 
             'map2': (),
             'map3': ()}
    
    ENEMY_SPAWN_FREQ = {'map1': 80,
                        'map2': 100,
                        'map3': 100}