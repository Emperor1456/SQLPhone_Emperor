# L-28_Aggregation_Challenge_Set.py
# SQLPhone Emperor – SQL Module 03
# Practice: Full aggregation challenge.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 MODULE 03 CHALLENGE: Sales Aggregation")
    print("Create table 'sales' (id, product, category, quantity, price, sale_date).")
    print("Insert at least 6 rows with varied data covering multiple months of 2026.")
    print("Write the five required queries (refer to lecture).")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    user_sql = input("Enter your full SQL script:\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    try:
        # Check that there are multiple months and enough rows
        cur.execute("SELECT COUNT(*) FROM sales")
        if cur.fetchone()[0] < 6:
            print("❌ Need at least 6 rows.")
            conn.close()
            return False
        # Try each required query pattern and see if they work
        # 1. count total sales records
        cur.execute("SELECT COUNT(*) FROM sales")
        c1 = cur.fetchone()[0]
        # 2. total quantity sold per product
        cur.execute("SELECT product, SUM(quantity) FROM sales GROUP BY product")
        # 3. average price per category
        cur.execute("SELECT category, AVG(price) FROM sales GROUP BY category")
        # 4. categories with total revenue > 5000
        cur.execute("SELECT category, SUM(quantity*price) as rev FROM sales GROUP BY category HAVING rev > 5000")
        # 5. month with sales count > 10 in 2026
        cur.execute("""
            SELECT strftime('%m', sale_date) as month, COUNT(*)
            FROM sales
            WHERE sale_date LIKE '2026%'
            GROUP BY month
            HAVING COUNT(*) > 10
        """)
        # If we got here without exception, it's good
        print(f"✅ All queries executed. Total sales records: {c1}.")
        conn.close()
        return True
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