# L-01_What_is_SQL.py
# SQLPhone Emperor – SQL Module 01
# Practice: Your first SQL query.

import sqlite3
import os

DB = ":memory:"

def task():
    print("=" * 50)
    print("🧱 TASK: Create a table named 'empire' with columns 'id' (INTEGER) and 'name' (TEXT). Insert one row: id=1, name='Emperor'. Then SELECT all rows.")
    print("=" * 50)
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    user_sql = input("Enter your SQL (end with ;):\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False

    # Verify that empire table exists and contains the correct row
    try:
        cur.execute("SELECT id, name FROM empire WHERE id=1")
        row = cur.fetchone()
        conn.close()
        if row and row[0] == 1 and row[1] == 'Emperor':
            print("✅ Correct! Your empire table is ready.")
            return True
        else:
            print("❌ Row not found or incorrect. Check your INSERT and SELECT.")
            return False
    except Exception as e:
        print(f"❌ Verification error: {e}")
        conn.close()
        return False

def main():
    while True:
        if task():
            break
        retry = input("Try again? (y/n): ")
        if retry.lower() != 'y':
            print("Exiting practice.")
            break

if __name__ == "__main__":
    main()