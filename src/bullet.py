from entity import Entity
from constants import GAME, BULLET

class Bullet(Entity):
    
    def __init__(self, game, pos, BULLET):
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
        super().update()
        self.move()
        for enemy in self.game.enemies.get_entities():
            if self.has_collided(enemy) and enemy not in self.collided_enemies:
                enemy.receive_damage(self.damage)
                self.collided_enemies.append(enemy)
                if len(self.collided_enemies) == self.penetration:
                    self.game.bullets.remove(self)

    def move(self):
        '''
        Moves bullet in a iteration of the game loop.
        '''
        self.pos = self.pos + self.velocity/GAME.FRAMERATE
