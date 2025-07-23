from flask_restful import Resource
from models.users import User
from extensions import db

class UserRegistration(Resource):
    def post(self):
        data = {'username': 'test', 'email': 'test@example.com', 'password': 'password'}
        user = User(username=data['username'], email=data['email'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return {'message': 'User created successfully'}

class UserLogin(Resource):
    def post(self):
        data = {'username': 'test', 'password': 'password'}
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            return {'message': 'User logged in successfully'}
        return {'message': 'Invalid credentials'}, 401

def init_routes(api):
    api.add_resource(UserRegistration, '/register')
    api.add_resource(UserLogin, '/login')