# routes/order_routes.py
from flask import request, jsonify
from flask_restful import Resource
from models.order import Order
from extensions import db

class OrderList(Resource):
    def get(self, user_id):
        orders = Order.query.filter_by(user_id=user_id).all()
        return [{'id': order.id, 'order_date': order.order_date, 'total': order.total} for order in orders]

    def post(self, user_id):
        data = request.get_json()
        order = Order(user_id=user_id, total=data['total'])
        db.session.add(order)
        db.session.commit()
        return {'message': 'Order placed successfully'}