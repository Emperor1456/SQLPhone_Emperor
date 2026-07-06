# L-59_Mathematical_Functions.py
# SQLPhone Emperor – SQL Module 07
# Practice: Use math functions.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'products' (name, price, discount_pct).")
    print("Insert a few products with prices and discount percentages (as integer, e.g., 10 for 10%).")
    print("Write a query that shows the final price after discount, rounded to 2 decimals.")
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
        cur.execute("SELECT ROUND(price * (100 - discount_pct) / 100.0, 2) FROM products LIMIT 1")
        val = cur.fetchone()
        if val is not None and val[0] is not None:
            print(f"✅ Final price calculated: {val[0]}")
            conn.close()
            return True
        else:
            print("❌ Could not compute final price.")
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