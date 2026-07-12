from typer import Typer

app = Typer()


@app.command()
def project():
    with open('example.txt', 'w') as file:
        file.write('Hello, this is a newly created file!')
