# L-52_DEFAULT_Values.py
# SQLPhone Emperor – SQL Module 06
# Practice: DEFAULT values in action.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'tasks' (id INTEGER PRIMARY KEY, title TEXT, status TEXT DEFAULT 'pending', created TEXT DEFAULT (datetime('now'))).")
    print("Insert a row specifying only title. Then SELECT to see the default values applied.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    user_sql = input("Enter your SQL:\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    try:
        cur.execute("SELECT status, created FROM tasks WHERE title IS NOT NULL LIMIT 1")
        row = cur.fetchone()
        if row and row[0] == 'pending' and row[1] is not None:
            print(f"✅ Defaults applied: status={row[0]}, created={row[1]}")
            conn.close()
            return True
        else:
            print(f"❌ Default values not as expected: {row}")
            conn.close()
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
            break

if __name__ == "__main__":
    main()