from flask_app import app
from flask_app.controllers import login_and_registration_controllers
from flask_app.models.login_and_registration_models import User

if __name__ == "__main__":
    app.run(debug = True, port=5001)