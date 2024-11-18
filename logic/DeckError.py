from enum import Enum

class DeckError(Enum):
    NO_SPACE = -1
    USED_NAME = -2
    DUPLICATE_CARD = -3
    TOO_MANY_URS = -4
    TOO_MANY_MRS = -5
    TOO_MANY_RS = -6
    TOO_MANY_NS = -7
