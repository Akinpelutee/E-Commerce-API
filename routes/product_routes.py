from flask_restful import Resource
from models.product import Product
from extensions import db

class ProductList(Resource):
    def post(self):
        data = {'name': 'Product 1', 'description': 'This is product 1', 'price': 10.99, 'quantity': 100}
        product = Product(name=data['name'], description=data['description'], price=data['price'], quantity=data['quantity'])
        db.session.add(product)
        db.session.commit()
        return {'message': 'Product created successfully'}

def init_routes(api):
    api.add_resource(ProductList, '/products')