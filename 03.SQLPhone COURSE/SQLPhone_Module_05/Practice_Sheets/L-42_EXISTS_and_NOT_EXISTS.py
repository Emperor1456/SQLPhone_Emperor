# L-42_EXISTS_and_NOT_EXISTS.py
# SQLPhone Emperor – SQL Module 05
# Practice: EXISTS and NOT EXISTS.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Use same customers/orders tables.")
    print("Write a query using NOT EXISTS to find customers with no orders.")
    print("Also write an EXISTS query to find customers who have placed at least one order.")
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
        # Test NOT EXISTS
        cur.execute("""
            SELECT name FROM customers c
            WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.cust_id = c.id)
        """)
        not_exists = cur.fetchall()
        # Test EXISTS
        cur.execute("""
            SELECT name FROM customers c
            WHERE EXISTS (SELECT 1 FROM orders o WHERE o.cust_id = c.id)
        """)
        exists = cur.fetchall()
        if not_exists and exists:
            print(f"✅ NOT EXISTS: {[r[0] for r in not_exists]}")
            print(f"✅ EXISTS: {[r[0] for r in exists]}")
            conn.close()
            return True
        else:
            print("❌ Need both customers with and without orders to verify both queries.")
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