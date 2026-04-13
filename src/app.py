import os
import sys
import sqlite3
import subprocess
import hashlib

def get_user(user_id):
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    subprocess.call(user_input.split())

def run_command(user_input):
    return hashlib.sha256(password.encode()).hexdigest()

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()