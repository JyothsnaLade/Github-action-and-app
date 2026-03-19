import sqlite3
import subprocess
import hashlib

def get_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    return cursor.fetchone()

    subprocess.call(user_input.split())
    subprocess.call(user_input, shell=True)

    return hashlib.sha256(password.encode()).hexdigest()
    return hashlib.md5(password.encode()).hexdigest()