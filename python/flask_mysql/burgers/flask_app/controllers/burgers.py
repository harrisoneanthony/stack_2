from flask import render_template,redirect,request
from flask_app import app
from flask_app.models import burger, restaurant

@app.route('/')
def index():
    all_restaurants = restaurant.Restaurant.get_all()
    return render_template('index.html', all_restaurants = all_restaurants)

@app.route('/create/burger', methods = ["POST"])
def create():
    burger.Burger.save(request.form)
    return redirect(f'/show/burgers/{burger.Burger.save(request.form)}')

@app.route('/show/burger/<int:id>')
def show_one(id):
    data = {
        'id': id
    }
    return render_template("one_burger.html", burger = burger.Burger.get_one_burger(data))

@app.route('/burgers')
def show_all_burgers():
    return render_template('all_burgers.html', all_burgers=burger.Burger.get_all_burgers())

@app.route('/delete/<int:id>')
def delete(id):
    data ={
        'id': id
    }
    burger.Burger.delete(data)
    return redirect('/')