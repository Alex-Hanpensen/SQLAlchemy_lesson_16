from app import app
from flask import render_template, request, url_for, redirect
from . import models
from . import modifiation_db


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/users')
def get_users():
    users = models.Users.query.order_by(models.Users.first_name)
    return render_template('get_items.html', item=users)


@app.route('/users/<u_id>')
def get_user(u_id):
    user = models.Users.query.get(u_id)
    return render_template('get_user.html', item=user)


@app.route('/orders')
def get_orders():
    orders = models.Orders.query.all()
    return render_template('get_orders.html', item=orders)


@app.route('/orders/<u_id>')
def get_order(u_id):
    order = models.Orders.query.get(u_id)
    return render_template('get_order.html', item=order)


@app.route('/created-user', methods=['POST', 'GET'])
def created_user():
    if request.method == 'POST':
        data = {'first_name': request.form['first_name'], 'last_name': request.form['last_name'],
                'age': request.form['age'], 'email': request.form['email'],
                'role': request.form['role'], 'phone': request.form['phone'],
                }
        return redirect('/users') if modifiation_db.add_user_db(data) is None else modifiation_db.add_user_db(data)

    return render_template('created-user.html')
