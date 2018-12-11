import logging

from flask_restplus import Api

log = logging.getLogger(__name__)

api = Api(version="1.0",
    title="Hello World v1.0",
    description="Hello World v1.0")
