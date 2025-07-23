from flask import request, jsonify
from flask_restful import Resource
from models.cart import Cart
from app import db

class CartList(Resource):
    def get(self, user_id):
        carts = Cart.query.filter_by(user_id=user_id).all()
        return [{'id':cart.id, 'product_id':cart.product_id, 'quantity':cart.quantity} for cart in carts]
    

    def post(self, user_id):
        data = request.get_json()
        cart = Cart(user_id=user_id, product_id=data['product_id'], quantity=data['quantity'])
        db.session.add(cart)
        db.session.commit()
        return {'message':'Product added to Cart successfully'}
    