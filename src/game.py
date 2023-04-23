import pygame
from entity import *
from entities import *
from enemy import *
from ally import *
from player import *
from wave import *
from map import *
from button import *
from constants import GAME, ALLY
import numpy as np

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((GAME.WIDTH, GAME.HEIGHT))
        self.map = Map(self, 'tileset.png', 'map.png')
        self.enemies = Entities()
        self.allies = Entities()
        self.bullets = Entities()
        self.draggables = Entities()
        self.player = Player(self)
        self.wave = Wave(self)
        pygame.font.init()

    def update(self):
        self.enemies.update()
        self.allies.update()
        self.bullets.update()
        self.player.interface.update() # displays updated user interface
        self.draggables.update()
        self.wave.update() # updates enemies

    def draw(self):
        self.window.fill((0, 0, 0))
        self.map.draw()
        self.enemies.draw()
        self.allies.draw()
        self.bullets.draw()
        self.player.interface.draw() # displays updated user interface
        self.draggables.draw()

    def run(self):
        '''
        Runs the game loop.
        '''
        running = True
        clock = pygame.time.Clock()

        while running:
            clock.tick(GAME.FRAMERATE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    draggables = self.draggables.get_entities()
                    for draggable in draggables:
                        draggable.on_click()
                    buttons = self.player.interface.buttons.get_entities()
                    clicked_buttons = [button for button in buttons if button.clicked(mouse_pos)]
                    for button in clicked_buttons:
                        button.on_click()
            
            self.update()
            self.draw()
            pygame.display.update()

        pygame.quit()
