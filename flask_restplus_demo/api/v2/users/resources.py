import logging

from flask import Flask, jsonify
from flask_restplus import Resource, Namespace
from flask_restplus._http import HTTPStatus
from flask_restplus_demo.api.v2.users.schemas import UserSchema

log = logging.getLogger(__name__)

api = Namespace('users', description='User endpoints')

@api.route('/', endpoint='UsersCollection')
class UsersCollection(Resource):
    @api.response(UserSchema(many=True), description='Get all users')
    def get(self):
        result = UserSchema(many=True).dump([])
        return jsonify(result.data)

@api.route('/<int:id>', endpoint='UserItem')
@api.param('id', 'The user identifier')
@api.response(code=HTTPStatus.NOT_FOUND, description='User not found')
class UserItem(Resource):
    @api.response(UserSchema(), description='Get user by id')
    def get(self, id):
        user = {
            'id': 1,
            'first_name': 'Bob',
            'last_name': 'Smith',
            'email_address': 'bob.smith@example.com'
        }
        return UserSchema().dump(user)
