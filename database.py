import sqlite3

def get_db():
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    # table for storing tasks + deadline
    conn.execute('''CREATE TABLE IF NOT EXISTS tasks 
                    (id INTEGER PRIMARY KEY, task TEXT, deadline TEXT)''')

    conn.commit()
    conn.close()


def add_task(task, deadline):
    conn = get_db()

    # insert task into database
    conn.execute(
        'INSERT INTO tasks (task, deadline) VALUES (?, ?)',
        (task, deadline)
    )

    conn.commit()
    conn.close()


def get_tasks():
    conn = get_db()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return tasks


def delete_task(task_id):
    conn = get_db()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()