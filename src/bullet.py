from entity import Entity
from constants import GAME

class Bullet(Entity):
    
    def __init__(self, game, pos, BULLET):
        """
        Constructor for the Bullet class.
        
        Parameters:
        game (Game): The instance of the game currently running.
        pos (tuple): The (x, y) position where the bullet is spawned.
        BULLET (class): A dictionary containing the attributes of the bullet. The class
                       contains the following attributes: DAMAGE, PENETRATION, SIZE, SPRITES, and VELOCITY.
        """
        super().__init__(game)
        self.collided_enemies = []
        self.damage = BULLET.DAMAGE
        self.penetration = BULLET.PENETRATION
        self.pos = pos
        self.size = BULLET.SIZE
        self.sprites = BULLET.SPRITES
        self.velocity = BULLET.VELOCITY
        game.bullets.append(self)

    def update(self):
        """
        Updates the bullet in a single iteration of the game loop.
        """
        super().update()
        self.move()
        for enemy in self.game.enemies.get_entities():
            if self.has_collided(enemy) and enemy not in self.collided_enemies:
                enemy.receive_damage(self.damage)
                self.collided_enemies.append(enemy)
                if len(self.collided_enemies) == self.penetration:
                    self.game.bullets.remove(self)

        if not(0 <= self.pos[0] <= GAME.WIDTH) or not(0 <= self.pos[1] <= GAME.HEIGHT):
            del self

    def move(self):
        """
        Moves the bullet in a single iteration of the game loop.
        """
        self.pos = self.pos + self.velocity/GAME.FRAMERATE