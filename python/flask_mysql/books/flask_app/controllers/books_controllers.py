from flask import render_template,redirect,request
from flask_app import app
from flask_app.models import authors_models, books_models

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def home():
    return render_template('authors.html')
