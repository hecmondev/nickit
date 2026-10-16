from inspect import cleandoc
from nickit.message import show_success_message
from nickit.utils import add_directory
from pathlib import Path


def create_vscode_settings_file(vscode_directory_path: Path):
    """Creating settings.json file under .vscode folder"""
    settings_file_path = vscode_directory_path / 'settings.json'
    with open(settings_file_path, 'w') as file:
        setting = """
            {
                "[python]": {
                    "editor.defaultFormatter": "charliermarsh.ruff",
                    "editor.formatOnSave": true,
                    "editor.codeActionsOnSave": {
                        "source.fixAll": "explicit",
                        "source.organizeImports": "explicit"
                    }
                },
                "editor.tabSize": 4,
            }
        """
        file.write(cleandoc(setting))
    show_success_message('.vscode/settings.json was added successfully')


def add_vscode_settings(name: str):
    """Adding settings file under .vscode folder"""
    vscode_directory_path = add_directory(f'{name}/.vscode')
    create_vscode_settings_file(vscode_directory_path)
