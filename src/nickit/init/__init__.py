from .project import app as project_app
from typer import Typer

app = Typer()

app.add_typer(project_app)
