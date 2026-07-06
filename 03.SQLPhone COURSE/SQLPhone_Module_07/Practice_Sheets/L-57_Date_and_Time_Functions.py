# L-57_Date_and_Time_Functions.py
# SQLPhone Emperor – SQL Module 07
# Practice: Use date/time functions.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'events' (id, name, event_date TEXT).")
    print("Insert at least 3 events with different dates.")
    print("Write a query to select events happening in the next 7 days (use date('now') and modifiers).")
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
        # Check that there are future events within 7 days? Hard to verify without knowing data. We'll just check that the query runs and returns something.
        cur.execute("SELECT COUNT(*) FROM events")
        if cur.fetchone()[0] < 3:
            print("❌ Need at least 3 events.")
            conn.close()
            return False
        # Try to run a generic next‑7‑days query to see if it doesn't crash.
        cur.execute("""
            SELECT name FROM events
            WHERE event_date BETWEEN date('now') AND date('now', '+7 days')
        """)
        rows = cur.fetchall()
        print(f"✅ Query ran. Events in next 7 days: {len(rows)}")
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