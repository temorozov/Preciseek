import sqlite3

with sqlite3.connect("mydb.db") as conn:
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            collection_name TEXT
        )
    """)


def save_user_collection(user_id, collection_name):
    with sqlite3.connect("mydb.db") as conn:
        cur = conn.cursor()
        cur.execute("INSERT OR REPLACE INTO users (user_id, collection_name) VALUES (?, ?)", (user_id, collection_name))

def get_user_collection(user_id):
    with sqlite3.connect("mydb.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT collection_name FROM users WHERE user_id = ?", (user_id,))
        result = cur.fetchone()

        if result is None: return
        return result[0]
        





