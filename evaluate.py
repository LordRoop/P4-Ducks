import sqlite3
import sqlite3
#Will make another table
def createTable2() :
    print ("In Create Table")
    conn = sqlite3.connect('teacher.db')
    # Creating a Cursor
    c = conn.cursor()
    c.execute("""CREATE TABLE users (
        teacher text ,
        Rate text ,
        Comment text ,
        
       
    )""")

    # Commit our command
    conn.commit()
    print("Table Created")
    #Close Connection
    conn.close



def getData2():
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
    #hi




