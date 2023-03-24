import pygame
from entity import *
from enemy import *
from ally import *
from map import FirstMap
from constants import *

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
        
        map = FirstMap()
        self.set_background(map)
        self.create_enemy_card(map, 25, 25, Suits.CLUBS, Numbers.J)
        self.create_ally_piece(100, 50, 25, 25, Pieces.BISHOP, Color.WHITE)
        
        while running:
            clock.tick(1/ITERATION_TIME)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw()
            self.enemies[0].draw(self.window)
            self.enemies[0].move()
            self.enemies[0].correct_destination()

            self.allies[0].draw(self.window)
        
        pygame.quit()
        
    def draw(self):
        self.window.blit(self.background, (0, 0))
        pygame.display.update()
        
    def create_enemy_card(self, map, width, height, suit, number):
        new_enemy = Card(width, height, suit, number)
        new_enemy.set_on_map(map)
        self.enemies.append(new_enemy)

    def create_ally_piece(self, initial_x, initial_y, width, height, piece, color):
        new_ally = Chess(width, height, piece, color)
        new_ally.set_initial_position(initial_x, initial_y)
        self.allies.append(new_ally)