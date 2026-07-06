# L-41_IN_and_NOT_IN_Subqueries.py
# SQLPhone Emperor – SQL Module 05
# Practice: IN and NOT IN with subquery.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create tables 'customers' (id, name) and 'orders' (id, cust_id).")
    print("Insert customers with and without orders.")
    print("Write a query using NOT IN to find customers who have never placed an order.")
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
        cur.execute("SELECT COUNT(*) FROM customers")
        if cur.fetchone()[0] < 3:
            print("❌ Need at least 3 customers.")
            conn.close()
            return False
        cur.execute("""
            SELECT name FROM customers
            WHERE id NOT IN (SELECT cust_id FROM orders)
        """)
        rows = cur.fetchall()
        if rows:
            print(f"✅ Customers without orders: {[r[0] for r in rows]}")
            conn.close()
            return True
        else:
            print("❌ All customers have orders. Insert at least one customer with no orders.")
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