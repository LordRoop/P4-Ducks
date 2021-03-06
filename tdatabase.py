import sqlite3




def createTeachersTable():
    print("In createTeachersTable")
    conn = sqlite3.connect('tlist.db')
    # Creating a Cursor
    c = conn.cursor()
    c.execute("""CREATE TABLE teachers (
        teacher_id integer NOT NULL,
        teacher_name text NOT NULL,
        subject text NOT NULL,
        
        PRIMARY KEY(teacher_id)
    )""")
    # Commit our command
    conn.commit()
    print("Table Created")
    # Close Connection
    conn.close


def createRatingTable():
    print("In createRatingTable")
    conn = sqlite3.connect('tlist.db')
    # Creating a Cursor
    c = conn.cursor()
    print("Table created")
    c.execute("""CREATE TABLE rating (
        teacher_id integer NOT NULL,
        teacher_name text NOT NULL,
        user_id text NOT NULL,
        rating integer NOT NULL
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
                   ("Buehler Jo ", "Math"),
                   ("Jenkins Christopher", "Math"),
                   ("West Briana", "Math"),
                   ("Dafoe Stephanie", "English"),
                   ("Darcey Melissa", "English"),
                   ("Hall Trent", "English"),
                   ("Jenkin Cara", "English"),
                   ("Mansour Colleen", "English"),
                   ("Nevares Nick", "English"),
                   ("Nona Lubna", "English"),
                   ("Paulson Kelly", "English"),
                   ("Philyaw Jennifer", "English"),
                   ("Ross Rachel", "English"),
                   ("Weeg Robert", "English"),
                   ("West Ted", "English"),
                   ("James Kristen", "English"),
                   ("Christopher Robin", "English"),
                   ("Segovia Johnny", "History"),
                   ("Ayres Elizabeth", "History"),
                   ("Coats Scott", "History"),
                   ("Curry Neal", "History"),
                   ("Smith Chermaine", "History"),
                   ("Giffin Tasha", "History"),
                   ("Keller Kevin", "History"),
                   ("Roberts Jodi", "History"),
                   ("Simmons Kenneth", "History"),
                   ("Swanson Tom", "History"),
                   ("Volger Megan", "History"),
                   ("Smith Joan", "History"),
                   ("Mortenson John", "Elective"),
                   ("Titlow Louise", "Elective"),
                   ("Kitelinger Jennifer", "Elective"),
                   ("Askegreen Jason", "Elective"),
                   ("Coleman Patrick", "Elective"),
                   ("Wong Ruth ", "Elective"),
                   ("DeCaprio Lauren", "Elective"),
                   ("Aronen Heather", "Elective"),
                   ("Campillo John", "Elective"),
                   ("Barnett Ashley", "Science"),
                   ("Callicott Andrea", "Science"),
                   ("Cheskaty Juli", "Science"),
                   ("Craig Courtney", "Science"),
                   ("Eckman Kyle", "Science"),
                   ("Hannan Julie", "Science"),
                   ("Hendricks Jay", "Science"),
                   ("Liao Frank", "Science"),
                   ("Millman Ryan", "Science"),
                   ("Moulton Tyler", "Science"),
                   ("Ozuna Ken", "Science"),
                   ("Pytel Kimberly", "Science"),
                   ("Smedley Lisa", "Science"),
                   ("Alvarez Maria", "Language"),
                   ("Balderas Maritza", "Language"),
                   ("Lecakes-Jones Holly", "Language"),
                   ("Ruggiero Lauren", "Language"),
                   ("Strutton Aaron", "Language"),
                   ("DeAlba Ingrid", "Language"),
                   ("Velasco Leonardo", "Language"),
                   ("Tu Ryan", "Language"),
                   ("Embrey Rielly", "ENS"),
                   ("Hanover Dale", "ENS"),
                   ("McNeely Jake", "ENS"),
                   ("Mele Brianna", "ENS"),
                   ("Milanovich Suzanne", "ENS"),
                   ("Robinson Sona", "ENS"),


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
    print("Getting Data for:", subject)
    c.execute("SELECT * FROM teachers where subject = (?)", (subject,))
    items = c.fetchall()
    for item in items:
        print("teacher_id" + "\t" + str(item[0]) + "\t" + "teacher_name" + "\t" + item[1] + "\t" + "subject" + "\t" + item[2])

    # Close Connection
    conn.close
    return items

def getResultData(subject):

    conn = sqlite3.connect('tlist.db')
    # Creating a Cursor
    c = conn.cursor()
    print("Getting Data for:", subject)
    c.execute("SELECT teachers.teacher_id, teachers.teacher_name, teachers.subject, avg(rating.rating) FROM teachers, rating WHERE teachers.teacher_id = rating.teacher_id AND teachers.subject = ? GROUP BY teachers.teacher_id", (subject,))
    items = c.fetchall()
    for item in items:
        print("teacher_id" + "\t" + str(item[0]) + "\t" + "teacher_name" + "\t" + item[1] + "\t" + "average Rating" + "\t" + "{:.2f}".format(item[3]))

    # Close Connection
    conn.close
    return items



def resetTtable():
    conn= sqlite3.connect('tlist.db')
    c = conn.cursor()
    c.execute("DELETE FROM teachers")
    print("clear")
    conn.commit()
    conn.close()

def resetRatingTable():
    conn= sqlite3.connect('tlist.db')
    c = conn.cursor()
    c.execute("DELETE FROM rating")
    conn.commit()
    conn.close()

def deleteRatingTable():
    conn= sqlite3.connect('tlist.db')
    c = conn.cursor()
    c.execute("DROP TABLE rating")
    conn.commit()
    conn.close()

def writeRatingtoTable(teacherId, teacherName, userId, rating):

    conn = sqlite3.connect('tlist.db')
    # Creating a Cursor
    c = conn.cursor()
    print("writing star data for teacherName")

    row = [teacherId, teacherName, userId, rating]
    print ("Trying to update record")
    c.execute("UPDATE rating SET rating = ? WHERE user_id = ? AND teacher_id = ?", (rating, userId, teacherId))
    if c.rowcount == 0:
        print("Seems updating record failed. Trying to insert record")
        c.execute("INSERT INTO rating VALUES (?,?,?,?)", row)
    conn.commit()
    print("wrote in database ", row)

    # Get Teachers average rating
    item = c.execute("SELECT teacher_id, avg(rating), count(*) FROM rating where teacher_id = (?)", (teacherId,))
    data = c.fetchone()
    print("teacher_id" + "\t" + str(data[0]) + "\t" + "Average Rating" + "\t" + str(data[1]) + "\t" + "Number of Votes" + "\t" + str(data[2]))
    conn.close()

    return str(data[1])


def getRatingData():

    conn = sqlite3.connect('tlist.db')
    # Creating a Cursor
    c = conn.cursor()
    c.execute("SELECT * FROM rating")
    items = c.fetchall()
    for item in items:
        print("teacher_id" + "\t" + str(item[0]) + "\t" + "teacher_name" + "\t" + item[1] + "\t" + "user_Id" + "\t" + item[2] + "rating" + "\t" + item[3])

    # Close Connection
    conn.close
    return items