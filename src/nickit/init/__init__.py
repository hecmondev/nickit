from .project import app as project_app
from .fastapi import app as fastapi_app
from typer import Typer

app = Typer()

app.add_typer(project_app)
app.add_typer(fastapi_app)
