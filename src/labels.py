import pygame
import os
from constants import LABELS

class Labels():
    def __init__(self, game):
        self.game = game

    def draw(self):
        '''
        Displays the player's labels: lives and money.
        '''
        label_font = pygame.font.SysFont(LABELS.LABEL_FONT, LABELS.LABEL_FONT_SIZE)
        lives_label = label_font.render(f'Lives: {self.game.player.lives}', 1, LABELS.LABEL_FONT_COLOR)
        money_label = label_font.render(f'Money: {self.game.player.money}', 1, LABELS.LABEL_FONT_COLOR)
        image = pygame.image.load(os.path.join('assets', 'user_interface', 'user_labels.png'))
        image = pygame.transform.scale(image, LABELS.LABEL_BACKGROUND_SIZE)
        self.game.window.blit(image, LABELS.LABEL_BACKGROUND_POSITION)
        self.game.window.blit(lives_label, LABELS.LIVES_LABEL_POSITION)
        self.game.window.blit(money_label, LABELS.MONEY_LABEL_POSITION)