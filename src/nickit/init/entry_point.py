from nickit.constants import COMMAND_SUCCESS
from nickit.message import show_information_message, show_success_message
from re import match
from subprocess import run


def init_project():
    """Checking out if uv is installed"""
    command = 'uv --version'
    result = run(command, capture_output=True, text=True, shell=True)

    pattern = r'^uv \d+.\d+.\d+'
    if not match(pattern, result.stdout):
        show_information_message('uv is not found then installing...')
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

    show_information_message('creating a new project using uv')
    result = run('uv init', capture_output=True, text=True, shell=True)
    if result.returncode == COMMAND_SUCCESS:
        show_success_message('project structure created')
