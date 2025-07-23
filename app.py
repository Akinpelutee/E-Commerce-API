from flask import Flask
from config import Config
from extensions import db, api
from routes import user_routes, product_routes, cart_routes, order_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    api.init_app(app)

    user_routes.init_routes(api)
    product_routes.init_routes(api)
    cart_routes.init_routes(api)
    order_routes.init_routes(api)

    return app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)