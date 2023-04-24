from enemy import *
from entities import *

class Enemy_Wave:
    def __init__(self, game, MAP):
        self.game = game
        self.wave_count = 0
        self.enemy_count = 0
        self.enemy_spawn_time_count = MAP.ENEMY_SPAWN_FREQ
        self.waves = MAP.WAVES

    def advance_wave(self):
        if self.wave_count < len(self.waves):
            if self.enemy_count == len(self.waves[self.wave_count]):
                self.wave_count += 1
                self.enemy_count = 0

    def initialize_enemy(self):
        if self.wave_count < len(self.waves):
            if self.enemy_spawn_time_count == 100 and len(self.waves[self.wave_count]) != 0:
                Card(self.game, self.waves[self.wave_count][self.enemy_count])
                self.enemy_spawn_time_count = 0
                self.enemy_count += 1
            self.enemy_spawn_time_count += 1

    def update(self):
        self.initialize_enemy()
        self.advance_wave()
