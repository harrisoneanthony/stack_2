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
    return redirect('/burgers')


@app.route('/burgers')
def show_all_burgers():
    return render_template('all_burgers.html', all_burgers=burger.Burger.get_all_burgers())