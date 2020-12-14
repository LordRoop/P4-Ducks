import data
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", projects=data.setup(), data=data.runtime())


@app.route('/projects')
def projects():
    return render_template("projects.html")


@app.route('/journals')
def journals():
    return render_template("journals.html")


@app.route('/pedro')
def pedro():
    return render_template("pedro.html")


@app.route('/roop')
def roop():
    return render_template("roop.html")


@app.route('/arul')
def arul():
    return render_template("arul.html")


@app.route('/manuel')
def manuel():
    return render_template("manuel.html")


@app.route('/colin')
def colin():
    return render_template("colin.html")

if __name__ == "__main__":
    app.run(debug=True, port=' 5000', host='192.168.86.51')
