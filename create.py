import sqlite3

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
       print("Username" + "\t" + item[0] + "\t" + "Password" + "\t" + item[1] + "\t" + "Email" + "\t" + item[2])

    #Close Connection
    conn.close





