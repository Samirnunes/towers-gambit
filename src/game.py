import pygame
from entity import *
from enemy import *
from ally import *
from map import *
from constants import *

class Game:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.allies = []
        self.enemies = []
        self.lives = 5
        self.money = 200
        self.background = None

    def set_background(self, map):
        '''
        Sets game's background based on a map.
        '''
        self.background = map.get_background(self.width, self.height)

    def run(self):
        '''
        Runs the game loop.
        '''
        running = True
        clock = pygame.time.Clock()
        
        map = Map(MapShapes.SHAPE1)
        self.set_background(map)
        self.create_enemy_card(map, 25, 25, Suits.CLUBS, Numbers.J)
        self.create_ally_piece(100, 50, 25, 25, Pieces.BISHOP, Color.WHITE)
        
        while running:
            clock.tick(FRAMERATE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw()
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
        
    def draw(self):
        '''
        Draws game's background.
        '''
        self.window.blit(self.background, (0, 0))
        pygame.display.update()
        
    def create_enemy_card(self, map, width, height, suit, number):
        '''
        Creates an enemy card (only for test, must be substituted).
        '''
        new_enemy = Card(width, height, suit, number)
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
