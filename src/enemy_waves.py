from enemy import *
from entities import *
from constants import MAP
from constants import GAME, LABELS
import pygame

class Enemy_Waves:
    """Class for managing enemy waves

    Attributes:
    game (Game): The Game object for the game.
    wave_count (int): Current wave number.
    enemy_count (int): Number of enemies spawned in current wave.
    enemy_spawn_time_count (int): Timer for enemy spawn frequency.
    interwave_count (int): Timer for time between waves.
    waves (list): A list of lists containing the cards for each wave for a specific map.
    """
    def __init__(self, game, map):
        """Initializes Enemy_Waves object.

        Args:
        game (Game): The Game object for the game.
        map (Map): The Map object for the current map.
        """
        self.game = game
        self.wave_count = 0
        self.enemy_count = 0
        self.enemy_spawn_time_count = MAP.ENEMY_SPAWN_FREQ[map.map_key]
        self.interwave_count = 0
        self.waves = MAP.WAVES[map.map_key]

    def advance_wave(self):
        """
        Checks if the current wave has ended and advances to the next wave.
        """
        if self.wave_count < len(self.waves):
            if self.enemy_count >= len(self.waves[self.wave_count]):
                self.interwave_count += 1
                if self.interwave_count == GAME.INTERWAVE_COUNT:
                    self.interwave_count = 0
                    self.wave_count += 1
                    self.enemy_count = 0
                    
    def draw(self):
        """
        Draws the label for the time between waves.
        """
        if self.enemy_count >= len(self.waves[self.wave_count]):
            label_font = pygame.font.SysFont(LABELS.LABEL_FONT, LABELS.LABEL_FONT_SIZE)
            time = int((GAME.INTERWAVE_COUNT - self.interwave_count)/GAME.FRAMERATE)
            interwave_count_label = label_font.render(f'Next wave: {time} s'
                                                            , 1, LABELS.LABEL_FONT_COLOR)
            self.game.window.blit(interwave_count_label, LABELS.INTERWAVE_LABEL_POSITION)

    def initialize_enemy(self):
        """
        Initializes the next enemy spawn.
        """
        if self.wave_count < len(self.waves):
            if self.enemy_spawn_time_count >= 100 and len(self.waves[self.wave_count]) != 0:
                if self.enemy_count < len(self.waves[self.wave_count]):
                    Card(self.game, self.waves[self.wave_count][self.enemy_count])
                    self.enemy_spawn_time_count = 0
                    self.enemy_count += 1
            self.enemy_spawn_time_count += 1

    def update(self):
        """
        Updates the enemy spawn and wave advancement.
        """
        self.initialize_enemy()
        self.advance_wave()
