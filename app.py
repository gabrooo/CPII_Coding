from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from models import db, ProductModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'

db.init_app(app)

api = Api(app)

with app.app_context():

    db.create_all()


class Product(Resource):
    def get(self, prod_id=None):

        if prod_id:
            prod = ProductModel.query.filter_by(id=prod_id).first()

            if prod:
                return {'id': prod.id, 'name': prod.name, 'price': prod.price, 'stock': prod.stock}, 200
            else:
                return {'error': 'Task not found'}, 404

        else:

            prod = ProductModel.query.all()
            return [{'id': prod.id, 'name': prod.name, 'price': prod.price, 'stock': prod.stock} for prod in

                    prod], 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='name is required')
        parser.add_argument('price', type=float)
        parser.add_argument('stock', type=int)
        args = parser.parse_args()

        prod = ProductModel(name=args['name'], price=args['price'], stock=args['stock'])
        db.session.add(prod)
        db.session.commit()

        return {'id': prod.id, 'name': prod.name, 'price': prod.price, 'stock': prod.stock}, 201

    def put(self, prod_id):

        prod = ProductModel.query.filter_by(id=prod_id).first()

        if prod:
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str, required=True, help='name is required')
            parser.add_argument('price', type=float)
            parser.add_argument('stock', type=int)
            args = parser.parse_args()

            prod.name = args['name']
            prod.price = args['price']
            prod.stock = args['stock']

            db.session.commit()
            return {'id': prod.id, 'name': prod.name, 'price': prod.price, 'stock': prod.stock}, 200

        else:
            return {'error': 'Task not found'}, 404
    def delete(self, prod_id):
        prod = ProductModel.query.filter_by(id=prod_id).first()

        if prod:
            db.session.delete(prod)
            db.session.commit()

            return '', 204

        else:
            return {'error': 'Prod not found'}, 404

api.add_resource(Product, '/products', '/products/<int:prod_id>')

if __name__ == '__main__':

    app.run(debug=True)

