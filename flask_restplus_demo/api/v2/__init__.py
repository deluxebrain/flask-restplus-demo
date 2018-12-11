import logging

from flask import Blueprint
from flask_restplus_demo.api.v2.api import api
from flask_restplus_demo.api.v2.users import ns as users_ns

log = logging.getLogger(__name__)

blueprint = Blueprint('api_v2', __name__, url_prefix="/api/v2")
api.init_app(blueprint)
api.add_namespace(users_ns)