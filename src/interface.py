import pygame
import os
from button import *
from entities import *
from labels import *
from interface_allies import *
from constants import INTERFACE

class Interface:
    def __init__(self, game):
        """
        Initializes the Interface class.

        Parameters:
            game: the game instance
        """
        self.game = game

        # Creates buttons for each type of piece the player can buy
        self.buttons = Entities();
        for BUTTON in INTERFACE.BUTTONS:
            self.buttons.append(BuyPieceButton(game, BUTTON))

        # Initializes the labels for displaying lives and money
        self.labels = Labels(game)

        # Initializes the interface for displaying the allied pieces
        self.interface_allies = InterfaceAllies(game)

    def update(self):
        """
        Updates the UI buttons
        """
        self.buttons.update()

    def draw(self):
        '''
        Displays the updated UI.
        '''
        self.buttons.draw()
        self.labels.draw()
        self.interface_allies.draw()
