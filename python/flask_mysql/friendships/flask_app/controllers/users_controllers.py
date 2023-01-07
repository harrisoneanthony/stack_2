from flask import render_template,redirect,request,session
from flask_app import app
from flask_app.models.users_models import User

@app.route('/')
def index():
    return redirect("/friendships")

@app.route('/friendships')
def users():
    all_friends = User.get_all_friendships()
    return render_template("index.html", all_users = User.get_all(), all_friends = all_friends)

@app.route('/user/create', methods=['POST'])
def create_user():
    User.save(request.form)
    return redirect('/')
