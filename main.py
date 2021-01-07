import data
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", projects=data.setup(), data=data.runtime())


@app.route('/math')
def math():
    return render_template("math.html")

@app.route('/english')
def english():
    return render_template("english.html")

@app.route('/arts')
def arts():
    return render_template("arts.html")

@app.route('/science')
def science():
    return render_template("science.html")

@app.route('/electives')
def electives():
    return render_template("electives.html")



if __name__ == "__main__":
    app.run(debug=True, port=' 5000', host='127.0.0.1')
