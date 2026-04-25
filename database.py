import sqlite3

def db_conn():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    
    return conn

def create_table_busy_intervals():
    conn = db_conn()
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS busy_intervals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    busy_from TEXT,
                    busy_to TEXT,
                    report_time TEXT,
                    whitelist TEXT
                   )""")
    
    conn.commit()
    conn.close()

