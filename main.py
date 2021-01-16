import data
import flask

app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template("home.html", projects=data.setup(), data=data.runtime())


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
    return flask.render_template("registration.html")

@app.route('/Evaluate')
def exaluate():
    return flask.render_template("Evaluate.html")


if __name__ == "__main__":
    app.run(debug=True, port=' 5007', host='127.0.0.1')

