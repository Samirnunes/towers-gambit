from wave_constants import *

class EnemyWave:
    def __init__(self, game):
        self.game = game
        self.wave_count = 0
        self.enemies = []
        self.determine_enemies_based_on_wave_count()

    def determine_enemies_traits_based_on_wave_count(self):
        if self.wave_count == 0:
            enemies_traits = [] # Não podemos usar um arquivo de constantes aqui para guardar as waves
                         # Pois quando chamamos Enemy ele já inicializa um inimigo na lista de Game.
                         # O certo é criar alguma interface que transforme inputs de Constants em Enemy.
        elif self.wave_count == 1:
            enemies_traits = []

        self.initialize_enemies(enemies_traits)
        pass

    def pass_wave(self):
        self.wave_count += 1

    def initialize_enemies(self, enemies_traits):
        for traits in enemies_traits:
            enemy = Enemy(self.game, traits[0], traits[1], traits[2]) # Enemy já dá append dele mesmo no jogo.
            self.enemies.append(enemy)