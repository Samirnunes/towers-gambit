from enemy import *
from enemy_constants import *

# Example for wave 0

SPAWN_PERIOD = 1/100 # 1 enemy / 100 frames, may be changed
SPAWN_FREQ = 1/SPAWN_PERIOD

WAVE0 = [{'shape': (CARDS_WIDTH, CARDS_HEIGHT), 'suit': Suits.CLUBS, 'number': Numbers.J},
         {'shape': (CARDS_WIDTH, CARDS_HEIGHT), 'suit': Suits.CLUBS, 'number': Numbers.J}]

WAVE1 = []