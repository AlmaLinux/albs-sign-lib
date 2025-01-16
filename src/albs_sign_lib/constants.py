import enum

class SignStatusEnum(enum.IntEnum):
    SUCCESS = 1
    READ_ERROR = 2
    NO_SIGNATURE = 3
    WRONG_SIGNATURE = 4
