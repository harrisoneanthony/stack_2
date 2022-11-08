from flask import Flask, render_template, session, redirect, request
from data import dinos

app = Flask(__name__)
app.secret_key = "testing"

# render page
@app.route('/')
def index():
    return render_template('index.html')

# redirect (adding user to session)
@app.route('/user/create/', methods=['POST'])
def createUser():
    session['fullName'] = request.form['fullName'] # take what is coming from the form and put it into session
    return redirect('/dashboard')

# render page
@app.route('/dashboard')
def dashboard():
    print("User in session", session['fullName'])
    theUser = session['fullName']
    return render_template('dashboard.html', theDinos=dinos, user=theUser)

# render page
@app.route('/dino/<int:dino_id>/view')
def view_dino(dino_id):
    theUser = session['fullName']
    return render_template('viewDino', dino=dinos[dino_id-1], user=theUser)

if __name__=='__main__':
    app.run(debug=True, port=5001)