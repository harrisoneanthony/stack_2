from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.burger import Burger

@app.route('/')
def index():
    return render_template('index.html')