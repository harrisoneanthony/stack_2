from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") # / means http://127.0.0.1:5001
def index():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<string:name>")
def say_name(name):
    return f"Hi, {name.capitalize()}!"

@app.route("/repeat/<int:num>/<string:word>")
def repeat(num, word):
    output = ''
    for i in range(0,num):
        output += f'<p>{word}</p>'
    return output

if __name__ == "__main__":
    app.run(debug=True, port=5001)