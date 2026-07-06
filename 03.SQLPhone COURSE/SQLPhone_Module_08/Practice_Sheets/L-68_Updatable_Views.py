# L-68_Updatable_Views.py
# SQLPhone Emperor – SQL Module 08
# Practice: Updatable views.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'products' (id, name, price, stock).")
    print("Create a view 'low_stock' selecting id, name, stock where stock < 10.")
    print("Insert rows, then UPDATE a row through the view to change stock, and verify the base table.")
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
        # Check that view exists
        cur.execute("SELECT name FROM sqlite_master WHERE type='view' AND name='low_stock'")
        if not cur.fetchone():
            print("❌ View 'low_stock' not found.")
            conn.close()
            return False
        # Try to update through view and then verify base table
        cur.execute("UPDATE low_stock SET stock = 20 WHERE id = (SELECT id FROM products WHERE stock < 10 LIMIT 1)")
        conn.commit()
        cur.execute("SELECT stock FROM products WHERE stock = 20")
        updated = cur.fetchone()
        if updated:
            print("✅ Update through view succeeded and base table reflects change.")
            conn.close()
            return True
        else:
            print("❌ Update through view failed or didn't affect base table.")
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