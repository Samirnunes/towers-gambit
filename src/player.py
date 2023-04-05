import pygame
from constants import *

class Player:
    def __init__(self):
        self.lives = LIVES
        self.money = MONEY
        
    def add_money(self, money):
        self.money += money

    def display(self, window):
        pygame.font.init()
        font = pygame.font.SysFont(LABEL_FONT, 26)
        lives_label = font.render(f'Lives: {self.lives}', 1, LABEL_FONT_COLOR)
        money_label = font.render(f'Money: {self.money}', 1, LABEL_FONT_COLOR)
        window.blit(lives_label, LIVES_LABEL_POSITION)
        window.blit(money_label, MONEY_LABEL_POSITION)

    def damage(self):
        if self.lives > 0:
            self.lives -= 1
