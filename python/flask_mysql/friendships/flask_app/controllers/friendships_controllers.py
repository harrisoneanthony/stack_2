from flask import render_template,redirect,request,session, flash
from flask_app import app
from flask_app.models.friendships_models import Friendship


@app.route('/friendship/create', methods=['POST'])
def create_friendship():
    if not Friendship.friendship_checker({'user_id': request.form['user_id'], 'friendship_id': request.form['friendship_id']}):
        flash('Friendship already exists!')
        return redirect ('/')
    Friendship.create_friendship(request.form)
    return redirect('/')