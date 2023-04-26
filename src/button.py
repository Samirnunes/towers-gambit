from entity import *
from ally import *
from constants import ALLY
from draggable_ally import *

class Button(Entity):
    def __init__(self, game, BUTTON):
        """Initialize a Button object.

        Args:
        - game: a Game object representing the current game
        - BUTTON: a Button object containing the BUTTON's properties
        """
        super().__init__(game)
        self.hover_sprites = BUTTON.HOVER_SPRITES
        self.idle_sprites = BUTTON.IDLE_SPRITES
        self.pos = BUTTON.POS
        self.size = BUTTON.SIZE
        self.sprites = BUTTON.IDLE_SPRITES

    def update(self):
        """Update the Button object"""
        super().update()
        if self.hovered():
            self.sprites = self.hover_sprites
        else:
            self.sprites = self.idle_sprites

    def hovered(self):
        """Check if the mouse is hovering over the Button object"""
        mouse_pos = pygame.mouse.get_pos()
        return all(self.pos - self.size/2 < mouse_pos) and all(mouse_pos < self.pos + self.size/2)

    def clicked(self, mouse_pos):
        """Check if the Button object is clicked"""
        return all(self.pos - self.size/2 < mouse_pos) and all(mouse_pos < self.pos + self.size/2)

    def on_click(self):
        """Perform action when the Button object is clicked"""
        pass


class BuyPieceButton(Button):
    def __init__(self, game, BUYPIECEBUTTON):
        """Initialize a BuyPieceButton object.

        Args:
        - game: a Game object representing the current game
        - BUYPIECEBUTTON: a BuyPieceButton object containing the BuyPieceButton's properties
        """
        super().__init__(game, BUYPIECEBUTTON)
        self.piece = BUYPIECEBUTTON.PIECE

    def update(self):
        """Update the BuyPieceButton object"""
        super().update()

    def on_click(self):
        """Perform action when the BuyPieceButton object is clicked"""
        super().on_click()
        if (not self.game.draggables.get_entities()):
            DraggablePiece(self.game, self.piece)
