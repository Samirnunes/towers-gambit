from entity import *
from ally import *
import numpy as np
from constants import ALLY
from draggable_ally import *

class Button(Entity):
    def __init__(self, game, BUTTON):
        super().__init__(game)
        self.hover_sprites = BUTTON.HOVER_SPRITES
        self.idle_sprites = BUTTON.IDLE_SPRITES
        self.pos = BUTTON.POS
        self.size = BUTTON.SIZE
        self.sprites = BUTTON.IDLE_SPRITES

    def update(self):
        super().update()
        if self.hovered():
            self.sprites = self.hover_sprites
        else:
            self.sprites = self.idle_sprites

    def hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        return all(self.pos - self.size/2 < mouse_pos) and all(mouse_pos < self.pos + self.size/2)

    def clicked(self, mouse_pos):
        return all(self.pos - self.size/2 < mouse_pos) and all(mouse_pos < self.pos + self.size/2)

    def on_click(self):
        pass

class BuyPieceButton(Button):
    def __init__(self, game, BUYPIECEBUTTON):
        super().__init__(game, BUYPIECEBUTTON)
        self.piece = BUYPIECEBUTTON.PIECE

    def update(self):
        super().update()

    def on_click(self):
        super().on_click()
        if (not self.game.draggables.get_entities()):
            DraggablePiece(self.game, self.piece)
