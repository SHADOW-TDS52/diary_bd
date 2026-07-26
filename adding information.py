import sqlite3
def add_reminder(reminder_id: int, date: str, event: str, time: str) -> None:
    with sqlite3.connect('reminder.db') as con:
        con.execute(
            "INSERT INTO reminder (id, date, event, time) VALUES (?, ?, ?, ?);",
            (reminder_id, date, event, time),
        )
if __name__ == '__main__': 
    add_reminder(2, '2027-02-15', 'Конференция', '09:00:00')
