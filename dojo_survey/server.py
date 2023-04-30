from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "A secret key is without a lock..."


@app.route('/')
def index():
    print("Got index.")
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def submit():
    print("Post form received.")
    print(request.form)
    session['fn'] = request.form['first_name']
    session['fn'] = request.form['last_name']
    session['dojo'] = request.form['dojo_loc']
    session['fav'] = request.form['fav_lan']
    session['comments'] = request.form['comments']
    return redirect('/results')


@app.route('/results')
def results():
    return render_template('results.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
