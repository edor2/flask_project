import sqlite3
from flask import request
from flask_restful import Resource, Api, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parse = reqparse.RequestParser()
    parse.add_argument(
    'username',
    required=True,
    help="credentials could not be found"
    )
    parse.add_argument("password")


    def post(self):
        data = UserRegister.parse.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'user already exists'}, 400

        user =  UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201
