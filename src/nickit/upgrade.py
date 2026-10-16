from nickit.constants import COMMAND_SUCCESS
from nickit.message import show_success_message
from subprocess import run


def upgrade_cli():
    result = run(
        'pip install nickit --upgrade', capture_output=True, text=True, shell=True
    )

    if result.returncode == COMMAND_SUCCESS:
        print(result.stdout)
        show_success_message('nickit was upgraded successfully')
    else:
        print(result)
