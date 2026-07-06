# L-03_First_Database_and_Dot_Commands.py
# SQLPhone Emperor – SQL Module 01
# Practice: Create a database file and inspect it.

import sqlite3, os

def task():
    print("=" * 50)
    print("🧱 TASK: Create a database file 'first.db' with a table 'people' (name TEXT, age INT). Insert one person. Use dot-commands to inspect.")
    print("We'll simulate .schema and .tables using Python.")
    print("=" * 50)
    db_name = "first.db"
    # Remove if exists for fresh start
    if os.path.exists(db_name):
        os.remove(db_name)
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    user_sql = input("Enter your SQL:\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    # Verify that table people exists
    try:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='people'")
        row = cur.fetchone()
        if not row:
            print("❌ Table 'people' not found.")
            conn.close()
            return False
        # Check if at least one row inserted
        cur.execute("SELECT * FROM people")
        data = cur.fetchall()
        if len(data) == 0:
            print("❌ No rows in people. Insert at least one row.")
            conn.close()
            return False
        # Show schema
        cur.execute("SELECT sql FROM sqlite_master WHERE name='people'")
        schema = cur.fetchone()[0]
        print(f"✅ Table 'people' exists. Schema:\n{schema}")
        print(f"Rows: {data}")
        conn.close()
        return True
    except Exception as e:
        print(f"❌ Verification error: {e}")
        conn.close()
        return False
    finally:
        if os.path.exists(db_name):
            os.remove(db_name)  # clean up

def main():
    while True:
        if task():
            break
        retry = input("Try again? (y/n): ")
        if retry.lower() != 'y':
            break

if __name__ == "__main__":
    main()