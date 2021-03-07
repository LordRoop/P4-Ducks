import data
import flask
from flask import request, redirect
from register import newuser
from login import validate
import requests
from create import updatepwd, delete



app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template("home.html", projects=data.setup(), data=data.runtime())

@app.route('/profile')
def profile():
    return flask.render_template("profile.html")


@app.route('/rfg', methods=['GET', 'POST'])
def rfg():
    url = 'https://uselessfacts.jsph.pl/random.json?language=en'
    response = requests.get(url)
    fact = response.json()['text']
    return flask.render_template("rfg.html", fact=fact)


@app.route('/math')
def math():
    return flask.render_template("math.html")


@app.route('/english')
def english():
    return flask.render_template("english.html")


@app.route('/language')
def language():
    return flask.render_template("language.html")


@app.route('/science')
def science():
    return flask.render_template("science.html")


@app.route('/elective')
def elective():
    return flask.render_template("elective.html")


@app.route('/history')
def history():
    return flask.render_template("history.html")


@app.route('/ens')
def ens():
    return flask.render_template("ens.html")


@app.route('/login')
def login():
    return flask.render_template("login.html")


@app.route('/registration')
def registration():
    print("I am in registraeldskfl")
    return flask.render_template("registration.html")


@app.route('/Evaluate')
def exaluate():
    return flask.render_template("Evaluate.html")

@app.route('/meme')
def meme():
    return flask.render_template("meme.html")

@app.route('/whoami')
def whoami():
    return flask.render_template("whoami.html")

@app.route('/signup', methods=['POST'])
def signup(): return newuser(request)


@app.route('/checkuser', methods=['POST'])
def checkuser(): return validate(request)

@app.route('/changepwd', methods=['POST'])
def changepwd():
    return flask.render_template("profile.html", error=updatepwd(request))

@app.route('/deleteAccount', methods=['POST'])
def deleteAccount():
    return flask.render_template("profile.html", error=delete(request))

@app.route('/star')
def star():
    return flask.render_template("star.html")



if __name__ == "__main__":
    app.run(debug=True, port=' 5006', host='127.0.0.1')

