import datetime
from pathlib import Path
import sqlite3
from database import db_conn, create_table_busy_intervals

# BLOCK A

create_table_busy_intervals()

# wip
def check_busy_intervals():
    conn = db_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT busy_from, busy_to FROM busy_intervals")
    current_intervals = cursor.fetchall()

    busy_from = cursor.execute("SELECT")
    busy_to = input("Until what time are you busy? (xx:xx)")

    print(f"Here are ")

    if not current_intervals:
        busy_from = input("From what time are you busy? (xx:xx)")
        busy_to = input("Until what time are you busy? (xx:xx)")

        cursor.execute("INSERT INTO busy_intervals (busy_from, busy_to) VALUES (?, ?)", (busy_from, busy_to))

        conn.commit()
        
        return f"Your busy interval has been set to from {busy_from} until {busy_to}"

check_busy_intervals()
