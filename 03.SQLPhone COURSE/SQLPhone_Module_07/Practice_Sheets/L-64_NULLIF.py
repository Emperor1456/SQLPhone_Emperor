# L-64_NULLIF.py
# SQLPhone Emperor – SQL Module 07
# Practice: NULLIF to prevent division by zero.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'stats' (item TEXT, total_sales REAL, quantity INTEGER).")
    print("Insert rows, including one where quantity is 0.")
    print("Write a query that calculates average sale per item (total_sales / quantity), but returns NULL if quantity is 0 (use NULLIF).")
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
        cur.execute("""
            SELECT item, total_sales / NULLIF(quantity, 0) AS avg_price
            FROM stats
        """)
        rows = cur.fetchall()
        for row in rows:
            if row[1] is None:
                print(f"✅ NULLIF returned NULL for item {row[0]} (division avoided).")
            else:
                print(f"Avg price for {row[0]}: {row[1]}")
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