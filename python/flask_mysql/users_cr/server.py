from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)


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
    User.save(request.form)
    return redirect('/users')


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

@app.route("/user/update", methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/delete/<int:id>')
def delete(id):
    data ={
        'id': id
    }
    User.delete(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug = True, port=5001)