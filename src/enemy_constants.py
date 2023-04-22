from enum import Enum
# Enemies Cards Configurations

class Suits(Enum):

    SPADES = 'Spades'
    CLUBS = 'Clubs'
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'

class Numbers(Enum):

    A = 'A'
    J = 'J'
    K = 'K'
    Q = 'Q'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'

CARDS_WIDTH = 25
CARDS_HEIGHT = 30

SPADES_CONSTANTS = {'velocity': 10}

CLUBS_CONSTANTS = {'velocity': 200}

HEARTS_CONSTANTS = {'velocity': 30}

DIAMONDS_CONSTANTS = {'velocity': 40}

SUITS_CONSTANTS = {'Spades': SPADES_CONSTANTS,
                   'Clubs': CLUBS_CONSTANTS,
                   'Hearts': HEARTS_CONSTANTS,
                   'Diamonds': DIAMONDS_CONSTANTS}


