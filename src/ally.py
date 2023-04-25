from entity import *
from bullet import *
from constants import ALLY
import numpy as np

class Ally(Entity):
    
    def __init__(self, game):
        super().__init__(game)
        self.bullet = None
        self.cost = None
        self.shoot_clock = 0
        self.shoot_time = None
        self.game.allies.append(self)

    def update(self):
        super().update()
        self.shoot_clock = self.shoot_clock + 1
        if self.shoot_clock == self.shoot_time:
            self.shoot()

    def shoot(self):
        Bullet(self.game, self.pos, self.bullet)

class Piece(Ally):

    def __init__(self, game, pos, PIECE):
        super().__init__(game)
        self.type = PIECE.TYPE
        self.bullet = PIECE.BULLET
        self.cost = PIECE.COST
        self.sprites = PIECE.SPRITES
        self.pos = pos
        self.shoot_time = PIECE.SHOOT_TIME
        self.size = PIECE.SIZE

    def update(self):
        super().update()
        self.bullet_behavior()

    def bullet_behavior(self):
        if self.shoot_clock == self.shoot_time:
            self.shoot_clock = 0
            if self.type == 'BISHOP':
                theta = np.pi/2
                rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
                self.bullet.VELOCITY = np.dot(rot, self.bullet.VELOCITY)

            #else if self.type == 'KING':

            #else if self.type == 'KNIGHT':

            #else if self.type == 'PAWN':

            #else if self.type == 'QUEEN':

            #else if self.type == 'ROOK':
