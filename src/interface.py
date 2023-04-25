import pygame
import os
from button import *
from entities import *
from labels import *
from interface_allies import *
from constants import INTERFACE

class Interface:
    def __init__(self, game):
        self.game = game
        self.buttons = Entities();
        for BUTTON in INTERFACE.BUTTONS:
            self.buttons.append(BuyPieceButton(game, BUTTON))
        self.labels = Labels(game)
        self.interface_allies = InterfaceAllies(game)

    def update(self):
        self.buttons.update()

    def draw(self):
        '''
        Displays the updated UI.
        '''
        self.buttons.draw()
        self.labels.draw()
        self.interface_allies.draw()
