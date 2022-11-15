from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = 'golden'

@app.route('/')
def home():
    if 'gold' not in session:
        session['gold'] = 0
    return render_template('index.html')

@app.route('/process_money', methods = ['POST'])
def process_money():
    if request.form['building'] == "farm":
        session['gold'] += random.randint(10,20)
    elif request.form['building'] == "cave":
        session['gold'] += random.randint(5,10)
    elif request.form['building'] == "house":
        session['gold'] += random.randint(2,5)
    else:
        session['gold'] += random.randint(-50,50)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True, port=5001)