import sqlite3

from flask import redirect


def Teacher(request):
    Teacher = request.form['Teacher']
    Rating = request.form['Rating']
    Comments = request.form['Comments']
    print("Teacher" + "\t" + Teacher + "\t" + "Comments" + "\t" + Rating + "\t" + "Rating" + "\t" + Comments)
    userinfo = [Teacher, Rating, Comments]
    conn = sqlite3.connect('user.db')
    # Creating a Cursor
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?,?,?)", userinfo)
    # Commit our command
    conn.commit()

    # close our connection
    conn.close()