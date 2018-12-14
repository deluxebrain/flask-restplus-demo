import logging

from flask import Blueprint
from flask_restplus_demo.api.v2.api import api

log = logging.getLogger(__name__)

blueprint = Blueprint('api_v2', __name__, url_prefix="/api/v2")
api.init_app(blueprint)

from . import users
