from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)

app.secret_key = "dojo survey secret key"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def result():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favorite_language'] = request.form['language']
    session['comment'] = request.form['comment']
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug = True, port = 5001)