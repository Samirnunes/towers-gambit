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
        self.map = Map(self, 'tileset.png', 'map.png')
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
        

        Chess(self, (PIECES_WIDTH, PIECES_HEIGHT), (24, 480), Pieces.QUEEN, Color.WHITE)
        
        i = 100

        while running:
            clock.tick(FRAMERATE)
            self.window.fill((0, 0, 0))
            self.map.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.entities.update()

            self.entities.draw()

            if (i == 100):
                Card(self, (CARDS_WIDTH, CARDS_HEIGHT), Suits.CLUBS, Numbers.J)
                i = 0
            i += 1

            #add collisions here
            
            pygame.display.update()
                    
        pygame.quit()
