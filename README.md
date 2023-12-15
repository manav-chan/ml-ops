# ML Operations

## Getting Started
- Setting up the virtual environment
```console
conda create -p /path/to/virtual-environment python=3.11 -y
conda activate /path/to/venv
```

- Creating a gitignore file for python using the github template.
- Creating a setup.py file so that the application can be packaged to be used with other projects or deploy to PyPI.
- Directories which have __init__.py will be treated as packages. For example, 'src' directory.
- Make a requirements.txt file to store the packages that need to be installed ending with '-e .', which will trigger setup.py whenever the packages from the requirements.txt are installed.

- Run the following command, a new package (directory) will be created, which can be used or deployed to PyPI
```console
pip install -r requirements.txt
```
