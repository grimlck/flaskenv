#!/usr/bin/env python3

import subprocess
import os
import sys

COMMANDS = {'venv': 'virtualenv --no-site-packages venv'}
FLASK_DIRECTORIES = ['app/static', 'app/templates']
FLASK_FILES = {
        'run.py': '#!/usr/bin/env python\nfrom app import app\n\napp.run(debug=True)',
        'app/__init__.py': '''from flask import Flask\n\napp = Flask(__name__)\nfrom app import views''',
        'app/views.py': '''from app import app\n\n@app.route('/')\n@app.route('/index')\ndef index(): pass'''
}


basedir = os.getcwd()


def check_requirements():
    """
    Check if required command line tools are present on the system
    """

    cli_tools = [v.split()[0] for v in COMMANDS.values()]
    locations = os.environ.get("PATH").split(os.pathsep)

    error = 0

    for app in cli_tools:
        for location in locations:
            if os.path.isfile(os.path.join(location, app)):
                found = True
                break
            else:
                found = False
        if found is False:
            print(app + ' required but not found on the system.')
            error += 1

    if error > 0:
        return 1
    else:
        return 0


def create_directories(project_name):
    """
    Create basic directory structure for the flask project

    project_name
     |- app
        |-static
        |-templates
    """

    project_directory = os.path.join(basedir, project_name)

    try:
        os.mkdir(project_directory)
        for directory in FLASK_DIRECTORIES:
            os.makedirs(os.path.join(project_directory, directory))

        return 0
    except OSError as e:
        sys.exit('Errno ' + str(e.errno) + ' - ' + e.strerror)


def create_virtualenv():
    """
    Create a virtualenv named 'venv'
    """
    command = COMMANDS['venv'].split()

    if os.path.exists('venv'):
        print('Directory already exists.')
    else:
        if subprocess.call(command) == 0:
            return True
        else:
            return False


def create_files(project_name):
    """
    Create the basic project files and its contents

    project_dir
     |- run.py
     |- app/
         |- __init__.py
         |- views.py
    """
    project_directory = os.path.join(basedir, project_name)

    for filename, content in FLASK_FILES.items():
        filename = os.path.join(project_directory, filename)
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                f.write(content)


def usage():
    print('Usage: ' + os.path.basename(__file__) + ' <project name>')


def post_creation():
    print('''To activate the virtual environment run:
. <project_name>/venv/bin/activate
Install Flask:
pip install flask''')


def main():
    if len(sys.argv) < 2:
        usage()
    else:
        if check_requirements() == 1:
            print('Fulfill requirements first.')
            sys.exit()
        else:
            if create_directories(sys.argv[1]) == 0:
                create_files(sys.argv[1])
                os.chdir(sys.argv[1])
            create_virtualenv()
            post_creation()

if __name__ == "__main__":
    main()
