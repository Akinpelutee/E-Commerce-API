from flask_restful import Resource
from models.cart import Cart
from extensions import db

class CartList(Resource):
    def post(self, user_id):
        data = {'product_id': 1, 'quantity': 2}
        cart = Cart(user_id=user_id, product_id=data['product_id'], quantity=data['quantity'])
        db.session.add(cart)
        db.session.commit()
        return {'message': 'Product added to cart successfully'}

    def get(self, user_id):
        carts = Cart.query.filter_by(user_id=user_id).all()
        return [{'id': cart.id, 'product_id': cart.product_id, 'quantity': cart.quantity} for cart in carts]

def init_routes(api):
    api.add_resource(CartList, '/users/<int:user_id>/cart')