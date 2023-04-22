import pygame
from entity import *
from entities import *
from enemy import *
from ally import *
from player import *
from wave import *
from map import *


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.map = Map(self, 'tileset.png', 'map.png')
        self.enemies = Entities()
        self.allies = Entities()
        self.bullets = Entities()
        self.player = Player(self)
        self.wave = Wave(self)

    def update(self):
        self.enemies.update()
        self.allies.update()
        self.bullets.update()
        self.wave.update() # updates enemies

    def draw(self):
        self.window.fill((0, 0, 0))
        self.map.draw()
        self.enemies.draw()
        self.allies.draw()
        self.bullets.draw()
        self.player.draw_user_interface() # displays updated user interface

    def run(self):
        '''
        Runs the game loop.
        '''
        running = True
        clock = pygame.time.Clock()
        self.player.buy_piece(Pieces.BISHOP, Color.WHITE, (24, 480)) # only for test

        while running:
            clock.tick(FRAMERATE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.update()
            self.draw()
            pygame.display.update()

        pygame.quit()
