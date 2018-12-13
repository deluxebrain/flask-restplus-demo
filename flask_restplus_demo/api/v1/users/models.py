from flask_restplus import fields
from flask_restplus_demo.api.v1.api import api

user = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The user unique identifier'),
    'first_name': fields.String(required=True, description='The user first name'),
    'last_name': fields.String(required=True, description='The user last name'),
    'email_address': fields.String(required=False, description='The user email address')
})