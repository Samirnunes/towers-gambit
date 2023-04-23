import pygame
from entity import *
from ally import *

class DraggablePiece(Entity):
    def __init__(self, game, PIECE):
        super().__init__(game)
        self.game = game
        self.size = PIECE.SIZE
        self.sprites = PIECE.SPRITES
        self.piece = PIECE
        self.game.draggables.append(self)

    def update(self):
        self.pos = pygame.mouse.get_pos()

    def on_click(self):
        Piece(self.game, self.pos, self.piece)
        self.game.draggables.remove(self)
