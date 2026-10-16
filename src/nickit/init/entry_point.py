from nickit.constants import COMMAND_SUCCESS, OS
from nickit.message import show_information_message, show_success_message
from nickit.utils import check_os
from re import match
from subprocess import run


def init_project(name: str):
    """Checking out if uv is installed"""
    command = 'uv --version'
    result = run(command, capture_output=True, text=True, shell=True)
    pattern = r'^uv \d+.\d+.\d+'

    if not match(pattern, result.stdout):
        show_information_message('uv is not found then installing...')

        if check_os() == OS.WINDOWS:
            # installing uv
            run(
                'powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"'
            )

            # adding uv into path on windows
            run(
                '$env:Path = "C:\\Users\\User\\.local\\bin;$env:Path"',
                capture_output=True,
                text=True,
                shell=True,
            )
        elif check_os() == OS.LINUX:
            # installing uv
            run('curl -LsSf https://astral.sh/uv/install.sh | sh')

            # activaing uv asap
            run('source ~/.bashrc')

    show_information_message('creating a new project using uv')
    command = f'uv init {name}'
    result = run(command, capture_output=True, text=True, shell=True)

    if result.returncode == COMMAND_SUCCESS:
        # init venv
        command = f'uv venv {name}/.venv'
        run(command, capture_output=True, text=True, shell=True)

        show_success_message('project structure created')
