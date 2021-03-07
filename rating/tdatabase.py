import sqlite3


def createTable():
    print("In Create Table")
    conn = sqlite3.connect('tlist.db')
    # Creating a Cursor
    c = conn.cursor()
    c.execute("""CREATE TABLE teachers (
        teacher_id integer NOT NULL,
        teacher_name text NOT NULL,
        subject text NOT NULL,
        
        PRIMARY KEY(teacher_id)
    )""")
    print("Table created")
    c.execute("""CREATE TABLE rating (
        teacher_id integer NOT NULL,
        teacher_name text NOT NULL,
        user_id text NOT NULL,
        rating text NOT NULL
       )""")
    # Commit our command
    conn.commit()
    print("Table Created")
    # Close Connection
    conn.close


def populateTeachers():
    conn = sqlite3.connect('tlist.db')
    # Creating a Cursor
    c = conn.cursor()
    print("writing dummy data")
    teacherList = [("Krenz James", "Math"),
                   ("Lanzi Sheaman Mitchelle", "Math"),
                   ("Nydam Cherrie", "Math"),
                   ("Lafferty James", "Math"),
                   ("Ziegler Mark", "Math"),
                   ("Bassett James", "Math"),
                   ("Joel Bernabeo", "Math"),
                   ("Ashton Arlene", "Math"),
                   ("Derksen Michelle", "Math"),
                   ("Edelstein Scott", "Math"),
                   ("Friedemann Erika", "Math"),
                   ("Heinen Cara", "Math"),
                   ("Hightower Reanna", "Math"),
                   ("Huang Yali", "Math"),
                   ("Titlow Louise", "Math"),
                   ("West Briana", "Math"),
                   ("Dafoe Stephanie", "English"),
                   ("Darcey Melissa", "English"),
                   ("Hall Trent", "English")


                   ]

    for teacher in teacherList:
        c.execute("INSERT INTO teachers(teacher_name, subject) VALUES (?,?)", teacher)

    print('Data added')
    # Commit our command
    conn.commit()
    # Close Connection
    conn.close


def getData(subject):

    conn = sqlite3.connect('tlist.db')
    # Creating a Cursor
    c = conn.cursor()
    print("Getting Data")
    c.execute("SELECT * FROM teachers where subject = (?)", (subject,))
    items = c.fetchall()
    for item in items:
        print("teacher_id" + "\t" + str(item[0]) + "\t" + "teacher_name" + "\t" + item[1] + "\t" + "subject" + "\t" + item[2])

    # Close Connection
    conn.close

def resetTtable():
    conn= sqlite3.connect('tlist.db')
    c = conn.cursor()
    c.execute("DELETE FROM teachers")
    conn.close()


def getTeachers():
    getData("English")