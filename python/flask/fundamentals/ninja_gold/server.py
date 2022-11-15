from flask import Flask, render_template, session, redirect, request
import random
import math
import datetime

app = Flask(__name__)
app.secret_key = 'golden'

def rand_gold(num1,num2):
    gold=random.randint(num1,num2)
    return gold

@app.route('/')
def home():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = ''
    return render_template('index.html')

@app.route('/process_money', methods = ['POST'])
def process_money():
    if request.form['building'] == "farm":
        mined_gold = rand_gold(10,20)
        session['gold'] += mined_gold
    elif request.form['building'] == "cave":
        mined_gold = rand_gold(5,10)
        session['gold'] += mined_gold
    elif request.form['building'] == "house":
        mined_gold = rand_gold(2,5)
        session['gold'] += mined_gold
    else:
        mined_gold = rand_gold(-50,50)
        session['gold'] += mined_gold
    session['activity'] += "Earned " + str(mined_gold) + " gold from the " + request.form['building']
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True, port=5001)