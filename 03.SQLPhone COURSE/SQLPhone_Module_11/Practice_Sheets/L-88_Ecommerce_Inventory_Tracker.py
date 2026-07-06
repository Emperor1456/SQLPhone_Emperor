# L-88_Ecommerce_Inventory_Tracker.py
# SQLPhone Emperor – SQL Module 11
# Practice: E‑commerce inventory.

import sqlite3, os

DB = "ecommerce.db"

def task():
    print("=" * 50)
    print("🧱 PROJECT 2: E‑commerce Inventory Tracker")
    print("Create tables: Category, Supplier, Product, Sale.")
    print("Insert data and run your analysis queries.")
    print("We'll check that tables exist and have records.")
    print("=" * 50)
    if os.path.exists(DB):
        os.remove(DB)
    user_sql = input("Paste your SQL script:\n> ")
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    try:
        for tbl in ['Category','Supplier','Product','Sale']:
            cur.execute(f"SELECT COUNT(*) FROM {tbl}")
            if cur.fetchone()[0] == 0:
                print(f"❌ Table {tbl} empty.")
                conn.close()
                return False
        print("✅ Database populated. Query it to verify your reports.")
        conn.close()
        return True
    except Exception as e:
        print(f"❌ {e}")
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