# L-32_RIGHT_JOIN_Simulated.py
# SQLPhone Emperor – SQL Module 04
# Practice: Simulate RIGHT JOIN.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create tables 'suppliers' (id, name) and 'products' (id, name, supplier_id).")
    print("Insert at least one supplier with no products, and some products with suppliers.")
    print("Write a query that simulates a RIGHT JOIN to list all products and their supplier (even if supplier missing).")
    print("(Swap the table order in a LEFT JOIN)")
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
        cur.execute("SELECT COUNT(*) FROM products")
        prod_count = cur.fetchone()[0]
        # Simulated RIGHT JOIN: products LEFT JOIN suppliers
        cur.execute("""
            SELECT p.name, s.name
            FROM products p
            LEFT JOIN suppliers s ON p.supplier_id = s.id
        """)
        rows = cur.fetchall()
        if len(rows) == prod_count:
            print(f"✅ Right join simulation returned all {prod_count} products.")
            conn.close()
            return True
        else:
            print(f"❌ Expected {prod_count} rows, got {len(rows)}.")
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