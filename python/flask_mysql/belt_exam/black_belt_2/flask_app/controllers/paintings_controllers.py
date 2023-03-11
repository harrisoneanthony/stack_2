from flask import render_template,redirect,request,session
from flask import flash
from flask_app import app
from flask_app.models.paintings_models import Painting
from flask_app.controllers import users_controllers

@app.route('/create', methods=['POST'])
def add_painting():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'title': request.form['title'],
        'description': request.form['description'],
        'price': request.form['price'],
        'quantity': request.form['quantity'],
        'user_id': session['user_id']
    }
    if not Painting.valdiate_painting(data):
        return redirect('/new')
    Painting.add_painting(data)
    return redirect('/paintings')

@app.route('/delete/<int:id>')
def delete(id):
    # if 'users_id' not in session:
    #     return redirect('/')
    data = {
        'id': id
    }
    Painting.delete(data)
    return redirect('/paintings')

@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id':id
    }
    return render_template('edit.html', painting = Painting.get_one_painting(data))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if 'user_id' not in session:
        return redirect('/')
    if not Painting.valdiate_painting(request.form):
        return redirect(f'/edit/{id}')
    data = {
        'id': id
    }
    Painting.update(request.form)
    return redirect('/paintings')

@app.route('/view/<int:id>')
def show_painting(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id':id
    }
    painting = Painting.get_one_painting(data)
    number_sold = Painting.get_purchased_paintings(data)
    return render_template('view.html', painting = painting, number_sold=number_sold)