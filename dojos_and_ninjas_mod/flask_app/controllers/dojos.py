from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    all_dojos = Dojo.display_all()
    return render_template('dojo_index.html', all_dojos=all_dojos)


@app.route('/dojo/display/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {'id': dojo_id}
    one_dojo = Dojo.display_one(data)
    return render_template('show_dojo.html', one_dojo=one_dojo)


@app.route('/dojo/create', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/')