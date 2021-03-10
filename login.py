import sqlite3

from flask import redirect, render_template, session
from create import checkLogin


def validate(request):
    if checkLogin(request) == 1:
        user = request.form['user']
        session['username'] = user
        return redirect('/')

    else:
        return render_template("login.html", error='UserId or password Incorrect')
