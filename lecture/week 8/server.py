from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'I love pizza'
import random
import math

def random_gems(num1,num2):
    gems = random.randint(num1,num2)
    return gems        


@app.route('/')
def index():
    if 'gems' not in session:
        session['gems'] = 0
    return render_template('index.html')

@app.route('/process_gems', methods=['POST'])
def process_gems():
    if request.form['mines'] == 'sapphire':
        mined_gems = random_gems(5,10)
        session['gems'] += mined_gems
        print(session['gems'])
    if request.form['mines'] == 'ruby':
        mined_gems = random_gems(15,20)
        session['gems'] += mined_gems
    if request.form['mines'] == 'diamond':
        mined_gems = random_gems(2,5)
        session['gems'] += mined_gems
    if request.form['mines'] == 'emerald':
        mined_gems = random_gems(-50,50)
        if mined_gems < 0:
            print("you had a cave in, run!")
        session['gems'] += mined_gems
    return redirect('/')


if __name__ == "__main__":
    app.run(debug = True, port = 5001)