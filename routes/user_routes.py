from flask import request, jsonify
from flask_restful import Resource
from models.users import User
from app import db


class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        user = User(username=data['username'], email=data['email'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return {'message': 'User created Successfully'}
    

class UserLogin(Resource):
    def post(self):
        data = request.get_json
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            return {'message':'User logged in successfully'}
        return {'message':'Invalid Credentials'}, 401