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

