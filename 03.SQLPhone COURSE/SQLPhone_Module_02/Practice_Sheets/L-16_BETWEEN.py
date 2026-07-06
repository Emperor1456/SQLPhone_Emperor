# L-16_BETWEEN.py
# SQLPhone Emperor – SQL Module 02
# Practice: Filter with BETWEEN.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'events' (id, name, event_date TEXT in 'YYYY-MM-DD').")
    print("Insert at least 4 rows with dates covering a range.")
    print("Write a query that selects events between '2026-06-01' and '2026-06-30' inclusive.")
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
        cur.execute("SELECT COUNT(*) FROM events WHERE event_date BETWEEN '2026-06-01' AND '2026-06-30'")
        count = cur.fetchone()[0]
        if count > 0:
            print(f"✅ Query returned {count} June events.")
            conn.close()
            return True
        else:
            print("❌ No events found for June 2026. Ensure data includes those dates.")
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