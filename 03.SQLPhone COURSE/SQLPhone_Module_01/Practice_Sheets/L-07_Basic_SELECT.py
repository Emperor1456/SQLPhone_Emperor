# L-07_Basic_SELECT.py
# SQLPhone Emperor – SQL Module 01
# Practice: Projection and filtering.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: You have a table 'inventory' with columns: id, product, quantity, price.")
    print("Create the table and insert 3 products.")
    print("Write a SELECT query that returns product name and total value (quantity*price) for items where quantity > 0.")
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
    # Verify that the table has data and the computed column query works.
    try:
        cur.execute("SELECT COUNT(*) FROM inventory")
        if cur.fetchone()[0] < 3:
            print("❌ Need at least 3 products.")
            conn.close()
            return False
        # Check that a SELECT with computed column doesn't fail.
        cur.execute("SELECT product, quantity * price AS total_value FROM inventory WHERE quantity > 0")
        row = cur.fetchone()
        if row:
            print(f"✅ Query worked. Example row: {row}")
            conn.close()
            return True
        else:
            print("❌ Query returned no rows. Ensure quantity > 0.")
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