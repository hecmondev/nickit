from nickit.constants import Architectures
from nickit.utils import add_directory


def add_mvc_architecture():
    models_directory = add_directory('models')
    views_directory = add_directory('views')
    controller_directory = add_directory('controllers')


def add_architecture(architecture: str = ''):
    # check if dev wants to add any supported architecture
    match architecture:
        case Architectures.MVT:
            pass
        case Architectures.MVC:
            add_mvc_architecture()
        case Architectures.DOMAIN_DRIVEN_DESIGN:
            pass
        case Architectures.CLEAN_ARCHITECTURE:
            pass
