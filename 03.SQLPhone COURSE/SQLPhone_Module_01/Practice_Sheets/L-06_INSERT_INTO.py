# L-06_INSERT_INTO.py
# SQLPhone Emperor – SQL Module 01
# Practice: Insert single and multiple rows.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'cities' (id INTEGER PRIMARY KEY, name TEXT NOT NULL, country TEXT, population INTEGER).")
    print("Insert 3 rows in one statement. Then insert one more row, omitting id (auto-increment).")
    print("Use RETURNING to get the generated id for the last insert.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    user_sql = input("Enter your SQL (multiple statements separated by ;):\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    try:
        cur.execute("SELECT COUNT(*) FROM cities")
        count = cur.fetchone()[0]
        if count != 4:
            print(f"❌ Expected 4 rows, got {count}.")
            conn.close()
            return False
        cur.execute("SELECT id FROM cities ORDER BY id DESC LIMIT 1")
        last_id = cur.fetchone()[0]
        print(f"✅ All 4 rows inserted. Last inserted id (via RETURNING or auto): {last_id}")
        conn.close()
        return True
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