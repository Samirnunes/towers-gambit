from enemy import *
from entities import *
from constants import MAP
from constants import GAME, LABELS
import pygame

class Enemy_Waves:
    def __init__(self, game, map):
        self.game = game
        self.wave_count = 0
        self.enemy_count = 0
        self.enemy_spawn_time_count = MAP.ENEMY_SPAWN_FREQ[map.map_key]
        self.interwave_count = 0
        self.waves = MAP.WAVES[map.map_key]

    def advance_wave(self):
        if self.wave_count < len(self.waves):
            if self.enemy_count >= len(self.waves[self.wave_count]):
                self.interwave_count += 1
                if self.interwave_count == GAME.INTERWAVE_COUNT:
                    self.interwave_count = 0
                    self.wave_count += 1
                    self.enemy_count = 0
                    
    def draw(self):
        if self.enemy_count >= len(self.waves[self.wave_count]):
            label_font = pygame.font.SysFont(LABELS.LABEL_FONT, LABELS.LABEL_FONT_SIZE)
            time = int((GAME.INTERWAVE_COUNT - self.interwave_count)/GAME.FRAMERATE)
            interwave_count_label = label_font.render(f'Next wave: {time} s'
                                                            , 1, LABELS.LABEL_FONT_COLOR)
            self.game.window.blit(interwave_count_label, LABELS.INTERWAVE_LABEL_POSITION)

    def initialize_enemy(self):
        if self.wave_count < len(self.waves):
            if self.enemy_spawn_time_count >= 100 and len(self.waves[self.wave_count]) != 0:
                if self.enemy_count < len(self.waves[self.wave_count]):
                    Card(self.game, self.waves[self.wave_count][self.enemy_count])
                    self.enemy_spawn_time_count = 0
                    self.enemy_count += 1
            self.enemy_spawn_time_count += 1

    def update(self):
        self.initialize_enemy()
        self.advance_wave()
