from users_cr import app
from users_cr.controllers import users

if __name__ == "__main__":
    app.run(debug = True, port=5001)