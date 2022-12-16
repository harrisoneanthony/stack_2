from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html', dojos = dojo.Dojo.get_all())

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')

# add app route to edit page
@app.route('/ninja/edit/<int:id>')
def edit_ninja(id):
    data = {
        "id": id
    }
    print(ninja.Ninja.get_one_ninja(data))
    return render_template('edit.html', one_ninja = ninja.Ninja.get_one_ninja(data))

@app.route("/ninja/delete/<int:ninja_id>/<int:dojo_id>")
def delete(ninja_id, dojo_id):
    data = {
        'id': ninja_id
    }
    ninja.Ninja.delete(data)
    return redirect(f'/dojo/{dojo_id}')

@app.route("/ninja/update/<int:id>", methods=['POST'])
def update(id):
    ninja.Ninja.update(request.form)
    dojo_id = request.form['dojo_id']
    return redirect(f'/dojo/{dojo_id}')
