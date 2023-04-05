import pygame
from constants import *

class Player:
    def __init__(self):
        self.lives = LIVES
        self.money = MONEY
        
    def add_money(self, money):
        self.money += money

    def display_user_interface(self, window, mouse_pos):
        pygame.font.init()

        # Player labels

        label_font = pygame.font.SysFont(LABEL_FONT, LABEL_FONT_SIZE)
        lives_label = label_font.render(f'Lives: {self.lives}', 1, LABEL_FONT_COLOR)
        money_label = label_font.render(f'Money: {self.money}', 1, LABEL_FONT_COLOR)
        window.blit(lives_label, LIVES_LABEL_POSITION)
        window.blit(money_label, MONEY_LABEL_POSITION)

        # Player buttons
        
        x_inside_button = (BUY_BUTTON_POSITION[0] <= mouse_pos[0] <= BUY_BUTTON_POSITION[0] + BUY_BUTTON_DIMENSIONS[0])
        y_inside_button = (BUY_BUTTON_POSITION[1] <= mouse_pos[1] <= BUY_BUTTON_POSITION[1] + BUY_BUTTON_DIMENSIONS[1])
        mouse_inside_button = x_inside_button and y_inside_button
        if mouse_inside_button:
            pygame.draw.rect(window, BUY_BUTTON_LIGHT_COLOR, list(BUY_BUTTON_POSITION) + list(BUY_BUTTON_DIMENSIONS))
        else:
            pygame.draw.rect(window, BUY_BUTTON_DARK_COLOR, list(BUY_BUTTON_POSITION) + list(BUY_BUTTON_DIMENSIONS))
        buy_font = pygame.font.SysFont(BUY_BUTTON_FONT, BUY_BUTTON_FONT_SIZE)
        buy_text = buy_font.render(f'Buy a Bishop', 1, BUY_BUTTON_FONT_COLOR)
        window.blit(buy_text, BUY_BUTTON_POSITION)

    def damage(self):
        if self.lives > 0:
            self.lives -= 1
