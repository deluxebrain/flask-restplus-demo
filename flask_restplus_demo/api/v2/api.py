import logging

from flask_restplus import Api

log = logging.getLogger(__name__)

api = Api(version="2.0",
    title="Hello World v2.0",
    description="Hello World v2.0")
