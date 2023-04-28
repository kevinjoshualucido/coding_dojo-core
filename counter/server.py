from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'This is my key.'


@app.route('/')
def index():
    # refresh page or 'add one' increments session visits +1
    print('Get Index')
    if 'talker' in session:
        session['talker'] += 1
    else:
        print('This is your first session!')
        session['talker'] = 1
    return render_template('index.html')


@app.route('/reset')
def delete():
    session.clear()
    return redirect('/')


@app.route('/add_two')
def count_by_two():
    session['talker'] += 1
    return redirect('/')
# Since I'm returning to the 'index' route, it will automatically +1, so 'add_two' route will only have another +1 counter which goes on top of the redirect, making the counter a +2.
# I made my counter +1 because I noticed that if my counter was +2 and I pressed my add two button while returning a redirect, it would add 3. Or if I kept on refreshing the page after adding two, it would continuously keep adding two until I pressed the reset or add one button.


@app.route('/custom_num', methods=['POST'])
def custom_increment():
    session['talker'] += (int(request.form['custom_num']) - 1)
    # Subtracted by 1 to basically cancel out the +1 that will happen when redirecting back to the 'index' route.
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
