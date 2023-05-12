from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import ninja, dojo


@app.route('/ninja/new')
def new_ninja():
    all_dojos = dojo.Dojo.display_all()
    return render_template('create_ninja.html', all_dojos=all_dojos)


@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    ninja_id = request.form['dojo_id']
    print(request.form)
    ninja.Ninja.save(request.form)
    return redirect (f'/dojo/display/{ninja_id}')