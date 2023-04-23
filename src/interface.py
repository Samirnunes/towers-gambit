import pygame
import os
from button import *
from entities import *
from constants import GAME, INTERFACE

class Interface:
    def __init__(self, game):
        self.game = game
        self.buttons = Entities();
        for BUTTON in INTERFACE.BUTTONS:
            self.buttons.append(BuyPieceButton(game, BUTTON))

    def update(self):
        self.buttons.update()

    def draw(self):
        '''
        Displays the updated UI.
        '''
        self.buttons.draw()
        # self.display_player_labels()

    def display_player_labels(self):
        '''
        Displays the player's labels: lives and money.
        '''
        label_font = pygame.font.SysFont(GAME.LABEL_FONT, GAME.LABEL_FONT_SIZE)
        lives_label = label_font.render(f'Lives: {self.game.player.lives}', 1, GAME.LABEL_FONT_COLOR)
        money_label = label_font.render(f'Money: {self.game.player.money}', 1, GAME.LABEL_FONT_COLOR)
        image = pygame.image.load(os.path.join('assets', 'user_interface', 'user_labels.png'))
        image = pygame.transform.scale(image, (GAME.BUY_BUTTON_DIMENSIONS[0] + 120, GAME.BUY_BUTTON_DIMENSIONS[1] + 60))
        self.game.window.blit(image, (GAME.BUY_BUTTON_POSITION[0] - 20, GAME.BUY_BUTTON_POSITION[1] - 150))
        self.game.window.blit(lives_label, GAME.LIVES_LABEL_POSITION)
        self.game.window.blit(money_label, GAME.MONEY_LABEL_POSITION)
