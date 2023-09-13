from app import app, SQLAlchemy
from . import create_table

db = SQLAlchemy(app)


class Users(db.Model):  # Юзеры
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String, unique=True)
    role = db.Column(db.String, nullable=False)
    phone = db.Column(db.String)

    def __init__(self, first_name, last_name, age, email, role, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.role = role
        self.phone = phone
        self.offers = create_table.offers
        self.orders = create_table.orders

    def __repr__(self):
        return f'<user: {self.id}'


class Orders(db.Model):  # Заказы
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    address = db.Column(db.String)
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    customers = db.relationship('Users',
                                foreign_keys=[Users.id],
                                primaryjoin="Orders.customer_id == Users.id and Users.role == \"customer\"",
                                )

    executors = db.relationship('Users',
                                foreign_keys=[Users.id],
                                primaryjoin="Orders.executor_id == Users.id and Users.role == \"executor\"",
                                overlaps="customers"
                                )

    def __init__(self, name, description, start_date, end_date, address, price, customer_id, executor_id):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.address = address
        self.price = price
        self.customer_id = customer_id
        self.executor_id = executor_id


class Offers(db.Model):  # предложение
    __tablename__ = 'offers'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(Orders.id))
    executor_id = db.Column(db.Integer, db.ForeignKey(Users.id))

    orders = db.relationship('Orders')
    executors = db.relationship('Users')

    def __init__(self, order_id, executor_id):
        self.order_id = order_id
        self.executor_id = executor_id


with app.app_context():
    db.create_all()
    for user in create_table.users:
        db.session.add(Users(**{k: v for k, v in user.items() if k != 'id'}))

    for order in create_table.orders:
        db.session.add(Orders(**{k: v for k, v in order.items() if k != 'id'}))

    for offer in create_table.offers:
        db.session.add(Offers(**{k: v for k, v in offer.items() if k != 'id'}))
    db.session.commit()
