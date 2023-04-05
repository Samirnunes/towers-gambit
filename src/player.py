from constants import *

class Player:
    def __init__(self):
        self.lives = LIVES
        self.money = MONEY
        
    def add_money(self, money):
        self.money += money
