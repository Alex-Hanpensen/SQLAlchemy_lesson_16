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


@app.route('/users/<u_id>/del')
def del_user(u_id):
    user = models.Users.query.get_or_404(u_id)
    return redirect('/users') if modifiation_db.del_obj_db(user) is None else modifiation_db.del_obj_db(user)


@app.route('/users/<u_id>/update', methods=['POST', 'GET'])
def update_user(u_id):
    user = models.Users.query.get(u_id)
    if request.method == 'POST':
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.age = request.form['age']
        user.email = request.form['email']
        user.role = request.form['role']
        user.phone = request.form['phone']

        return redirect('/users') if modifiation_db.update_data_db(user) is None else modifiation_db.update_data_db(
            user)
    else:
        return render_template('update_user.html', item=user)


@app.route('/orders')
def get_orders():
    orders = models.Orders.query.all()
    return render_template('get_orders.html', item=orders)


@app.route('/orders/<u_id>')
def get_order(u_id):
    order = models.Orders.query.get(u_id)
    return render_template('get_order.html', item=order)


@app.route('/orders/<u_id>/del')
def del_order(u_id):
    order = models.Orders.query.get_or_404(u_id)
    return redirect('/orders') if modifiation_db.del_obj_db(order) is None else modifiation_db.del_obj_db(order)


@app.route('/orders/<u_id>/update', methods=['POST', 'GET'])
def update_order(u_id):
    order = models.Orders.query.get(u_id)
    if request.method == 'POST':
        order.name = request.form['name']
        order.description = request.form['description']
        order.start_date = request.form['start_date']
        order.end_date = request.form['end_date']
        order.address = request.form['address']
        order.price = request.form['price']

        return redirect('/users') if modifiation_db.update_data_db(order) is None else modifiation_db.update_data_db(
            order)
    else:
        return render_template('update_order.html', item=order)


@app.route('/offers')
def get_offers():
    offers = models.Offers.query.all()
    return render_template('get_offers.html', item=offers)


@app.route('/offers/<u_id>')
def get_offer(u_id):
    offer = models.db.session.query(models.Users, models.Offers).join(models.Offers).filter(models.Offers.id == u_id)
    order = models.Orders.query.get(offer.all()[0][1].order_id)
    res = offer.all()[0][0], order, offer.all()[0][1]
    return render_template('get_offer.html', item=res)


@app.route('/offers/<u_id>/del')
def del_offers(u_id):
    offer = models.Offers.query.get_or_404(u_id)
    return redirect('/offers') if modifiation_db.del_obj_db(offer) is None else modifiation_db.del_obj_db(offer)


@app.route('/offers/<u_id>/update', methods=['POST', 'GET'])
def update_offer(u_id):
    offer = models.Offers.query.get(u_id)
    if request.method == 'POST':
        offer.order_id = request.form['order_id']
        offer.executor_id = request.form['executor_id']

        return redirect('/offers') if modifiation_db.update_data_db(offer) is None else modifiation_db.update_data_db(
            offer)
    else:
        return render_template('update_offer.html', item=offer)


@app.route('/created-user', methods=['POST', 'GET'])
def created_user():
    if request.method == 'POST':
        data = {'first_name': request.form['first_name'], 'last_name': request.form['last_name'],
                'age': request.form['age'], 'email': request.form['email'],
                'role': request.form['role'], 'phone': request.form['phone'],
                }
        return redirect('/users') if modifiation_db.add_obj_db(data, 'Users') is None else modifiation_db.add_obj_db(
            data, 'Users')

    return render_template('created-user.html')


@app.route('/created-order', methods=['POST', 'GET'])
def created_order():
    if request.method == 'POST':
        data = {'name': request.form['name'], 'description': request.form['description'],
                'start_date': request.form['start_date'], 'end_date': request.form['end_date'],
                'address': request.form['address'], 'price': request.form['price'],
                'customer_id': request.form['customer_id'],
                'executor_id': request.form['executor_id']}
        return redirect('/orders') if modifiation_db.add_obj_db(data, 'Orders') is None else modifiation_db.add_obj_db(
            data, 'Orders')

    return render_template('created-order.html')


@app.route('/created-offer', methods=['POST', 'GET'])
def created_offer():
    if request.method == 'POST':
        data = {'order_id': request.form['order_id'], 'executor_id': request.form['executor_id']}
        return redirect('/offers') if modifiation_db.add_obj_db(data, 'Offers') is None else modifiation_db.add_obj_db(
            data, 'Offers')

    return render_template('created-offer.html')
