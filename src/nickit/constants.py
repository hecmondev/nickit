from enum import StrEnum

COMMAND_SUCCESS = 0
COMMAND_FAILURE = 1


class Architectures(StrEnum):
    MVT = 'mvt'
    MVC = 'mvc'
    DOMAIN_DRIVEN_DESIGN = 'ddd'
    CLEAN_ARCHITECTURE = 'ca'


class OS(StrEnum):
    WINDOWS = 'Windows'
    LINUX = 'Linux'
    MACOS = 'Darwin'
