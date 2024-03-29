from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

#MODELS
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), )
    published_year = db.Column(db.Integer)
    price = db.Column(db.Float, nullable=False)
    qty_in_stock= db.Column(db.Integer,default= 0)


class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    yob= db.Column(db.Integer, nullable=False)
    nationality=db.Column(db.String, nullable=True)
    books = db.relationship("Book", backref="author", lazy=True)  # one-


class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email= db.Column(db.String(50), unique=True, nullable=False)
    phone= db.Column(db.String(14), unique=True, nullable=False)
    address=db.Column(db.String(50), nullable=False)
