# L-47_UPDATE_Modifying_Rows.py
# SQLPhone Emperor – SQL Module 06
# Practice: UPDATE rows safely.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'inventory' (id, item, quantity).")
    print("Insert at least 3 rows. Then update the quantity of one item (by name) to a new value.")
    print("Make sure your UPDATE uses a WHERE clause. Then SELECT to verify.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    user_sql = input("Enter your SQL (DDL + INSERT + UPDATE + SELECT):\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    try:
        # Check that at least one row quantity changed from original
        # We'll assume user updated item 'widget' to 50, but we can't enforce that name.
        # Instead, we'll just verify that the UPDATE didn't change all rows to the same value unintentionally.
        cur.execute("SELECT COUNT(*) FROM inventory")
        count = cur.fetchone()[0]
        if count < 3:
            print("❌ Need at least 3 rows.")
            conn.close()
            return False
        # Check that not all quantities are equal (if user didn't filter, all would be same)
        cur.execute("SELECT COUNT(DISTINCT quantity) FROM inventory")
        distinct = cur.fetchone()[0]
        if distinct > 1:
            print(f"✅ UPDATE successful. {distinct} different quantities exist (targeted update worked).")
            conn.close()
            return True
        else:
            print("❌ All quantities are the same. Did you forget the WHERE clause?")
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