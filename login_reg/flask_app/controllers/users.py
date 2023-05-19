from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


# Home
@app.route('/')
def index_home():
    return render_template('index_home.html')


# Register
@app.route('/users/register', methods=['POST'])
def register_user():
    if not user.User.validate_register(request.form):
        return redirect('/')
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': hashed_pw
    }
    user_id = user.User.save_user(data)
    session['user_id'] = user_id
    return redirect('/users/dashboard')

# Login
@app.route('/users/login', methods=['POST'])
def login_user():
    one_user = user.User.get_one_user_by_email(request.form)
    if not one_user:
        flash('Invalid email address.', 'login')
        return redirect('/')
    check_hashed_pw = bcrypt.check_password_hash(one_user.password, request.form['password'])
    if not check_hashed_pw:
        flash('Invalid password.', 'login')
        return redirect('/')
    session['user_id'] = one_user.id
    return redirect('/users/dashboard')


# Dashboard
@app.route('/users/dashboard')
def dashboard():
    if 'user_id' not in session:
        redirect('/')
    data = {
        'id': session['user_id']
    }
    user_dash = user.User.get_one_user_by_id(data)
    return render_template('dashboard.html', user=user_dash)


# Logout
@app.route('/users/logout')
def logout_user():
    session.clear()
    return redirect('/')