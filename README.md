# flaskenv
This script creates a basic Flask app directory and file structure and initializes a virtual environment within the project folder.

It should run on both Linux and MacOS.

Folder and file structur

    <project name>
     |- app
     |   |- templates
     |   |- static
     |   |- venv
     |   |- __init__.py
     |   |- views.py
     |- run.py

## Usage
    Usage: flaskenv.py <project name>

## Post creation
To activate the virtual environment run:

    . <project_name>/venv/bin/activate

Install Flask:

    pip install flask

