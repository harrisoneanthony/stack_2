from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") # / means http://127.0.0.1:5001/
def home():
    return render_template("home.html")

@app.route("/say/hello/<name>")
def say_hello(name):
    print(name)
    return render_template("say_hello.html", name = name)


if __name__ == "__main__":
    app.run(debug=True, port=5001)