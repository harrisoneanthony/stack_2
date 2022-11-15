from flask import Flask, render_template, session, redirect, request
import random
from datetime import datetime

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
        session['activity'] = []
    if 'count' not in session:
        session['count'] = 0

    return render_template('index.html')

@app.route('/process_money', methods = ['POST'])
def process_money():
    if request.form['building'] == "farm":
        mined_gold = rand_gold(10,20)
        if mined_gold < 0:
            color = "red"
        else: color = "green"
        session['gold'] += mined_gold
    elif request.form['building'] == "cave":
        mined_gold = rand_gold(5,10)
        if mined_gold < 0:
            color = "red"
        else: color = "green"
        session['gold'] += mined_gold
    elif request.form['building'] == "house":
        mined_gold = rand_gold(2,5)
        if mined_gold < 0:
            color = "red"
        else: color = "green"
        session['gold'] += mined_gold
    else:
        mined_gold = rand_gold(-50,50)
        session['gold'] += mined_gold
        if mined_gold < 0:
            color = "red"
        else: color = "green"
    session['activity'].insert(0,[f"Earned {mined_gold} gold from the {request.form['building']} {datetime.now().strftime('%Y/%m/%d %I:%M %p')}", color]) 
    print(color)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True, port=5001)