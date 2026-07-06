# L-04_Data_Types_in_SQLite.py
# SQLPhone Emperor – SQL Module 01
# Practice: Use correct storage classes and type affinity.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create a table 'products' with columns:")
    print("  id (INTEGER PRIMARY KEY), name (TEXT NOT NULL), price (REAL), quantity (INTEGER), photo (BLOB).")
    print("Insert one row with realistic values (photo can be X'0000').")
    print("Then SELECT to verify type affinity works.")
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
    # Verify structure
    try:
        cur.execute("PRAGMA table_info('products')")
        cols = cur.fetchall()
        if len(cols) != 5:
            print("❌ Table should have 5 columns.")
            conn.close()
            return False
        # Check inserted data
        cur.execute("SELECT * FROM products")
        row = cur.fetchone()
        if not row:
            print("❌ No data inserted.")
            conn.close()
            return False
        print(f"✅ Products table created with {len(cols)} columns. Data: {row}")
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