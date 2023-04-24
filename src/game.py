import pygame
from entity import *
from entities import *
from enemy import *
from ally import *
from player import *
from enemy_wave import *
from map import *
from button import *
from constants import GAME, MAP

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((GAME.WIDTH, GAME.HEIGHT))
        self.map = Map(self, 'map1.png')
        self.enemies = Entities()
        self.allies = Entities()
        self.bullets = Entities()
        self.draggables = Entities()
        self.player = Player(self)
        self.wave = Enemy_Wave(self, MAP.MAP1)
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
        #mouse_pos_list = [] # TO GET PATH

        while running:
            clock.tick(GAME.FRAMERATE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    #mouse_pos_list.append(mouse_pos) # TO GET PATH
                    draggables = self.draggables.get_entities()
                    for draggable in draggables:
                        draggable.on_click()
                    buttons = self.player.interface.buttons.get_entities()
                    clicked_buttons = [button for button in buttons if button.clicked(mouse_pos)]
                    for button in clicked_buttons:
                        button.on_click()
            #print(mouse_pos_list) # TO GET PATH
            self.update()
            self.draw()
            pygame.display.update()

        pygame.quit()
