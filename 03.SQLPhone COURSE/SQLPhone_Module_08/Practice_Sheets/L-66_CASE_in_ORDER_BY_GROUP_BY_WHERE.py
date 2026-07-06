# L-66_CASE_in_ORDER_BY_GROUP_BY_WHERE.py
# SQLPhone Emperor – SQL Module 08
# Practice: CASE in other clauses.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'tickets' (id, severity TEXT, created_date).")
    print("Insert rows with severity 'critical', 'high', 'medium', 'low'.")
    print("Write a query that orders by severity: critical first, then high, then rest.")
    print("Use CASE in ORDER BY.")
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
        cur.execute("SELECT severity FROM tickets ORDER BY CASE severity WHEN 'critical' THEN 1 WHEN 'high' THEN 2 ELSE 3 END")
        rows = cur.fetchall()
        if rows and rows[0][0] == 'critical':
            print(f"✅ Order correct. First: {rows[0][0]}")
            conn.close()
            return True
        else:
            print(f"❌ Ordering not as expected. First row: {rows[0] if rows else 'none'}")
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