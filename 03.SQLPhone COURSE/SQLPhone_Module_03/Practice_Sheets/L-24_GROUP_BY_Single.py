# L-24_GROUP_BY_Single.py
# SQLPhone Emperor – SQL Module 03
# Practice: GROUP BY single column.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'orders' (id, customer, amount).")
    print("Insert at least 5 rows, with multiple orders per customer.")
    print("Write a query that shows total amount spent per customer.")
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
        cur.execute("SELECT COUNT(*) FROM orders")
        if cur.fetchone()[0] < 5:
            print("❌ Need at least 5 rows.")
            conn.close()
            return False
        # Verify grouping query runs
        cur.execute("SELECT customer, SUM(amount) FROM orders GROUP BY customer")
        rows = cur.fetchall()
        if len(rows) > 0:
            print(f"✅ Grouped by customer. {len(rows)} groups found.")
            conn.close()
            return True
        else:
            print("❌ Grouping returned nothing.")
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