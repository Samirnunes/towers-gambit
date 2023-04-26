import pygame
import os
from ally import *
from interface import *
from constants import GAME, ALLY

class Player:
    def __init__(self, game):
        """
        Initializes a Player instance.

        Args:
        - game: The game instance where the player is in.

        Attributes:
        - game: The game instance where the player is in.
        - lives: The number of lives the player has.
        - money: The amount of money the player has.
        - interface: The Interface instance that represents the player's interface.
        """
        self.game = game
        self.lives = GAME.LIVES
        self.money = GAME.MONEY
        self.interface = Interface(game)
        
    def add_money(self, money):
        """
        Adds money to the player's account.

        Args:
        - money: The amount of money to be added.
        """
        self.money += money

    def decrease_money(self, money):
        """
        Decreases money from the player's account.

        Args:
        - money: The amount of money to be decreased.
        """
        self.money -= money

    def receive_damage(self):
        """
        Decreases the player's life by one when the player is hit by an enemy.
        """
        if self.lives > 0:
            self.lives -= 1