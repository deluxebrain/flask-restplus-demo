import logging

from flask_restplus_demo.extensions import ma

log = logging.getLogger(__name__)

class UserSchema(ma.Schema):
    class meta:
        fields = ('id', 'first_name', 'last_name', 'email_address')
    #_links = ma.Hyperlinks({
    #    'self': ma.URLFor('UserItem', id='<id>'),
    #    'collection': ma.URLFor('UsersCollection')
    #})

user_schema = UserSchema()
users_schema = UserSchema(many=True)