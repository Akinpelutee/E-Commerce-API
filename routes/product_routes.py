# routes/product_routes.py
from flask import request, jsonify
from flask_restful import Resource
from models.product import Product
from app import db

class ProductList(Resource):
    def get(self):
        products = Product.query.all()
        return [{'id': product.id, 'name': product.name, 'price': product.price} for product in products]

    def post(self):
        data = request.get_json()
        product = Product(name=data['name'], description=data['description'], price=data['price'], quantity=data['quantity'])
        db.session.add(product)
        db.session.commit()
        return {'message': 'Product created successfully'}

class ProductDetail(Resource):
    def get(self, product_id):
        product = Product.query.get(product_id)
        if product:
            return {'id': product.id, 'name': product.name, 'price': product.price}
        return {'message': 'Product not found'}, 404