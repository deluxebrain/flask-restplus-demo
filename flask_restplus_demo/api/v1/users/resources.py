import logging

from flask import Flask, jsonify
from flask_restplus import Resource
from flask_restplus_demo.api.v1.api import api
from flask_restplus_demo.api.v1.users.models import user
from flask_restplus_demo.api.v1.users.schemas import user_schema, users_schema

log = logging.getLogger(__name__)

ns = api.namespace('users', description='User endpoints')

@ns.route('/')
class UsersCollection(Resource):
    def get(self):
        result = users_schema.dump([])
        return jsonify(result.data)
        # return []

@ns.route('/<int:id>')
@api.response(404, 'User not found')
class UserItem(Resource):
    def get(self, id):
        return user_schema.jsonify(user(1, "a", "b", "c"))
        # return {}

