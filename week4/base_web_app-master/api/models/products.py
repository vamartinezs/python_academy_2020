from app import db
from .currency import CurrencyEnum


class Products(db.Model):
    __tablename__ = "products"
    title = db.Column(db.String(50), unique=False, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float(10, 2), unique=False, nullable=False)
    currency_types = db.Column(db.Enum(CurrencyEnum.USD.value, CurrencyEnum.CAD.value), name='currency_types')
    inventory_count = db.Column(db.Integer, default=0, nullable=False)
    visits = db.Column(db.Integer, default=0, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title=None, id=None, price=None, inventory_count=None, visits=None, currency_types=None,
                 user_id=None):
        self.title = title
        self.id = id
        self.price = price
        self.inventory_count = inventory_count
        self.visits = visits
        self.currency_types = currency_types
        self.user_id = user_id

    def __repr__(self):
        return '<product {}>'.format(self.title)

    def increment_visit(self):
        self.visits += 1

    def to_json(self):
        return {"title":self.title,
                "id": self.id,
                "price":  "{:.2f}".format(self.price),
                "inventory": self.inventory_count,
                "visits": self.visits,
                "currency": self.currency_types,
                "user_id": self.user_id
        }

    def default(o):
        if hasattr(o, 'to_json'):
            return o.to_json()
        raise TypeError(f'Object of type {o.__class__.__name__} is not JSON serializable')


def get_tables(products_tb):
    tables = products_tb.query.all()
    return tables
