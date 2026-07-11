from importlib.metadata import version
from nickit.message import show_success_message


def get_cli_version():
    current_version = version('nickit')
    show_success_message(f'CLI Nickit Version {current_version}', background=True)
