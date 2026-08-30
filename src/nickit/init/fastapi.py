from typer import Typer, Argument, Option
from subprocess import run
from nickit.message import show_success_message
from nickit.constants import COMMAND_SUCCESS
from .vscode_settings import add_vscode_settings
from .entry_point import init_project
from .ruff_settings import add_ruff_settings
from .architecture import add_architecture
from pathlib import Path
from inspect import cleandoc
from .settings import add_settings
from typing import Annotated

app = Typer()


def add_fastapi():
    """Add fastapi on the project"""
    result = run(
        'uv add "fastapi[standard]"', capture_output=True, text=True, shell=True
    )

    if result.returncode == COMMAND_SUCCESS:
        show_success_message('fastapi was added successfully')


def init_application():
    main_file_path = Path().resolve() / 'main.py'
    with open(main_file_path, 'w') as file:
        code = """
            from fastapi import FastAPI

            app = FastAPI()

            @app.get('/')
            async def hello_world():
                return {'hello': 'world'}
        """
        file.write(cleandoc(code))


@app.command()
def fastapi(
    name: Annotated[str, Argument()] = '', architecture: Annotated[str, Option()] = ''
):
    """It's going to init a fastapi project following up a right structure"""
    init_project(name)

    add_ruff_settings()
    add_vscode_settings()
    add_fastapi()

    # check if dev wants to add any supported architecture
    if architecture is not None:
        add_architecture(architecture)

    init_application()
    add_settings()

    show_success_message('fastapi project has been initialized successfully')
