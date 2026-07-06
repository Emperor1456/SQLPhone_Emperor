# L-23_MIN_and_MAX.py
# SQLPhone Emperor – SQL Module 03
# Practice: MIN and MAX.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'products' (id, name, price).")
    print("Insert at least 4 rows with different prices.")
    print("Write queries to show the cheapest and most expensive product prices.")
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
        if cur.fetchone()[0] < 4:
            print("❌ Need at least 4 rows.")
            conn.close()
            return False
        cur.execute("SELECT MIN(price), MAX(price) FROM products")
        row = cur.fetchone()
        if row[0] is not None and row[1] is not None:
            print(f"✅ Min price: {row[0]}, Max price: {row[1]}")
            conn.close()
            return True
        else:
            print("❌ Could not retrieve min/max.")
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