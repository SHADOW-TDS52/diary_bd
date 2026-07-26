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

# Удаляем таблицу
with con:
    con.execute("DROP TABLE reminder")

# подготавливаем запрос
sql = 'INSERT INTO marvel (ID, date, event, time) values(?, ?, ?, ?)'

# указываем данные для запроса
data = [
    (1, '26-07-2026', 'Первая версия ежедневника', '20:00'),
    (2, '03-08-2026', '???', '19:00-20:00'),
]

# добавляем с помощью множественного запроса все данные сразу
with con:
    con.executemany(sql, data)