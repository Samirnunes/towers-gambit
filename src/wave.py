from wave_constants import *
from entities import *

class Wave:
    def __init__(self, game):
        self.game = game
        self.wave_count = 0
        self.enemy_count = 0
        self.enemy_spawn_time_count = SPAWN_FREQ
        self.enemies_traits = []
        self.determine_enemies_traits_based_on_wave_count()

    def pass_wave(self):
        if self.enemy_count == len(self.enemies_traits):
            self.wave_count += 1
            self.enemy_count = 0
            self.determine_enemies_traits_based_on_wave_count()

    def initialize_enemy(self):
        if self.enemy_spawn_time_count == 100 and len(self.enemies_traits) != 0:
            # Enemy já dá append dele mesmo no game.
            Card(self.game, self.enemies_traits[self.enemy_count]['shape'], 
                self.enemies_traits[self.enemy_count - 1]['suit'], 
                self.enemies_traits[self.enemy_count - 1]['number'])
            self.enemy_spawn_time_count = 0
            self.enemy_count += 1
        self.enemy_spawn_time_count += 1

    def determine_enemies_traits_based_on_wave_count(self):
        if self.wave_count == 0:
            self.enemies_traits = WAVE0 # Não podemos usar um arquivo de constantes aqui para guardar as waves
                         # Pois quando chamamos Enemy ele já inicializa um inimigo na lista de Game.
                         # O certo é criar alguma interface que transforme inputs de Constants em Enemy.
        elif self.wave_count == 1:
            self.enemies_traits = WAVE1

    def update(self):
        self.initialize_enemy()
        self.pass_wave()
