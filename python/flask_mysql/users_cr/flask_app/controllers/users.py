from flask import render_template,redirect,request,session
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect("/users")

@app.route('/users')
def users():
    return render_template("read_all.html", all_users = User.get_all())

@app.route('/user/new')
def add_user():
    return render_template("new_user.html")

@app.route('/user/create', methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/user/new')
    return redirect(f'/user/show/{User.save(request.form)}')


@app.route("/user/edit/<int:id>")
def edit(id):
    data = {
        "id":id
    }
    return render_template('edit.html', user=User.get_one(data))

@app.route('/user/show/<int:id>')
def get_one(id):
    data = {
        "id":id
    }
    return render_template("read_one.html", user=User.get_one(data))

@app.route("/user/update/<int:id>", methods=['POST'])
def update(id):
    User.update(request.form)
    return redirect(f'/user/show/{id}')

@app.route('/user/delete/<int:id>')
def delete(id):
    data ={
        'id': id
    }
    User.delete(data)
    return redirect('/users')
