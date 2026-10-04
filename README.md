# nickit

An interesting cli to improve the development experience on python

## why nickit

the idea is looking for a controlled way to create python projects
from scratch including empty projects, django, flask, fastapi and
ai sort of projects with all of the necessary configurations done
but following the best practices and also allowing to the developer
select which architecture needed for the project created.

## how to use it

### installing

since this is python library you must have installed pip (python package manager)
firstly then just run the next command:

```bash
pip install nickit
```

### using

this is the list of commands available:

**get current version**

```bash
nic version
```

**init an empty project** with basic initial settings
project name param is optional if this param is not
provided the cli is going to take parent folder as
project name

```bash
nic init project <project-name>
```

**init fastapi project** with the latest way following [official documentation](https://fastapi.tiangolo.com/#installation)
project name param is optional if this param is not
provided the cli is going to take parent folder as
project name

```bash
nic init fastapi

# including architecture
nic init fastapi <project-name> --architecture mvc
```

## how to contribute

first thing to do before any change is increasing the version with the next command:

```bash
uv version 0.0.10
```

then just apply the changes and send the pull request to main branch
