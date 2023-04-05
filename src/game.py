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
        self.enemies = Entities()
        self.allies = Entities()
        self.bullets = Entities()
        self.player = Player()

    def run(self):
        '''
        Runs the game loop.
        '''
        running = True
        clock = pygame.time.Clock()
        self.window.fill((0, 0, 0))
        

        Chess(self, (25, 50), (24, 480), Pieces.QUEEN, Color.WHITE)
        
        i = 100

        while running:
            clock.tick(FRAMERATE)
            self.window.fill((0, 0, 0))
            self.map.draw(self)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.entities.update()

            self.entities.draw(self)

            if (i == 100):
                Card(self, (25, 25), Suits.CLUBS, Numbers.J)
                i = 0
            i += 1

            #add collisions here
            
            for enemy in self.enemies.get_entities():
                if not enemy.alive():
                    enemy.kill(self)

            pygame.display.update()
                    
        pygame.quit()
