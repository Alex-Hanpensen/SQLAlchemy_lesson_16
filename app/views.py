from app import app
from flask import render_template
from . import models


@app.route('/users')
def index():
    user = models.Users.query.all()
    result = [(i.last_name, i.age, i.email, i.role, i.phone) for i in user]
    return render_template('index.html', item=result)
