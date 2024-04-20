from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

##BANCOS DE DADOS PRODUTOS

class ProductModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock= db.Column(db.Integer, nullable=False)

##BANCOS DE DADOS PEDIDOS

class PedidoModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    id_produto = db.Column(db.Integer, nullable=False)

##BANCOS DE DADOS USUARIOS

class UsuarioModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    idade = db.Column(db.Integer, nullable=False)


