import sqlite3

from flask import redirect


def newuser(request):
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