import sqlite3

#from flask import session


def createTable() :
    print ("In Create Table")
    conn = sqlite3.connect('user.db')
    # Creating a Cursor
    c = conn.cursor()
    c.execute("""CREATE TABLE users (
        user_id text NOT NULL,
        user_pwd text NOT NULL,
        user_email text NOT NULL,
        
        PRIMARY KEY(user_id, user_email)
    )""")

    # Commit our command
    conn.commit()
    print("Table Created")
    #Close Connection
    conn.close


def writeDummyData():
    conn = sqlite3.connect('user.db')
    # Creating a Cursor
    c = conn.cursor()
    print ("writing dummy data")
    c.execute("INSERT INTO users VALUES ('navo','navopass','navo@navo.com')")
    print('Data added')
    # Commit our command
    conn.commit()
    #Close Connection
    conn.close

def getData():
    conn = sqlite3.connect('user.db')
    # Creating a Cursor
    c = conn.cursor()
    print("Getting Data")
    c.execute("SELECT * FROM users")
    items = c.fetchall()
    for item in items:
       print("user_id" + "\t" + item[0] + "\t" + "user_pwd" + "\t" + item[1] + "\t" + "user_email" + "\t" + item[2])

    #Close Connection
    conn.close


def checkLogin(request):
    user = request.form['user']
    password = request.form['user_pass']
    print("Username" + "\t" + user + "\t" + "Password" + "\t" + password)
    conn = sqlite3.connect('user.db')
    # Creating a Cursor
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE user_id=?", (user,))
        row = c.fetchall()
        print(row)
        print(row[0][1])
        if row[0][1] == password:
            print("success")
        else:
            print("failed")
            return 0


    # Commit our command
    #conn.commit()
    except IndexError as e:
        print(e)
        print("wrong username")
        return 0
    # close our connection
    conn.close()

    return 1


def updatepwd(request):

    if checkLogin(request) == 1:
        user = request.form['user']
        password = request.form['user_pass']
        npassword = request.form['user_pass1']
        ncpassword = request.form['user_pass2']

        if npassword != ncpassword:
            return "New password does not match"

        else:
            conn = sqlite3.connect('user.db')
            c = conn.cursor()
            c.execute("UPDATE users SET user_pwd = ? WHERE user_id = ?", (npassword, user))
            conn.commit()
            conn.close()
            return "Password Updated"
    else:
        return "Username or Password incorrect"

def delete(request):

    if checkLogin(request) == 1:
        user = request.form['user']
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE user_id = ?", (user,))
        conn.commit()
        conn.close()
        return 1


    else:
        return 0

