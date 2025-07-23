from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import Config
from routes.user_routes import UserRegistration, UserLogin
from routes.product_routes import ProductList, ProductDetail
from routes.cart_routes import CartList
from routes.order_routes import OrderList

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    api = Api(app)

    api.add_resource(UserRegistration, '/register')
    api.add_resource(UserLogin, '/login')
    api.add_resource(ProductList, '/products')
    api.add_resource(ProductDetail, '/products/<int:product_id>')
    api.add_resource(CartList, '/users/<int:user_id>/cart')
    api.add_resource(OrderList, '/users/<int:user_id>/orders')

    return app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)