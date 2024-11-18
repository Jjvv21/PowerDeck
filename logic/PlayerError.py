from enum import Enum

class PlayerError(Enum):
    NAME_LENGTH = -1
    USERNAME_LENGTH = -2
    NO_MAIL = -3
    USERNAME_TAKEN = -4
    USED_MAIL = -5
    PASSWORD_LENGTH = -6
    INVALID_PASSWORD = -7
    NO_COUNTRY = -8