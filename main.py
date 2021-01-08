import data
import  flask

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

@app.route('/art')
def art():
    return flask.render_template("art.html")

@app.route('/science')
def science():
    return flask.render_template("science.html")

@app.route('/elective')
def elective():
    return flask.render_template("elective.html")

@app.route('/history')
def history():
    return flask.render_template("history.html")


if __name__ == "__main__":
    app.run(debug=True, port=' 5001', host='127.0.0.1')
#Hi, Ak is here
