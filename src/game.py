import pygame
from entity import *
from enemy import *
from ally import *
from map import *
from constants import *

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.map = Map('tileset.png', 'map.png')
        self.allies = []
        self.enemies = []
        self.lives = 5
        self.money = 200

    def run(self):
        '''
        Runs the game loop.
        '''
        running = True
        clock = pygame.time.Clock()
        
        self.map.draw(self.window)

        self.create_enemy_card(25, 25, Suits.CLUBS, Numbers.J, self.map)
        # self.create_ally_piece(100, 50, 25, 25, Pieces.BISHOP, Color.WHITE)
        self.enemies[0].draw(self.window)
        
        while running:
            clock.tick(FRAMERATE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for enemy in self.enemies:
                enemy.draw(self.window)
                enemy.move()
                enemy.correct_destination()

            for ally in self.allies:
                ally.draw(self.window)
                
            #add collisions here
            
            for enemy in self.enemies:
                if not enemy.alive():
                    enemy.kill(self)
                    self.enemies.remove(enemy)
                    
        pygame.quit()
        
    def create_enemy_card(self, width, height, suit, number, map):
        '''
        Creates an enemy card (only for test, must be substituted).
        '''
        new_enemy = Card(width, height, suit, number, map)
        new_enemy.set_on_map(map)
        self.enemies.append(new_enemy)

    def create_ally_piece(self, initial_x, initial_y, width, height, piece, color):
        '''
        Creates an ally piece (only for test, must be substituted).
        '''
        new_ally = Chess(width, height, piece, color)
        new_ally.set_initial_position(initial_x, initial_y)
        self.allies.append(new_ally)
        
    def add_money(self, mon):
        self.money += mon
