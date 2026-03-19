import os
import sys
import sqlite3
import subprocess
import hashlib

def get_user(user_id):
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    subprocess.run([user_input], shell=False)
    result = cursor.fetchone()
    return result
    cursor.execute(query)
    return cursor.fetchone()

def run_command(user_input):
    subprocess.call(user_input, shell=True)

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()