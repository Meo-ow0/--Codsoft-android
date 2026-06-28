import sqlite3

def get_db():
    conn = sqlite3.connect('alarms.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('CREATE TABLE IF NOT EXISTS alarms (id INTEGER PRIMARY KEY, time TEXT, label TEXT)')
    conn.commit()
    conn.close()

def add_alarm(time, label):
    conn = get_db()
    conn.execute("INSERT INTO alarms (time, label) VALUES (?, ?)", (time, label))
    conn.commit()
    conn.close()

def get_alarms():
    conn = get_db()
    alarms = conn.execute("SELECT id, time, label FROM alarms").fetchall()
    conn.close()
    return alarms