import data
import flask
from flask import request, redirect
import sqlite3
import json as j
import requests as r


app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template("home.html", projects=data.setup(), data=data.runtime())

@app.route('/test')
def test():
    return flask.render_template("test.html")


@app.route('/rfg')
def rfg():
    x = r.get("https://uselessfacts.jsph.pl/random.json?language=en")
    data = j.loads(x.content)
    fact = data.get("text")
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


@app.route('/signup', methods=['POST'])
def signup():
    user = request.form['user']
    password = request.form['user_pass']
    mail = request.form['mail']
    print("Username" + "\t" + user + "\t" + "Password" + "\t" + password + "\t" + "Email" + "\t" + mail)
    userinfo = [user, password, mail]
    conn = sqlite3.connect('user.db')
    # Creating a Cursor
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?,?,?)", userinfo)
    # Commit our command
    conn.commit()

    # close our connection
    conn.close()

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=' 5007', host='127.0.0.1')
    #ak is here hi
