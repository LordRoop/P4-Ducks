import sqlite3

from flask import redirect


def validate(request):
    user = request.form['user']
    password = request.form['user_pass']
    print("Username" + "\t" + user + "\t" + "Password" + "\t" + password + "\t" + "Email")
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