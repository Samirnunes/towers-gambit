from entity import *
from bullet import *
import numpy as np
import copy

class Ally(Entity):
    
    def __init__(self, game):
        """
        Initializes an Ally object.

        Args:
        - game: the Game object that this ally belongs to

        Returns:
        - None
        """
        super().__init__(game)
        self.bullet = None
        self.cost = None
        self.shoot_clock = 0
        self.shoot_time = None
        self.game.allies.append(self)

    def update(self):
        """
        Updates the Ally's position and shoot clock.

        Args:
        - None

        Returns:
        - None
        """
        super().update()
        self.shoot_clock = self.shoot_clock + 1
        if self.shoot_clock == self.shoot_time:
            self.shoot()

    def shoot(self):
        """
        Creates a new Bullet object and adds it to the game's bullets list.

        Args:
        - None

        Returns:
        - None
        """
        Bullet(self.game, self.pos, self.bullet)

class Piece(Ally):

    def __init__(self, game, pos, PIECE):
        """
        Initializes a Piece object.

        Args:
        - game: the Game object that this piece belongs to
        - pos: the position of the Piece object
        - PIECE: a PieceType object representing the type of the Piece object

        Returns:
        - None
        """
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
        """
        Updates the Piece's behavior and checks if it needs to be killed.

        Args:
        - None

        Returns:
        - None
        """
        super().update()
        self.behavior()
        if self.health == 0:
            self.kill()

    def receive_damage(self, damage):
        """
        Decrements the Piece's health by the given amount of damage.

        Args:
        - damage: the amount of damage to be dealt to the Piece

        Returns:
        - None
        """
        self.health -= damage

    def kill(self):
        """
        Removes the Piece from the game's allies list.

        Args:
        - None

        Returns:
        - None
        """
        self.game.allies.remove(self)

    def behavior(self):
        """
        Defines the Piece's behavior when it shoots based on its type.

        Args:
        - None

        Returns:
        - None
        """
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