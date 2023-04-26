import pygame
import os
from ally import *
from interface import *
from constants import INTERFACE_ALLIES

class InterfaceAllies:
    def __init__(self, game):
        self.game = game

    def draw(self):
        index = 0
        for image in INTERFACE_ALLIES.IMAGES:
            image = pygame.transform.scale(image, INTERFACE_ALLIES.IMAGE_SIZE)
            self.game.window.blit(image, INTERFACE_ALLIES.IMAGE_POSITIONS[index])
            index += 1
        
        index = 0
        for text in INTERFACE_ALLIES.COST_TEXTS:
            label_font = pygame.font.SysFont(INTERFACE_ALLIES.LABEL_FONT, INTERFACE_ALLIES.LABEL_FONT_SIZE)
            cost_label = label_font.render(text, 1, INTERFACE_ALLIES.LABEL_FONT_COLOR)
            self.game.window.blit(cost_label, INTERFACE_ALLIES.COST_TEXT_POSITIONS[index])
            index += 1

