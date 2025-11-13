# vuln_example.py
# Intentionally insecure example for testing scanners (educational use only).

import os
import subprocess
import pickle
import hashlib
import sqlite3

# 1) Hardcoded credentials
ADMIN_PASSWORD = "P@ssw0rd123"   # Hardcoded secret

# 2) Using eval on user input (remote code execution risk)
def run_calc():
    expr = input("Enter math expression to evaluate: ")
    # Vulnerable: eval runs arbitrary code
    result = eval(expr)
    print("Result:", result)

# 3) Using exec on dynamically built string
def dynamic_exec(name):
    code = f"print('Hello, {name.upper()}')"
    # Vulnerable: exec executes arbitrary code strings
    exec(code)

# 4) Shell injection via subprocess with untrusted input
def list_files():
    user = input("Enter directory to list: ")
    # Vulnerable: passing unsanitized input to shell=True
    subprocess.run(f"ls {user}", shell=True)

# 5) Insecure pickle deserialization from file
def load_session():
    if os.path.exists("session.dat"):
        with open("session.dat", "rb") as f:
            # Vulnerable: untrusted pickle.load can execute arbitrary code
            session = pickle.load(f)
            print("Loaded session:", session)

# 6) SQL injection via string formatting
def get_user_by_name(name):
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);")
    cur.execute("INSERT INTO users (name) VALUES ('alice'), ('bob');")
    # Vulnerable: directly formatting user input into SQL
    query = f"SELECT id, name FROM users WHERE name = '{name}';"
    cur.execute(query)
    print(cur.fetchall())
    conn.close()

# 7) Weak hash (MD5) for password hashing
def hash_password(pw):
    # Vulnerable: MD5 is not suitable for password hashing
    return hashlib.md5(pw.encode()).hexdigest()

# 8) Insecure file permission (world-readable)
def write_config():
    data = "API_KEY=ABC123SECRET"
    with open("config.txt", "w") as f:
        f.write(data)
    # Vulnerable: setting overly permissive permissions (example)
    os.chmod("config.txt", 0o644)  # world-readable on some systems

if __name__ == "__main__":
    print("Pick a function to run:")
    print("1) run_calc  2) dynamic_exec  3) list_files  4) load_session")
    print("5) get_user_by_name  6) hash_password  7) write_config")
    choice = input("Choice: ").strip()
    if choice == "1":
        run_calc()
    elif choice == "2":
        dynamic_exec("user")
    elif choice == "3":
        list_files()
    elif choice == "4":
        load_session()
    elif choice == "5":
        get_user_by_name(input("Name: "))
    elif choice == "6":
        print(hash_password(input("Password: ")))
    elif choice == "7":
        write_config()
    else:
        print("No-op")
