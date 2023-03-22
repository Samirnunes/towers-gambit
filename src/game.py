import pygame
from enemy import Enemy
from map import FirstMap

class Game():
    def __init__(self):
        self.width = 700
        self.height = 700
        self.window = pygame.display.set_mode((self.width, self.height))
        self.allies = []
        self.enemies = []
        self.lives = 5
        self.money = 200
        self.background = None

    def set_background(self, map):
        self.background = map.get_background(self.width, self.height)

    def run(self):
        running = True
        clock = pygame.time.Clock()
        
        self.set_background(FirstMap())
        self.create_enemy()
        
        while running:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw()
            self.enemies[0].draw(self.window)
        
        pygame.quit()
        
    def draw(self):
        self.window.blit(self.background, (0, 0))
        pygame.display.update()
        
    def create_enemy(self):
        self.enemies.append(Enemy(5 ,185, 25, 25))