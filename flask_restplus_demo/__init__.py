import os
import logging.config

from flask import Flask, Blueprint
from flask_restplus_demo.extensions import init_app
from flask_restplus_demo.api.v1 import blueprint as v1_endpoints
from config import config_map

def create_app(config_name):

    # get the corresponding config
    config = config_map[config_name]

    # as we are using a package the application object should be given a hardcoded name
    # the following will pull the application name assuming myapp/__init__.py
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config)
    config.init_app(app)
    app.register_blueprint(v1_endpoints)

    return app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
init_app(app)
