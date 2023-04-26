import pygame
import os
from constants import LABELS

class Labels():
    def __init__(self, game):
        """
        Initializes a Labels object.

        Args:
            game (Game): The Game object.
        """
        self.game = game

    def draw(self):
        '''
        Displays the player's labels: lives and money.
        '''
        label_font = pygame.font.SysFont(LABELS.LABEL_FONT, LABELS.LABEL_FONT_SIZE)

        # Renders lives and money labels
        lives_label = label_font.render(f'Lives: {self.game.player.lives}', 1, LABELS.LABEL_FONT_COLOR)
        money_label = label_font.render(f'Money: {self.game.player.money}', 1, LABELS.LABEL_FONT_COLOR)

        # Loads and scales the background image for the labels
        image = pygame.image.load(os.path.join('assets', 'user_interface', 'user_labels.png'))
        image = pygame.transform.scale(image, LABELS.LABEL_BACKGROUND_SIZE)

        # Displays the background image and the labels
        self.game.window.blit(image, LABELS.LABEL_BACKGROUND_POSITION)
        self.game.window.blit(lives_label, LABELS.LIVES_LABEL_POSITION)
        self.game.window.blit(money_label, LABELS.MONEY_LABEL_POSITION)