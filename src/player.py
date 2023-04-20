import pygame
import os
from general_game_constants import *
from ally import *

class Player:
    def __init__(self, game):
        self.lives = LIVES
        self.money = MONEY
        self.game = game
        
    def add_money(self, money):
        self.money += money

    def damage(self):
        if self.lives > 0:
            self.lives -= 1

    def buy_piece(self, piece, color, position):
        # Only for test, must develop this function to receive 'piece' as a parameter.
        Chess(self.game, (PIECES_WIDTH, PIECES_HEIGHT), position, piece, color)

    def update_allies(self):
        self.game.allies.update()
        self.game.allies.draw()

    def update_bullets(self):
        self.game.bullets.update()
        self.game.bullets.draw()

    def update_user_interface(self, mouse_pos):
        '''
        Displays the updated UI.
        '''
        pygame.font.init()
        self.display_player_labels()
        positions = [BUY_BUTTON_POSITION, 
                    (BUY_BUTTON_POSITION[0] + 80, BUY_BUTTON_POSITION[1]),
                    (BUY_BUTTON_POSITION[0], BUY_BUTTON_POSITION[1] + 80),
                    (BUY_BUTTON_POSITION[0] + 80, BUY_BUTTON_POSITION[1] + 80),
                    (BUY_BUTTON_POSITION[0], BUY_BUTTON_POSITION[1] + 160),
                    (BUY_BUTTON_POSITION[0] + 80, BUY_BUTTON_POSITION[1] + 160)]
        for position in positions:
            self.display_button(mouse_pos, position, BUY_BUTTON_DIMENSIONS)

    def display_player_labels(self):
        '''
        Displays the player's labels: lives and money.
        '''
        label_font = pygame.font.SysFont(LABEL_FONT, LABEL_FONT_SIZE)
        lives_label = label_font.render(f'Lives: {self.lives}', 1, LABEL_FONT_COLOR)
        money_label = label_font.render(f'Money: {self.money}', 1, LABEL_FONT_COLOR)
        image = pygame.image.load(os.path.join('assets', 'user_interface', 'user_labels.png'))
        image = pygame.transform.scale(image, (BUY_BUTTON_DIMENSIONS[0] + 120, BUY_BUTTON_DIMENSIONS[1] + 60))
        self.game.window.blit(image, (BUY_BUTTON_POSITION[0] - 20, BUY_BUTTON_POSITION[1] - 150))
        self.game.window.blit(lives_label, LIVES_LABEL_POSITION)
        self.game.window.blit(money_label, MONEY_LABEL_POSITION)

    def display_button(self, mouse_pos, button_position, button_dimensions):
        '''
        Displays a button of the user interface.
        '''
        x_inside_button = (button_position[0] <= mouse_pos[0] <= button_position[0] + button_dimensions[0])
        y_inside_button = (button_position[1] <= mouse_pos[1] <= button_position[1] + button_dimensions[1])
        mouse_inside_button = x_inside_button and y_inside_button
        image = None
        if mouse_inside_button:
            image = pygame.image.load(os.path.join('assets', 'user_interface', 'button_clicked.png'))
            image = pygame.transform.scale(image, button_dimensions)
        else:
            image = pygame.image.load(os.path.join('assets', 'user_interface', 'button.png'))
            image = pygame.transform.scale(image, button_dimensions)
        self.game.window.blit(image , button_position)