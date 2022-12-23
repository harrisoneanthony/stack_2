from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.cookie_models import Cookie_order

@app.route('/')
def index():
    return redirect('/cookies')

@app.route('/cookies')
def all_orders():
    return render_template('cookie_orders.html', all_orders=Cookie_order.get_all())

@app.route('/cookies/new')
def new_order():
    return render_template('new_order.html')

@app.route('/neworder', methods=['POST'])
def save():
    if not Cookie_order.validate_order(request.form):
        return redirect('/cookies/new')
    Cookie_order.save(request.form)
    return redirect('/')

@app.route('/cookies/edit/<int:id>')
def get_one(id):
    return render_template('edit_order.html', cookie_order = Cookie_order.get_one({'id':id}))

@app.route('/cookies/edit/<int:id>', methods=['POST'] )
def update(id):
    if not Cookie_order.validate_order(request.form):
        return redirect(f'/cookies/edit/{id}')
    Cookie_order.update_order(request.form)
    return redirect('/')

@app.route('/cookies/delete/<int:id>')
def delete(id):
    Cookie_order.delete({'id':id})
    return redirect('/')
