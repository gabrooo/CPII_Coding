from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from models import db, ProductModel, PedidoModel, UsuarioModel
 
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
 
db.init_app(app)
api = Api(app)
 
with app.app_context():
    db.create_all()
 
##################### Endpoint Usuarios #####################
   
class Usuario(Resource):

    #### Metodo GET ####
    def get(self, usuario_id=None):
 
        if usuario_id != None:
            user = UsuarioModel.query.filter_by(id=usuario_id).first()
 
            if user:
                return {'id': user.id, 'name': user.name, 'email': user.email, 'idade': user.idade}, 200
            else:
                return {'error': 'Task not found'}, 404
 
        else:
            print("Não encontrado")

           
    #### Metodo POST ####
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='name is required')
        parser.add_argument('email', type=str)
        parser.add_argument('idade', type=int)
        args = parser.parse_args()
 
        user = UsuarioModel(name=args['name'], email=args['email'], idade=args['idade'])
        db.session.add(user)
        db.session.commit()
 
        return {'id': user.id, 'name': user.name, 'email': user.email, 'idade': user.idade}, 201
   
 
##################### Endpoint Product #####################
class Product(Resource):
 
    #### Metodo GET ####  
    def get(self, prod_id=None):
 
        if prod_id != None:
            prod = ProductModel.query.filter_by(id=prod_id).first()
 
            if prod:
                return {'id': prod.id, 'name': prod.name, 'price': prod.price, 'stock': prod.stock}, 200
            else:
                return {'error': 'Produto não encontrado'}, 404
 
        else:
            print("Produto não encontrado")

           
    #### Metodo POST ####
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
   
 
##################### Endpoint Pedidos #####################
 
class Pedidos(Resource):
 
    #### Metodo GET ####
    def get(self, pedido_id=None):
 
        if pedido_id != None:
            order = PedidoModel.query.filter_by(id=pedido_id).first()
 
            if order:
                return {'id': order.id, 'usuario_id': order.usuario_id, 'descricao': order.descricao, 'status': order.status, 'id_produto': order.id_produto}, 200
            else:
                return {'error': 'Pedido não encontrado'}, 404
 
        else:
            print("Pedido não encontrado")

       
    #### Metodo POST ####
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('usuario_id', type=int, required=True, help='ID User is required')
        parser.add_argument('descricao', type=str, required=True, help='description is required')
        parser.add_argument('status', type=str)
        parser.add_argument('id_produto', type=int, required=True, help='ID Product is required')
        args = parser.parse_args()
 
        order = PedidoModel(usuario_id=args['usuario_id'],descricao=args['descricao'], status=args['status'],id_produto=args['id_produto'])
        db.session.add(order)
        db.session.commit()
 
        return {'id': order.id, 'descricao': order.descricao, 'status': order.status}, 201
 
 
api.add_resource(Product, '/products', '/products/<int:prod_id>')
api.add_resource(Pedidos, '/pedidos', '/pedidos/<int:pedido_id>')
api.add_resource(Usuario, '/usuario', '/usuario/<int:usuario_id>')
 
if __name__ == '__main__':
 
    app.run(debug=True)