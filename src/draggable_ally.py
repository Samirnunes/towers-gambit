import pygame
from entity import *
from ally import *
from constants import GAME

class DraggablePiece(Entity):
    def __init__(self, game, PIECE):
        super().__init__(game)
        self.game = game
        self.size = PIECE.SIZE
        self.sprites = PIECE.SPRITES
        self.piece = PIECE
        self.game.draggables.append(self)

    def update(self):
        self.pos = list(pygame.mouse.get_pos())
        self.pos[0] = GAME.TILE_DISCRETE_DIMENSION * (self.pos[0] // GAME.TILE_DISCRETE_DIMENSION)
        self.pos[1] = GAME.TILE_DISCRETE_DIMENSION * (self.pos[1] // GAME.TILE_DISCRETE_DIMENSION)

    def is_empty_pos(self):
        for ally in self.game.allies.get_entities():
            if self.pos == ally.pos:
                return False
        return True

    def on_click(self):
        if self.game.player.money >= self.piece.COST and self.is_empty_pos():
            Piece(self.game, self.pos, self.piece)
            self.game.player.decrease_money(self.piece.COST)
        self.game.draggables.remove(self)
