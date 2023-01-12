from flask import render_template,redirect,request,session
from flask import flash
from flask_app import app
from flask_app.models.login_and_registration_models import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    # Call the save @classmethod on User
    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    return redirect('/')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/login', methods=['POST'])
def login():
    # see if the user provided exists in the database
    data = {"email" : request.form["email"]}
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password", 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        #  if we get false after checking the password
        flash("Invalid Email/Password", 'login')
        return redirect('/')
    # if the passwrods matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    session['last_name'] = user_in_db.last_name
    # never renter on a post!
    return redirect('/user')

@app.route('/logout')
def logout():
    session['user_id'] = ''
    session['first_name'] = ''
    session['last_name'] = ''
    return redirect('/')