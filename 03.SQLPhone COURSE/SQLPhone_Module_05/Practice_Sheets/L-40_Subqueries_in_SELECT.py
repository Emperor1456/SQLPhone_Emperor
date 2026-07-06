# L-40_Subqueries_in_SELECT.py
# SQLPhone Emperor – SQL Module 05
# Practice: Scalar subquery in SELECT list.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'products' (id, name, price).")
    print("Insert at least 3 rows.")
    print("Write a query that shows each product's price and the overall average price as a column.")
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
        cur.execute("SELECT AVG(price) FROM products")
        avg = cur.fetchone()[0]
        cur.execute("SELECT name, price, (SELECT AVG(price) FROM products) AS avg_price FROM products")
        rows = cur.fetchall()
        if len(rows) < 3:
            print("❌ Need at least 3 products.")
            conn.close()
            return False
        if rows and all(row[2] == avg for row in rows):
            print(f"✅ Each row shows the correct average price {avg:.2f}.")
            conn.close()
            return True
        else:
            print("❌ The subquery column is not consistent or incorrect.")
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