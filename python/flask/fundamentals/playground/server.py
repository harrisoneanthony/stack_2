from flask import Flask, render_template
app = Flask(__name__)

# http://127.0.0.1:5001

@app.route('/play')
def play_one():
    return render_template("playground.html", num=3, color="steelblue")

@app.route('/play/<int:num>')
def play_two(num):
    return render_template("playground.html", num=num, color="steelblue")

@app.route('/play/<int:num>/<string:color>')
def play_3(num,color):
    return render_template("playground.html", num=num, color=color)

if __name__ == "__main__":
    app.run(debug=True, port=5001)