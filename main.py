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




if __name__ == "__main__":
    app.run(debug=True, port=' 5000', host='127.0.0.1')
