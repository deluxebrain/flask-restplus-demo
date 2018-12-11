import logging

from flask_restplus import Resource
from flask_restplus_demo.api.v1.api import api

log = logging.getLogger(__name__)

ns = api.namespace('users', description='User endpoints')

@ns.route('/')
class UsersCollection(Resource):
    def get(self):
        return { 'users': [] }

@ns.route('/<int:id>')
@api.response(404, 'User not found')
class UserItem(Resource):
    def get(self, id):
        return { 'user_id': id}
    
