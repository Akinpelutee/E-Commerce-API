from flask_restful import Resource
from models.cart import Cart
from extensions import db

class CartList(Resource):
    def post(self):
        data = {'user_id': 1, 'product_id': 1, 'quantity': 2}
        cart = Cart(user_id=data['user_id'], product_id=data['product_id'], quantity=data['quantity'])
        db.session.add(cart)
        db.session.commit()
        return {'message': 'Product added to Cart'}