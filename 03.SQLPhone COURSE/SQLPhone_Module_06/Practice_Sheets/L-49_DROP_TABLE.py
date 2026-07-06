# L-49_DROP_TABLE.py
# SQLPhone Emperor – SQL Module 06
# Practice: DROP TABLE safely.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create two tables: 'temp1' and 'temp2'.")
    print("Then drop 'temp1' using DROP TABLE IF EXISTS.")
    print("Finally, list remaining tables to verify temp1 is gone.")
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
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [r[0] for r in cur.fetchall()]
        if 'temp1' not in tables and 'temp2' in tables:
            print(f"✅ temp1 dropped. Remaining tables: {tables}")
            conn.close()
            return True
        else:
            print(f"❌ temp1 still exists or temp2 missing. Tables: {tables}")
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