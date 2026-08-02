import sqlite3 

# открываем файл с базой данных
con = sqlite3.connect('reminder.db')

# создаём таблицу 
try:
    with con:
        # 2. Создаем таблицу. 
        # ВАЖНО: Добавляем AUTOINCREMENT и убираем явное указание ID при вставке
        con.execute("""
            CREATE TABLE IF NOT EXISTS reminder (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                event TEXT,
                time TEXT
            )
        """)
        
        # 3. Запрос БЕЗ колонки ID
        sql = 'INSERT INTO reminder (date, event, time) VALUES (?, ?, ?)'
        
        # 4. Данные БЕЗ ID
        data = [
            
        ]
        
        con.executemany(sql, data)
        print("Данные успешно добавлены!")

except sqlite3.IntegrityError as e:
    print(f"Ошибка целостности данных: {e}")
except sqlite3.Error as e:
    print(f"Произошла ошибка: {e}")
finally:
    con.close()

def add_remind(date, event, time):
    """
    Добавляет одну запись (дата, событие, время) в таблицу reminder.
    Возвращает ID вставленной строки или None при ошибке.
    ID генерируется автоматически (AUTOINCREMENT).
    """
    conn = sqlite3.connect('reminder.db')
    try:
        cur = conn.cursor()
        
        # ИСПРАВЛЕНИЕ: Убрали ID из списка колонок и из значений.
        # Теперь база сама присвоит номер.
        cur.execute(
            "INSERT INTO reminder (date, event, time) VALUES (?, ?, ?)",
            (date, event, time)
        )
        
        conn.commit()
        
        # lastrowid теперь гарантированно вернёт новый ID
        return cur.lastrowid
        
    except sqlite3.Error as e:
        print("Ошибка при вставке:", e)
        conn.rollback()
        return None
    finally:
        conn.close()

def update_price(record_id, new_date, new_event, new_time):
    """
    Обновляет напоминание для записи с указанным id.
    Возвращает True при успехе, False при ошибке.
    """
    conn = sqlite3.connect("reminder.db")
    try:
        cur = conn.cursor()
        # ИСПРАВЛЕНИЕ 1: таблица reminder вместо prices
        # ИСПРАВЛЕНИЕ 2: добавлены запятые между полями в SET
        cur.execute(
            "UPDATE reminder SET date = ?, event = ?, time = ? WHERE ID = ?",
            (new_date, new_event, new_time, record_id)
        )
        conn.commit()
        
        # rowcount вернет 1, если запись обновлена, или 0, если такого ID не было
        return cur.rowcount > 0
        
    except sqlite3.Error as e:
        print("Ошибка при обновлении:", e)
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_remind_by_id(record_id):
    """
    Удаляет запись из таблицы reminder по id.
    Возвращает True, если строка была удалена, иначе False.
    """
    conn = sqlite3.connect('reminder.db')
    try:
        cur = conn.cursor()
        # ИСПРАВЛЕНИЕ 1: таблица reminder вместо prices
        # ИСПРАВЛЕНИЕ 2: (record_id,) — запятая обязательна для кортежа
        cur.execute(
            "DELETE FROM reminder WHERE ID = ?",
            (record_id,)
        )
        conn.commit()
        
        # rowcount вернет 1, если запись удалена, или 0, если такого ID не было
        return cur.rowcount > 0
        
    except sqlite3.Error as e:
        print("Ошибка при удалении:", e)
        conn.rollback()
        return False
    finally:
        conn.close()


# добавляем с помощью множественного запроса все данные сразу
con = sqlite3.connect('reminder.db')
with con:
    con.executemany(sql, data)

#введи ниже то что ты хочешь сделать:
