from flask_restplus_demo.api.v1.api import api
from flask_restplus_demo.api.v1.users.resources import api as users_ns

api.add_namespace(users_ns)
