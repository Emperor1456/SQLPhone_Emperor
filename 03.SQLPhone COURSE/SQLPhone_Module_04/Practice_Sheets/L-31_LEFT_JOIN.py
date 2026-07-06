# L-31_LEFT_JOIN.py
# SQLPhone Emperor – SQL Module 04
# Practice: LEFT JOIN.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Use the same 'customers' and 'orders' tables (at least 1 customer with no orders).")
    print("Write a LEFT JOIN query that lists all customer names and any product they ordered (NULL if none).")
    print("Also write a query using LEFT JOIN to find customers without orders.")
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
        # Check left join returns all customers
        cur.execute("SELECT COUNT(*) FROM customers")
        total_cust = cur.fetchone()[0]
        cur.execute("""
            SELECT COUNT(*) FROM customers c
            LEFT JOIN orders o ON c.id = o.customer_id
        """)
        left_count = cur.fetchone()[0]
        if left_count >= total_cust:
            print(f"✅ LEFT JOIN returned {left_count} rows (>= {total_cust} customers).")
            # Check if there's at least one customer with NULL order
            cur.execute("""
                SELECT c.name FROM customers c
                LEFT JOIN orders o ON c.id = o.customer_id
                WHERE o.id IS NULL
            """)
            nulls = cur.fetchall()
            if nulls:
                print(f"✅ Customers without orders: {[r[0] for r in nulls]}")
                conn.close()
                return True
            else:
                print("❌ All customers have orders. Insert a customer with no order for the full test.")
                conn.close()
                return False
        else:
            print("❌ LEFT JOIN should return at least the number of customers.")
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