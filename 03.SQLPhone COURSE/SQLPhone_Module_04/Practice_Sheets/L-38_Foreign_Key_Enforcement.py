# L-38_Foreign_Key_Enforcement.py
# SQLPhone Emperor – SQL Module 04
# Practice: Test foreign key actions.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create tables 'categories' (id, name) and 'items' (id, name, cat_id) with FK ON DELETE CASCADE.")
    print("Enable foreign keys. Insert a category and an item in that category.")
    print("Delete the category; the item should be deleted automatically.")
    print("Show by querying items after deletion (should be empty).")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    user_sql = input("Enter your SQL:\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    try:
        # Check that the item was cascade deleted
        cur.execute("SELECT COUNT(*) FROM items")
        cnt = cur.fetchone()[0]
        if cnt == 0:
            print("✅ Item deleted via CASCADE. Foreign key action works.")
            conn.close()
            return True
        else:
            print(f"❌ Expected 0 items, but {cnt} remain. Check ON DELETE CASCADE and PRAGMA.")
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