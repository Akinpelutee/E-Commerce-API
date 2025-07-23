from flask_restful import Resource
from models.order import Order
from extensions import db

class OrderList(Resource):
    def post(self, user_id):
        data = {'total': 21.98}
        order = Order(user_id=user_id, total=data['total'])
        db.session.add(order)
        db.session.commit()
        return {'message': 'Order placed successfully'}

    def get(self, user_id):
        orders = Order.query.filter_by(user_id=user_id).all()
        return [{'id': order.id, 'order_date': order.order_date, 'total': order.total} for order in orders]

def init_routes(api):
    api.add_resource(OrderList, '/users/<int:user_id>/orders')