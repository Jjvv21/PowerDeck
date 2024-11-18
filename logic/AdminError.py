from enum import Enum

class AdminError(Enum):
    NAME_LENGTH = -1
    NO_MAIL = -2
    USED_MAIL = -3
    PASSWORD_LENGTH = -4
    INVALID_PASSWORD = -5
    NO_ROLE = -6