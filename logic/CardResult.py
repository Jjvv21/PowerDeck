from enum import Enum

class CardResult(Enum):
    CREATED_MAIN = 0
    CREATED_VARIANT = 1
    NAME_LENGTH = -1
    VARIANT_NAME_LENGTH = -2
    DUPLICATE = -3
    NO_IMAGE = -4
    NO_RACE = -5
    NO_RARITY = -6
    INVALID_TURN_POWER = -7
    INVALID_BONUS_POWER = -8
    INVALID_STAT = -9