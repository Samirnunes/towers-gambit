import pygame
from entity import *
from enemy import *
from ally import *
from player import *
from map import *
from constants import *

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.map = Map('tileset.png', 'map.png')
        self.entities = Entities()
        self.enemies = Enemies()
        self.allies = Allies()
        self.bullets = Bullets()
        self.player = Player()

    def run(self):
        '''
        Runs the game loop.
        '''
        running = True
        clock = pygame.time.Clock()
        self.window.fill((0, 0, 0))
        

        Card(self, (25, 25), Suits.CLUBS, Numbers.J)
        Chess(self, (25, 25), (24, 480), Pieces.BISHOP, Color.WHITE)
        

        while running:
            clock.tick(FRAMERATE)
            self.window.fill((0, 0, 0))
            self.map.draw(self)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.entities.update()

            self.entities.draw(self)

            #add collisions here
            
            for enemy in self.enemies.get_enemies():
                if not enemy.alive():
                    enemy.kill(self)
                    self.enemies.remove(enemy)

            pygame.display.update()
                    
        pygame.quit()
        
    def add_money(self, mon):
        self.money += mon
