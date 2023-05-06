from flask import Flask, render_template, request, redirect
from users import User
app = Flask(__name__)
app.secret_key = "This is a secret key."


@app.route('/')
def index():
    return render_template('show_all.html', users=User.read_all())


@app.route('/create', methods=['POST'])
def add_user():
    User.create(request.form)
    return redirect('/')


@app.route('/add_user')
def create_user():
    return render_template('create.html')



if __name__ == '__main__':
    app.run(debug=True, port=8000)
