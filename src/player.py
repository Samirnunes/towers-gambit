import pygame
import os
from ally import *
from interface import *
from constants import GAME, ALLY

class Player:
    def __init__(self, game):
        self.game = game
        self.lives = GAME.LIVES
        self.money = GAME.MONEY
        self.interface = Interface(game)
        
    def add_money(self, money):
        self.money += money

    def receive_damage(self):
        if self.lives > 0:
            self.lives -= 1
