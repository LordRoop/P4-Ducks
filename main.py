import data
import flask
from flask import request, redirect, session
from register import newuser
from login import validate
import requests
import json
from create import updatepwd, delete
from tdatabase import getData, writeRatingtoTable, getResultData

app = flask.Flask(__name__)
app.secret_key = 'mySecretKey'

@app.route('/')
def home():

    if 'username' in session:
        return flask.render_template("home.html", projects=data.setup(), data=data.runtime())
    else:
        return flask.render_template("login.html")


@app.route('/result')
def result():
    subject = request.args.get("subject")
    if (subject != None):
        items = getResultData(subject)
        json_str = json.dumps(items)
        return flask.render_template("ratingResult.html", teacherList=json_str)
    else:
        return flask.render_template("result.html")


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
    error = delete(request)
    if error == 1:
        session.pop('username')
        errorMsg = "Account Deleted"
    else:
        errorMsg = "UserName or Pwd not correct"
    return flask.render_template("profile.html", error=errorMsg)

@app.route('/signOut', methods=['POST'])
def signOut():
    session.pop('username', None)
    return flask.render_template("login.html")

@app.route('/star')
def star():
    return flask.render_template("star.html")

@app.route('/news')
def news():
    #twitter embed api url
    urldnhs = "https://publish.twitter.com/oembed?url=https://twitter.com/dnhsnighthawks"
    urlpoway = "https://publish.twitter.com/oembed?url=https://twitter.com/powayunified"
    responsednhs = requests.get(urldnhs)
    responsepoway = requests.get(urlpoway)
    #set url value in json to variable
    jsonurldnhs = responsednhs.json()['url']
    jsonurlpoway = responsepoway.json()['url']
    return flask.render_template("news.html", jsonurldnhs=jsonurldnhs, jsonurlpoway=jsonurlpoway)

@app.route('/teachers', methods=['GET'])
def getTeachers():
    subject = request.args.get("subject")
    items = getData(subject)
    json_str = json.dumps(items)
    return flask.render_template("rating.html", teacherList=json_str)

@app.route('/submitRating', methods=['POST'])
def saveRating():
    teacherID = request.args.get("teacherId")
    teacherName = request.args.get("teacherName")
    teacherRating = request.args.get("rating")
    userId = session.get("username")
    result = (writeRatingtoTable(int(teacherID), teacherName, userId, int(teacherRating)))
    return flask.render_template("rating.html")


if __name__ == "__main__":
    app.run(debug=True, port=' 5006', host='127.0.0.1')

