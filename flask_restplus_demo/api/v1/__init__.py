import logging

from flask import Blueprint
from flask_restplus_demo.api.v1.api import api
from flask_restplus_demo.api.v1.users import ns as users_ns

log = logging.getLogger(__name__)

blueprint = Blueprint('api_v1', __name__, url_prefix="/api/v1")
api.init_app(blueprint)
api.add_namespace(users_ns)