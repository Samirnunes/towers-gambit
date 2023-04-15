import pygame
from entity import *
from entities import *
from enemy import *
from ally import *
from player import *
from map import *


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.map = Map(self, 'tileset.png', 'map.png')
        self.entities = Entities()
        self.enemies = Entities()
        self.allies = Entities()
        self.bullets = Entities()
        self.player = Player(self)

    def run(self):
        '''
        Runs the game loop.
        '''
        running = True
        clock = pygame.time.Clock()
        self.window.fill((0, 0, 0))
        
        Chess(self, (PIECES_WIDTH, PIECES_HEIGHT), (24, 480), Pieces.BISHOP, Color.WHITE)
        i = 100

        while running:
            clock.tick(FRAMERATE)
            mouse_pos = pygame.mouse.get_pos()
            self.window.fill((0, 0, 0))
            self.map.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.entities.update()
            self.entities.draw()
            self.player.display_user_interface(mouse_pos)

            if (i == 100):
                Card(self, (CARDS_WIDTH, CARDS_HEIGHT), Suits.CLUBS, Numbers.J)
                i = 0
            i += 1
            
            pygame.display.update()
                    
        pygame.quit()
