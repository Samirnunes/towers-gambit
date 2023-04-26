from entity import *
from bullet import *
import numpy as np
import copy

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
        self.bullet = copy.copy(PIECE.BULLET)
        self.cost = PIECE.COST
        self.sprites = PIECE.SPRITES
        self.pos = pos
        self.shoot_time = PIECE.SHOOT_TIME
        self.size = PIECE.SIZE
        self.health = PIECE.HEALTH

    def update(self):
        super().update()
        self.behavior()
        if self.health == 0:
            self.kill()

    def receive_damage(self, damage):
        self.health -= damage

    def kill(self):
        self.game.allies.remove(self)

    def behavior(self):
        if self.shoot_clock == self.shoot_time:
            self.shoot_clock = 0
            if self.type == 'BISHOP':
                for i in range(1, 4):
                    theta = np.pi/2
                    rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
                    self.bullet.VELOCITY = np.dot(rot, self.bullet.VELOCITY)
                    self.shoot()

            elif self.type == 'QUEEN':
                for i in range(1, 8):
                    theta = np.pi/4
                    rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
                    self.bullet.VELOCITY = np.dot(rot, self.bullet.VELOCITY)
                    self.shoot()

            elif self.type == 'ROOK':
                for i in range(1, 4):
                    theta = np.pi/2
                    rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
                    self.bullet.VELOCITY = np.dot(rot, self.bullet.VELOCITY)
                    self.shoot()

            elif self.type == 'KING':
                theta = np.pi/2
                rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
                self.bullet.VELOCITY = np.dot(rot, self.bullet.VELOCITY)

            elif self.type == 'KNIGHT':
                for i in range(1, 3):
                    theta = np.pi/4
                    rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
                    self.bullet.VELOCITY = np.dot(rot, self.bullet.VELOCITY)
                    self.shoot()

            elif self.type == 'PAWN':
                theta = np.pi/2
                rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
                self.bullet.VELOCITY = np.dot(rot, self.bullet.VELOCITY)
