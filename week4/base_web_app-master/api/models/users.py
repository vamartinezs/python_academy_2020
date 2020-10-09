from ..app import db
from .products import Products
import json


# from .products import Products
# from app import db


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(64), index=True, unique=True)
    email = db.Column("email", db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    products = db.relationship('Products', backref='products', lazy='dynamic')

    def __init__(self, name, email=None, password_hash=None, products=None):
        self.name = name
        self.email = email
        self.password_hash = password_hash
        if products is None:
            self.products = []
        else:
            self.products = products

    def __repr__(self):
        return f'<User {self.name}>'

    def to_json(self):
        prod_dict = {}
        for product in self.products:
            prod_dict[product.title] = product.to_json()

        return {"name": self.name,
                "email": self.email,
                "password hash": self.password_hash,
                "products": prod_dict
                }

    def default(o):
        if hasattr(o, 'to_json'):
            return o.to_json()
        raise TypeError(f'Object of type {o.__class__.__name__} is not JSON serializable')


def does_user_exist(users_tb, name):
    return users_tb.query.filter_by(name=name).first()


def get_tables(users_tb):
    users = users_tb.query.all()
    return users


def get_user_by_name(users_tb, name):
    return users_tb.query.filter_by(name=name).first()


def get_user_by_email(users_tb, email):
    return users_tb.query.filter_by(email=email).first()


def get_users_emails(users_tb):
    users = users_tb.query.all()
    return {user.name: user.email for user in users}


def delete_user_by_email(users_tb, email):
    return users_tb.query.filter_by(email=email).delete()


def delete_user_by_name(users_tb, name):
    return users_tb.query.filter_by(name=name).delete()
