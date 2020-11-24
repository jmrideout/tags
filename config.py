import os
import sys

from os.path import abspath, dirname, join
base_path  = dirname(abspath(__file__))
sys.path.insert(1, join(base_path, 'lib'))
sys.path.insert(1, join(base_path, 'models'))

from flask import Flask
from flask_orator import Orator
import yaml

app = None
db = None   # Module to share Orator DB variables

FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'

def app_init(appname):
    global db
    global app
    app = Flask(appname)

    app.config['ORATOR_DATABASES'] = load_db_config()
    app.config['ORATOR_DATABASES']['default'] = FLASK_ENV

    db = Orator(app)

    return app


def load_config(config_file):
    return yaml.safe_load(open(join(dirname(__file__), config_file)))

def load_db_config():
    return load_config('config/database.yml')
