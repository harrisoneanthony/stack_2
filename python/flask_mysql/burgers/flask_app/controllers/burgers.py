from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.burger import Burger

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/burgers')
def all_burgers():
    return render_template('all_burgers.html')

@app.route('/create/burger', methods = ["POST"])
def create():
    data = {
        "name": request.form["name"],
        "bun": request.form["bun"],
        "meat": request.form["meat"],
        "calories": request.form["calories"],
        "restaurant": request.form["restaurant_id"],

    }
    return redirect('/burgers', data = data)