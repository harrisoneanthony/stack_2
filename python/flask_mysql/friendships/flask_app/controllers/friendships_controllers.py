from flask import render_template,redirect,request,session
from flask_app import app
from flask_app.models.friendships_models import Friendship


@app.route('/friendship/create', methods=['POST'])
def create_friendship():
    Friendship.create_friendship(request.form)
    print(Friendship.create_friendship(request.form))
    return redirect('/')