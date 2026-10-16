from .entry_point import init_project
from .ruff_settings import add_ruff_settings
from .vscode_settings import add_vscode_settings
from nickit.message import show_success_message
from typer import Typer

app = Typer()


@app.command()
def project(name: str):
    """It's going to init an empty project following up a right structure"""
    init_project(name)

    add_ruff_settings(name)
    add_vscode_settings(name)

    show_success_message('project has been initialized successfully')
