from flask import Flask, render_template, session, request, redirect
import random
from data import leader_board

app = Flask (__name__)
app.secret_key = "Can you guess what number I'm thinking of?"


@app.route('/')
def home():
    if 'rand_num' not in session:
        session['rand_num'] = random.randint(1,100)
    if "count" not in session:
        session["count"] = 0
    print(session['rand_num'])
    return render_template('index.html')

@app.route('/leader')
def leaderboard():
    return render_template('leaderboard.html', leader_board=leader_board)

@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['num_guess']) > int(session["rand_num"]):
        session['result'] = "too high! try again"
        session['count'] += 1
        return redirect('/')
    elif int(request.form['num_guess']) < int(session["rand_num"]):
        session['result'] = "too low! try again"
        session['count'] += 1
        return redirect('/')
    else:
        session['result'] = "correct!"
        session['count'] += 1
        return redirect('/')

@app.route('/leaderboard', methods=['POST'])
def addtoleaderboard():
    leader_board.append([request.form['leaderboard_name'], session['count']])
    print(leader_board)
    return redirect('/leader')

@app.route('/reset')
def reset():
    session.clear()
    return redirect ('/')



if __name__ == "__main__":
    app.run(debug = True, port = 5001)