import os
import pygame
from constants import GAME, MAP

class Map:

    def __init__(self, game, map_filename):
        self.game = game
        self.tileset = None
        self.map = None
        self.path = MAP.MAP1.PATH
        self.map_filename = map_filename

    def draw(self):
        image = pygame.image.load(os.path.join('assets', 'maps', self.map_filename))
        image = pygame.transform.scale(image, (GAME.WIDTH, GAME.HEIGHT))
        self.game.window.blit(image, (0, 0))

    def get_path(self):
        '''
        Returns map's path.
        Path is the place where an enemy can walk through.
        '''
        return self.path
"""     def get_path(self):
        '''
        Returns map's path.
        Path is the place where an enemy can walk through.
        '''
        return self.path

    def draw(self):
        self.game.window.blit(self.background, (0, 0))

    def load_tileset(self, filename):
        image = pygame.image.load(filename)
        image_width, image_height = image.get_size()
        tileset = []
        for tileset_x in range(0, image_width // GAME.TILE_WIDTH):
            line = []
            tileset.append(line)
            for tileset_y in range(0, image_height // GAME.TILE_HEIGHT):
                rect = (tileset_x * GAME.TILE_WIDTH, tileset_y * GAME.TILE_HEIGHT, GAME.TILE_WIDTH, GAME.TILE_HEIGHT)
                line.append(image.subsurface(rect))
        self.tileset = tileset

    def load_map(self, filename):
        # Inner functions
        def check_special_case(pixel):
            '''
            Check if pixel fits any special tile case.
            '''
            r, g, b, a = pixel
            cases = ['', 'path', 'spawn', 'goal']
            return cases[b // 16]
        # Convert image pixel to tile index
        def pixel_to_tile_index(pixel):
            r, g, b, a = pixel
            return (r // 16, g // 16)
        
        def sort_path(path, spawn, goal):
            '''
            Sorts path from spawn to goal.
            '''
            new_path = []
            current = spawn
            while path:
                new_path.append(current)
                path.remove(current)
                if ((current[0] - GAME.TILE_WIDTH, current[1]) in path):
                    current = (current[0] - GAME.TILE_WIDTH, current[1])
                elif ((current[0] + GAME.TILE_WIDTH, current[1]) in path):
                    current = (current[0] + GAME.TILE_WIDTH, current[1])
                elif ((current[0], current[1] - GAME.TILE_HEIGHT) in path):
                    current = (current[0], current[1] - GAME.TILE_HEIGHT)
                elif ((current[0], current[1] + GAME.TILE_HEIGHT) in path):
                    current = (current[0], current[1] + GAME.TILE_HEIGHT)
            return new_path
        def map_point_to_point(map_point):
            '''
            Converts map point to point.
            '''
            return (GAME.TILE_WIDTH / 2 + GAME.TILE_WIDTH * map_point[0], GAME.TILE_WIDTH / 2 + GAME.TILE_WIDTH * map_point[1])
        # Outer function
        # Load map
        image = pygame.image.load(filename)
        image_width, image_height = image.get_size()
        map = []
        path = []
        for map_x in range(0, image_width):
            line = []
            map.append(line)
            for map_y in range(0, image_height):
                map_point = (map_x, map_y)
                pixel = image.get_at(map_point)
                special_case = check_special_case(pixel)
                if special_case == 'path':
                    path.append(map_point_to_point(map_point))
                elif special_case == 'spawn':
                    path.append(map_point_to_point(map_point))
                    spawn = map_point_to_point(map_point)
                elif special_case == 'goal':
                    path.append(map_point_to_point(map_point))
                    goal = map_point_to_point(map_point)
                line.append(pixel_to_tile_index(pixel))
        path = sort_path(path, spawn, goal)
        background = pygame.Surface((GAME.WIDTH, GAME.HEIGHT))
        map_width, map_height = len(map[0]), len(map)
        for map_x in range(0, map_width):
            for map_y in range(0, map_height):
                tileset_x, tileset_y = map[map_x][map_y]
                tile = self.tileset[tileset_x][tileset_y]
                background.blit(tile, (map_x * GAME.TILE_WIDTH, map_y * GAME.TILE_HEIGHT))
        self.background = background
        self.map = map
        self.path = path """
