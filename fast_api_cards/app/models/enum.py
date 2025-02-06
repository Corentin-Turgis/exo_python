from enum import Enum

class Shape(str, Enum):
    HEART = "heart"
    DIAMOND = "diamond"
    CLUB = "club"
    SPADE = "spade"

class Rank(str, Enum):
    A = "A"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    J = "J"
    Q = "Q"
    K = "K"
