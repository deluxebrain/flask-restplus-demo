import logging

from flask import Blueprint
from flask_restplus_demo.api.v1.api import api

log = logging.getLogger(__name__)

blueprint = Blueprint('api_v1', __name__, url_prefix="/api/v1")
api.init_app(blueprint)

from . import users
