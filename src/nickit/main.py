from .init import app as init_app
from .version import get_cli_version
import typer

app = typer.Typer()


@app.command()
def version():
    """To get the current cli version installed"""
    get_cli_version()


app.add_typer(
    init_app,
    name='init',
    help='A set of subcommands to improve development starting a new project',
)


def run():
    app()
