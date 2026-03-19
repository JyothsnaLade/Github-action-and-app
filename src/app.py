import os
import os
import sys
import sys
import sqlite3
import subprocess
import hashlib
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    return result
    conn = sqlite3.connect('users.db')
    subprocess.run(user_input.split(), shell=False)
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    return result

def run_command(user_input):
    subprocess.run([user_input], shell=False)

def hash_password(password):