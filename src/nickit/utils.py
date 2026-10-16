from pathlib import Path
from platform import system


def add_directory(name: str) -> Path:
    """Creating a new folder using name parameter

    Returns:
        Path: including the new folder created
    """
    directory_path = Path().resolve() / name
    directory_path.mkdir(parents=True, exist_ok=True)
    return directory_path


def check_os():
    """Check which OS is running"""
    return system()
