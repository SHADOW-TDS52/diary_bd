import sqlite3 

# открываем файл с базой данных
con = sqlite3.connect('reminder.db')

# создаём таблицу 
with con:
    con.execute("""
        CREATE TABLE reminder (
            ID INTEGER PRIMARY KEY,
            date TEXT,
            event TEXT,
            time TEXT
        );
    """)