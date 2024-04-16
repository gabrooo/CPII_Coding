from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class ProductModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=False)

    price = db.Column(db.Float, nullable=False)

    stock = db.Column(db.Integer, nullable=False)


def __repr__(self):


    return f'<Product {self.name}>'