import sqlite3
def update_reminder(reminder_id: int, date: str, event: str, time: str) -> None:
    with sqlite3.connect('reminder.db') as con:
        con.execute(
            "UPDATE reminder SET date = ?, event = ?, time = ? WHERE id = ?;",
            (date, event, time, reminder_id),
        )
if __name__ == '__main__':
    update_reminder(2, '2027-02-16', 'Встреча с клиентом', '14:00:00')
