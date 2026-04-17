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

def run_command(user_input):
    subprocess.run(user_input.split(), shell=False)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()