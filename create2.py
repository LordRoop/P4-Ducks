import sqlite3

def createTable() :
    print ("In Create Table")
    conn = sqlite3.connect('teacher.db')
    # Creating a Cursor
    c = conn.cursor()
    c.execute("""CREATE TABLE users (
        teacher text ,
        Rate text ,
        Comment text ,
        
        PRIMARY KEY(user_id, user_email)
    )""")

    # Commit our command
    conn.commit()
    print("Table Created")
    #Close Connection
    conn.close


def writeDummyData():
    conn = sqlite3.connect('teacher.db')
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
    conn = sqlite3.connect('teacher.db')
    # Creating a Cursor
    c = conn.cursor()
    print("Getting Data")
    c.execute("SELECT * FROM users")
    items = c.fetchall()
    for item in items:
        print("Teacher" + "\t" + item[0] + "\t" + "Rating" + "\t" + item[1] + "\t" + "Comments" + "\t" + item[2])

    #Close Connection
    conn.close





