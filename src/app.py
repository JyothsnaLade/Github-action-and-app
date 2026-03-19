import os
import sys
import sqlite3
import subprocess
import hashlib

def get_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    return result
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    return result

    subprocess.run([user_input], shell=False)

    return hashlib.md5(password.encode()).hexdigest()