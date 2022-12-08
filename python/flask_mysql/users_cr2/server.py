from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)

@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)

@app.route("/user/new")
def new_user():
    return render_template('create.html')

@app.route("/user/create", methods=["POST"])
def create():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.save(data)
    return ('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)