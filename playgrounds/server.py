from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def index():
    return render_template('index.html', boxes=3)


@app.route("/play/<int:num_of_box>")
def return_num(num_of_box):
    return render_template("index.html", boxes=num_of_box)


@app.route("/play/<int:num_of_box>/<string:change_color>")
def return_num_color(num_of_box, change_color):
    return render_template("index.html", boxes=num_of_box, color=change_color)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
