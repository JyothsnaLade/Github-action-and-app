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

def run_command(user_input):
    subprocess.run([user_input], shell=False)

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()