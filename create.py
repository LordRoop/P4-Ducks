import sqlite3


conn = sqlite3.connect('user.db')

# Creating a Cursor
c = conn.cursor()

many_users = [

    ('west', 'Yee', 'wes@gmail.com'),
    ('Navodit', 'Yee', 'Navodit@gmail.com'),
    ('Joe', 'Yee', 'joe@gmail.com'),
]



c.execute("SELECT * FROM users")

items = c.fetchall()

for item in items:
    print("Username" + "\t" + item[0] + "\t" + "Password" + "\t" + item[1] + "\t" + "Email" + "\t" + item[2])

print("Correct")
# Commit our command
conn.commit()

# close our connection
conn.close()
