from pathlib import Path


def add_directory(name: str) -> Path:
    """Creating a new folder using name parameter

    Returns:
        Path: including the new folder created
    """
    directory_path = Path().resolve() / name
    directory_path.mkdir(parents=True, exist_ok=True)
    return directory_path
