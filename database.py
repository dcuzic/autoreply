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
                    busy_to TEXT
                   )""")
    
    conn.commit()
    conn.close()

def create_table_whitelist():
    conn = db_conn()
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS whitelist (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name
                   )""")
    
    conn.commit()
    conn.close()

def create_table_report_time():
    conn = db_conn()
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS report_time (
                   time TEXT
                   )""")
    
    conn.commit()
    conn.close()

def create_table_messages():
    conn = db_conn()
    cursor = conn.cursor()

    cursor.execute(""" 
                   CREATE TABLE IF NOT EXISTS messages (
                   message_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   message TEXT
                   )""")
    
    conn.commit()
    conn.close()

def create_table_incoming():
    conn = db_conn()
    cursor = conn.cursor()

    cursor.execute(""" 
                   CREATE TABLE IF NOT EXISTS incoming (
                   date TEXT,
                   incoming_message TEXT,
                   sender TEXT,
                   sender_id INTEGER
                   )""")
    
    conn.commit()
    conn.close()
