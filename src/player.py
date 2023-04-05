import pygame
from constants import *

class Player:
    def __init__(self):
        self.lives = LIVES
        self.money = MONEY
        
    def add_money(self, money):
        self.money += money

    def display_user_interface(self, window, mouse_pos):
        '''
        Displays the UI.
        '''
        pygame.font.init()
        self.display_player_labels(window)
        self.display_button(window, mouse_pos, 'Buy Bishop',
                            BUY_BUTTON_FONT, BUY_BUTTON_FONT_COLOR, BUY_BUTTON_FONT_SIZE,
                            BUY_BUTTON_POSITION, BUY_BUTTON_DIMENSIONS,
                            BUY_BUTTON_LIGHT_COLOR, BUY_BUTTON_DARK_COLOR) # Only an example

    def display_player_labels(self, window):
        '''
        Displays the player's labels: lives and money.
        '''
        label_font = pygame.font.SysFont(LABEL_FONT, LABEL_FONT_SIZE)
        lives_label = label_font.render(f'Lives: {self.lives}', 1, LABEL_FONT_COLOR)
        money_label = label_font.render(f'Money: {self.money}', 1, LABEL_FONT_COLOR)
        window.blit(lives_label, LIVES_LABEL_POSITION)
        window.blit(money_label, MONEY_LABEL_POSITION)

    def display_button(self, window, mouse_pos, button_text, 
                       button_font, button_font_color, button_font_size,
                       button_position, button_dimensions, 
                       button_light_color, button_dark_color):
        '''
        Displays a button of the user interface.
        '''
        x_inside_button = (button_position[0] <= mouse_pos[0] <= button_position[0] + button_dimensions[0])
        y_inside_button = (button_position[1] <= mouse_pos[1] <= button_position[1] + button_dimensions[1])
        mouse_inside_button = x_inside_button and y_inside_button
        if mouse_inside_button:
            pygame.draw.rect(window, button_light_color, list(button_position) + list(button_dimensions))
        else:
            pygame.draw.rect(window, button_dark_color, list(button_position) + list(button_dimensions))
        font = pygame.font.SysFont(button_font,button_font_size)
        text = font.render(button_text, 1, button_font_color)
        window.blit(text, button_position)

    def damage(self):
        if self.lives > 0:
            self.lives -= 1
