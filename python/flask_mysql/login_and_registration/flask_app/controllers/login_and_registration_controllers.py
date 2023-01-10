from flask import render_template,redirect,request,session
from flask_app import app
from flask_app.models.login_and_registration_models import User


@app.route('/')
def index():
    return render_template('index.html')
