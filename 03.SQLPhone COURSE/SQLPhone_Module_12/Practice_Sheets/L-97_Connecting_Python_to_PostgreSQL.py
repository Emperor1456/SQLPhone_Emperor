# L-97_Connecting_Python_to_PostgreSQL.py
# SQLPhone Emperor – SQL Module 12
# Practice: Connect to PostgreSQL if available, or simulate.

import sqlite3, subprocess, sys

def task():
    print("=" * 50)
    print("🧱 TASK: If you have PostgreSQL running (via proot), write a Python script using psycopg2 to connect and run SELECT version().")
    print("If not, write a Python script that prints 'Simulated PostgreSQL connection' and the SQLite version.")
    print("We'll execute your code.")
    print("=" * 50)
    code = input("Enter your Python code:\n> ")
    try:
        exec(code, {"__name__": "__main__"})
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    print("✅ Code executed without exceptions.")
    return True

def main():
    while True:
        if task():
            break
        retry = input("Try again? (y/n): ")
        if retry.lower() != 'y':
            break

if __name__ == "__main__":
    main()