from flask import Flask, render_template, session
app = Flask(__name__)

app.secret_key = "dojo survey secret key"

@app.route('/')
def homte():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug = True, port = 5001)