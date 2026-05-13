import datetime
from pathlib import Path
import sqlite3
import asyncio
from database import db_conn, create_table_busy_intervals, create_table_whitelist, create_table_report_time, create_table_messages, create_table_incoming
import tgconnect
# BLOCK A

# creating tables
create_table_busy_intervals()
create_table_whitelist()
create_table_report_time()
create_table_messages()
create_table_incoming()

def validate_time(time_str):
    try:
        datetime.datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False

def change_busy_intervals(busy_from, busy_to):
    conn = db_conn()
    cursor = conn.cursor()

    cursor.execute("UPDATE busy_intervals SET busy_from = ?, busy_to = ? WHERE id = 1", (busy_from, busy_to))

    conn.commit()
        
    print(f"your busy intervals have been set to {busy_from} to {busy_to}")

    return busy_from, busy_to


def set_busy_intervals():
    conn = db_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT busy_from, busy_to FROM busy_intervals")
    current_intervals = cursor.fetchall()

    if not current_intervals:
        busy_from = input("From what time are you busy? (xx:xx)")
        busy_to = input("Until what time are you busy? (xx:xx)")

        cursor.execute("INSERT INTO busy_intervals (busy_from, busy_to) VALUES (?, ?)", (busy_from, busy_to))
        conn.commit()

        print(f"\nYour busy intervals have been set to {busy_from} to {busy_to}")
        return busy_from, busy_to
    
    else:
        print("Your current busy intervals are:")
        for row in current_intervals:
            print(dict(row))
        change_current_intervals = input("Would you like to change current intervals?(y for yes, n for no)")

        if change_current_intervals == "y":
            busy_from = input("\nFrom what time are you busy? (xx:xx)")
            busy_to = input("Until what time are you busy? (xx:xx)")

            change_busy_intervals(busy_from, busy_to)

        cursor.execute("SELECT * FROM busy_intervals")
        result = cursor.fetchall()

        for row in result:
            print(f"\nYour current busy intervals {dict(row)}")

        return row

def set_whitelist():
    conn = db_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM whitelist")
    current_whitelist = cursor.fetchall()

    if not current_whitelist:
        whitelist = []

        while True:
            user = input("Enter name to add to whitelist (Press enter to stop):")

            if user == "":
                break

            whitelist.append(user)
        
        for item in whitelist:
            cursor.execute("INSERT INTO whitelist (name) VALUES (?)", (item,))

        conn.commit()

        cursor.execute("SELECT name FROM whitelist")
        result = cursor.fetchall()
        print("Users currently in whitelist:")
        for u in result:
            print(dict(u))

    else:
        print("\nYour current whitelist:")
        for row in current_whitelist:
            print(dict(row))
        change_current_whitelist = input("Would you like to change current whitelist?(y for yes, n for no)")

        if change_current_whitelist == "y":
            whitelist = []

            cursor.execute("DELETE FROM whitelist")

            while True:
                user = input("Enter name to add to whitelist (Press enter to stop):")

                if user == "":
                    break

                whitelist.append(user)
        
            for item in whitelist:
                cursor.execute("INSERT INTO whitelist (name) VALUES (?)", (item,))
            
            conn.commit()

        cursor.execute("SELECT name FROM whitelist")
        result = cursor.fetchall()
        print("Users currently in whitelist:")
        for u in result:
            print(dict(u))
        return

def set_report_time():
    conn = db_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM report_time")
    current_report_time = cursor.fetchone()

    if not current_report_time:
        time = input("\nChoose report time (xx:xx)").strip()

        if not validate_time(time):
            cursor.execute("SELECT busy_to FROM busy_intervals")
            time = cursor.fetchone()[0]
            
            print("Wrong format input, report time has been set to the end of busy interval.")

        cursor.execute("INSERT INTO report_time (time) VALUES (?)", (time,))
        conn.commit()

        cursor.execute("SELECT * FROM report_time")
        result = cursor.fetchone()

        print(f"Your current report time has been set to {result[0]}")

        return 

    else:
        print(f"\nYour current report time is {current_report_time[0]}")
        change_report_time = input("Do you want to change it? (y for yes, n for no)")

        if change_report_time == "y":
            cursor.execute("DELETE FROM report_time")

            time = input("Choose report time (xx:xx)").strip()

            if not validate_time(time):
                cursor.execute("SELECT busy_to FROM busy_intervals")
                time = cursor.fetchone()[0]
                
                print("Wrong format input, report time has been set to the end of busy interval.")

            cursor.execute("INSERT INTO report_time (time) VALUES (?)", (time,))
            conn.commit()

            cursor.execute("SELECT * FROM report_time")
            result = cursor.fetchone()

            print(f"Your current report time has been set to {result[0]}")

    return

def set_message():
    conn = db_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT message FROM messages")
    current_responses = cursor.fetchall()

    if not current_responses:
        responses_list = []

        while True:
            response_in = input("Enter at least 3 responses to incoming messages (Press Enter to stop): ")

            if response_in == "":
                if len(responses_list) < 3:
                    print("You need to enter at least 3 resonses to proceed")
                    pass
                else:
                    break
            if response_in.strip():
                responses_list.append(response_in)

        for item in responses_list:
            cursor.execute("INSERT INTO messages (message) VALUES (?)", (item,))

        conn.commit()
        conn.close()

    else:
        print('\nYour current responses are:')
        for item in current_responses:
            print(dict(item))

        change_message = input("Do you want to change them? (y for yes, n for no)")

        if change_message == "y":
            cursor.execute("DELETE FROM messages")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'messages'")

            responses_list = []

            while True:
                response_in = input("Enter at least 3 responses to incoming messages (Press Enter to stop): ")

                if response_in == "":
                    if len(responses_list) < 3:
                        print("You need to enter at least 3 resonses to proceed")
                        pass
                    else:
                        break
                if response_in.strip():
                    responses_list.append(response_in)

            for item in responses_list:
                cursor.execute("INSERT INTO messages (message) VALUES (?)", (item,))

            conn.commit()

            cursor.execute("SELECT message FROM messages")
            result = cursor.fetchall()

            print("Your current responses have been set to:")
            for item in result:
                print(dict(item))
            return

set_busy_intervals()
set_whitelist()
set_report_time()
set_message()


asyncio.run(tgconnect.main())