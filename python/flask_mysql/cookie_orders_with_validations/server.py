from flask_app import app
from flask_app.controllers import cookie_controllers
from flask_app.models.cookie_models import Cookie_order

if __name__ == "__main__":
    app.run(debug = True, port=5001)