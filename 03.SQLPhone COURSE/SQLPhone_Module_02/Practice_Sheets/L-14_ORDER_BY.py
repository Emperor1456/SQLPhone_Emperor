# L-14_ORDER_BY.py
# SQLPhone Emperor – SQL Module 02
# Practice: Sort query results.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'scores' (player TEXT, score INTEGER, level INTEGER).")
    print("Insert at least 4 rows with varied scores and levels.")
    print("Write a query that returns all columns sorted by level DESC, then score DESC.")
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
        cur.execute("SELECT * FROM scores ORDER BY level DESC, score DESC")
        rows = cur.fetchall()
        if len(rows) < 4:
            print("❌ Need at least 4 rows.")
            conn.close()
            return False
        levels = [r[2] for r in rows]
        if levels == sorted(levels, reverse=True):
            print(f"✅ Query returned {len(rows)} rows, sorted by level DESC then score DESC.")
            conn.close()
            return True
        else:
            print("❌ Sorting not as expected. Check your ORDER BY clause.")
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