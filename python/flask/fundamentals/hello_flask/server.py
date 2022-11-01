from flask import Flask
app = Flask(__name__)

@app.route("/") # / means http://127.0.0.1:5001/
def home():
    return "Trick or Treat"



if __name__ == "__main__":
    app.run(debug=True, port=5001)