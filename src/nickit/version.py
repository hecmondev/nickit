from importlib.metadata import version
from nickit.message import show_success_message


def get_project_version():
    return version('nickit')


def get_cli_version():
    current_version = get_project_version()
    show_success_message(f'CLI Nickit Version {current_version}', background=True)
