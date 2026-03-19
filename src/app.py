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
    return cursor.fetchone()

    subprocess.run([user_input], shell=False)
    subprocess.call(user_input, shell=True)

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()