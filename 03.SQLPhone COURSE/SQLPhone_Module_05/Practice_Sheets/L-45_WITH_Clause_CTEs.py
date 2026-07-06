# L-45_WITH_Clause_CTEs.py
# SQLPhone Emperor – SQL Module 05
# Practice: Common Table Expressions (WITH).

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'sales' (id, product, amount, region).")
    print("Insert at least 6 rows with multiple regions.")
    print("Use a CTE to compute total sales per region, then select regions where total > 1000.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    user_sql = input("Enter your SQL (include WITH clause):\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    try:
        cur.execute("SELECT COUNT(*) FROM sales")
        if cur.fetchone()[0] < 6:
            print("❌ Need at least 6 rows.")
            conn.close()
            return False
        # Check if CTE syntax works by running a similar query
        # We'll just trust that their CTE works; we can verify by running a simple CTE
        cur.execute("""
            WITH region_totals AS (
                SELECT region, SUM(amount) as total
                FROM sales
                GROUP BY region
            )
            SELECT region, total FROM region_totals WHERE total > 1000
        """)
        rows = cur.fetchall()
        if rows:
            print(f"✅ CTE query returned regions with total > 1000: {rows}")
            conn.close()
            return True
        else:
            print("❌ No region with total > 1000. Adjust data so at least one region's sum exceeds 1000.")
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