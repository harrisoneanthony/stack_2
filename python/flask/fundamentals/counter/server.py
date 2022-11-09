from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key = 'this is a secret key'

@app.route('/')
def count_home():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/plus_two')
def plus_two():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def addnumber():
    session['count'] += (int(request.form['var_num'])-1)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug = True, port=5001)