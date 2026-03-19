import os
import sys
import os
import sys
import sqlite3
import subprocess
import hashlib

def get_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    return result
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    subprocess.run([user_input], shell=False)

def run_command(user_input):

def hash_password(password):