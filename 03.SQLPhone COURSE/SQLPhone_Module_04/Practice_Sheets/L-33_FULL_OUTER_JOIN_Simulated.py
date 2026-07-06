# L-33_FULL_OUTER_JOIN_Simulated.py
# SQLPhone Emperor – SQL Module 04
# Practice: Simulate FULL OUTER JOIN.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create tables 'A' (id, val) and 'B' (id, val) with overlapping and non‑overlapping ids.")
    print("Write a FULL OUTER JOIN simulation using LEFT JOIN + UNION + LEFT JOIN (swapped).")
    print("The result should contain all rows from both tables, with NULLs where no match.")
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
        # Quick check: count unique ids from both tables
        cur.execute("SELECT COUNT(DISTINCT id) FROM (SELECT id FROM A UNION SELECT id FROM B)")
        expected = cur.fetchone()[0]
        cur.execute("""
            SELECT id FROM A LEFT JOIN B USING(id)
            UNION
            SELECT id FROM B LEFT JOIN A USING(id)
        """)
        actual = len(cur.fetchall())
        if actual == expected:
            print(f"✅ FULL OUTER JOIN simulation returned {actual} rows, matching expected distinct ids.")
            conn.close()
            return True
        else:
            print(f"❌ Expected {expected} rows, got {actual}. Check your UNION query.")
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