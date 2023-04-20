import pygame
from entity import *
from entities import *
from enemy import *
from ally import *
from player import *
from enemy_wave import *
from map import *


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.map = Map(self, 'tileset.png', 'map.png')
        self.enemies = Entities()
        self.allies = Entities()
        self.bullets = Entities()
        self.player = Player(self)
        self.wave = EnemyWave(self)

    def game_update(self, mouse_pos):
        self.player.update_user_interface(mouse_pos) # displays updated user interface
        self.player.update_allies() # updates allies
        self.bullets.update() # updates bullets
        self.bullets.draw()
        self.wave.update() # updates enemies
        pygame.display.update()

    def run(self):
        '''
        Runs the game loop.
        '''
        running = True
        clock = pygame.time.Clock()
        self.window.fill((0, 0, 0))
        self.player.buy_piece(Pieces.BISHOP, Color.WHITE, (24, 480)) # only for test

        while running:
            clock.tick(FRAMERATE)
            mouse_pos = pygame.mouse.get_pos()
            self.window.fill((0, 0, 0))
            self.map.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.game_update(mouse_pos)

        pygame.quit()
