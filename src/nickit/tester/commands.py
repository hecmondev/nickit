from nickit.constants import COMMAND_SUCCESS
from nickit.message import show_information_message
from nickit.utils import add_directory
from nickit.version import get_project_version
from pathlib import Path
from subprocess import run
from typer import Typer

app = Typer()


@app.command(help='build latest version of the nickit under development')
def build():
    # check if the cli is under nickit project source folder
    current_directory = Path.cwd()

    if current_directory.name != 'nickit':
        show_information_message(
            'this command can be executed only under nickit source folder'
        )
        return

    # otherwise carry on the build process
    result = run('uv build', capture_output=True, text=True, shell=True)

    if result.stdout == COMMAND_SUCCESS:
        show_information_message('latest version of lib built successfully')

        # create testing folder
        add_directory('testing')

        # getting working version
        version = get_project_version()
        splitted_version = version.split('.')
        working_version = (
            f'{".".join(splitted_version[:-1])}.{int(splitted_version[-1]) + 1}'
        )

        # copy latest built version
        command = f'cp -rf dist/nickit-{working_version}.tar.gz testing'
        result = run(command, capture_output=True, text=True, shell=True)

        if result.stdout == COMMAND_SUCCESS:
            show_information_message('go to testing folder for testing')


@app.command(name='run', help='enable built development version')
def run_tester():
    # check if the cli is under nickit/testing folder
    current_directory = Path.cwd()

    if current_directory.name != 'testing':
        show_information_message(
            'this command can be executed only under nickit/testing folder'
        )
        return

    # otherwise carry on the run tester process
    command = 'uv run --with nickit --no-project python -c "import nickit"'
    result = run(command, capture_output=True, text=True, shell=True)

    if result.stdout == COMMAND_SUCCESS:
        show_information_message('tester is up and running under nickit/testing folder')
