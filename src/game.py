import pygame
from entity import *
from entities import *
from enemy import *
from ally import *
from player import *
from enemy_waves import *
from map import *
from button import *
from constants import GAME, MAP, BUTTON

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((GAME.WIDTH, GAME.HEIGHT))
        self.map = Map(self, 'map1')
        self.enemies = Entities()
        self.allies = Entities()
        self.bullets = Entities()
        self.draggables = Entities()
        self.player = Player(self)
        self.waves = Enemy_Waves(self, self.map)
        pygame.font.init()

    def update(self):
        self.enemies.update()
        self.allies.update()
        self.bullets.update()
        self.player.interface.update() # displays updated user interface
        self.draggables.update()
        self.waves.update() # updates enemies

    def draw(self):
        self.window.fill((0, 0, 0))
        self.map.draw()
        self.enemies.draw()
        self.allies.draw()
        self.bullets.draw()
        self.player.interface.draw() # displays updated user interface
        self.draggables.draw()
        self.waves.draw()
            
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
        
    def start_screen(self):
        '''
        Start screen with two buttons: "start game" and "instructions".
        '''
        start_button = Button(self, BUTTON.STARTGAME)
        instructions_button = Button(self, BUTTON.INSTRUCTIONS)
        credits_button = Button(self, BUTTON.CREDITS)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    if start_button.clicked(mouse_pos):
                        self.run()
                    if instructions_button.clicked(mouse_pos):
                        self.instructions()
                    if credits_button.clicked(mouse_pos):
                        self.credits()
            self.window.fill((255, 255, 255))
            title = pygame.image.load(os.path.join('assets', 'user_interface', 'title.png'))
            title = pygame.transform.scale(title, (title.get_width()/1.5, title.get_height()/1.5))
            self.window.blit(title, (GAME.WIDTH/2 - title.get_width()/2, 100))
            start_button.draw()
            instructions_button.draw()
            credits_button.draw()
            pygame.display.update()
            
        pygame.quit()      
            
    def instructions(self):
        '''
        Instructions screen.
        '''
        exit_button = Button(self, BUTTON.EXIT)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    if exit_button.clicked(mouse_pos):
                        self.start_screen()
            self.window.fill((255, 255, 255))
            exit_button.draw()
            title = pygame.image.load(os.path.join('assets', 'user_interface', 'instructions.png'))
            self.window.blit(title, (GAME.WIDTH/2 - title.get_width()/2, 100))
            pygame.display.update()
            
        pygame.quit()
        
    def credits(self):
        '''
        Credits screen.
        '''
        exit_button = Button(self, BUTTON.EXIT)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    if exit_button.clicked(mouse_pos):
                        self.start_screen()
            self.window.fill((255, 255, 255))
            exit_button.draw()
            title = pygame.image.load(os.path.join('assets', 'user_interface', 'credits.png'))
            self.window.blit(title, (GAME.WIDTH/2 - title.get_width()/2, 100))
            pygame.display.update()
            
        pygame.quit()