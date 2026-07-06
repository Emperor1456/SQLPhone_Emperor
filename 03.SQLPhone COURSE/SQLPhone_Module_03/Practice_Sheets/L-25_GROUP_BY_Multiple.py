# L-25_GROUP_BY_Multiple.py
# SQLPhone Emperor – SQL Module 03
# Practice: GROUP BY multiple columns.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'sales' (region, product, quantity).")
    print("Insert rows covering at least 2 regions and 2 products with varying quantities.")
    print("Write a query to show total quantity sold per region and product.")
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
        cur.execute("SELECT COUNT(*) FROM sales")
        if cur.fetchone()[0] < 4:
            print("❌ Need at least 4 rows.")
            conn.close()
            return False
        cur.execute("SELECT region, product, SUM(quantity) FROM sales GROUP BY region, product")
        rows = cur.fetchall()
        if len(rows) >= 2:
            print(f"✅ Multi‑column grouping produced {len(rows)} groups.")
            conn.close()
            return True
        else:
            print("❌ Not enough distinct groups. Insert more varied data.")
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