from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.cookie_models import Cookie_order

app.route('/')
def index():
    return redirect('/cookies')

app.route('/cookies')
def all_orders():
    return render_template('cookie_orders.html', all_orders=Cookie_order.get_all())