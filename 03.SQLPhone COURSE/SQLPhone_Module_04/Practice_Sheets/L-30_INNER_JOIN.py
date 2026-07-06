# L-30_INNER_JOIN.py
# SQLPhone Emperor – SQL Module 04
# Practice: INNER JOIN.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create tables 'customers' (id, name) and 'orders' (id, customer_id, product).")
    print("Insert at least 3 customers and 5 orders, some customers with no orders.")
    print("Write an INNER JOIN query that returns customer name and product for all orders.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    user_sql = input("Enter your SQL (DDL + DML + query):\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    try:
        # Verify inner join returns only matched rows
        cur.execute("SELECT COUNT(*) FROM orders")
        orders = cur.fetchone()[0]
        cur.execute("""
            SELECT COUNT(*) FROM customers c
            INNER JOIN orders o ON c.id = o.customer_id
        """)
        join_count = cur.fetchone()[0]
        if join_count == orders:
            print(f"✅ INNER JOIN returned {join_count} rows (all orders have matching customers).")
            conn.close()
            return True
        else:
            print(f"❌ Mismatch: {orders} orders but join returned {join_count}. Ensure all orders link to existing customers.")
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