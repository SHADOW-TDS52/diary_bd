import sqlite3 
con = sqlite3.connect('reminder.db')
with con:
    con.execute("""
        CREATE TABLE reminder (
            ID INTEGER PRIMARY KEY,
            date TEXT,
            event TEXT,
            time TEXT
        );
    """)
