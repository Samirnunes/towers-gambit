import os
import pygame
from enemy import Enemy

class Game:
    def __init__(self):
        self.width = 700
        self.height = 700
        self.window = pygame.display.set_mode((self.width, self.height))
        self.allies = []
        self.enemies = []
        self.lives = 5
        self.money = 200
        self.bg = pygame.image.load(os.path.join(os.path.join('game_assets', 'pixel_chess','boards', 'board_plain_04_modified.png')))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        # self.clicks = []
        
    def run(self):
        running = True
        clock = pygame.time.Clock()
        
        self.create_enemy()
        
        while running:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                # pos = pygame.mouse.get_pos()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # self.clicks.append(pos)
                    # print(self.clicks)
                    pass
            self.draw()
            self.enemies[0].draw(self.window)
        
        pygame.quit()
        
    def draw(self):
        self.window.blit(self.bg, (0, 0))
        # for p in self.clicks:
        #     pygame.draw.circle(self.window, (255, 0, 0), (p[0], p[1]), 5, 0)
        pygame.display.update()
        
    def create_enemy(self):
        self.enemies.append(Enemy(5 ,185, 25, 25))