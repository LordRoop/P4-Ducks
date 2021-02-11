import sqlite3

from flask import redirect , render_template
from create import checkLogin

def validate(request):
    if checkLogin(request) == 1:
        return redirect('/')
    else:
        return render_template("login.html", error='UserId or password Incorrect')

