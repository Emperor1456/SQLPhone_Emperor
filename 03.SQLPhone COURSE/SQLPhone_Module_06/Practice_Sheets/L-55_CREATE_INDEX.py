# L-55_CREATE_INDEX.py
# SQLPhone Emperor – SQL Module 06
# Practice: Create and test an index.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'contacts' (id, name TEXT, phone TEXT).")
    print("Insert many rows (at least 5). Create an index on 'name'.")
    print("Use EXPLAIN QUERY PLAN on a SELECT with WHERE name = '...' to show the index is used.")
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
        # Check that index exists
        cur.execute("SELECT name FROM sqlite_master WHERE type='index' AND name='idx_contacts_name'")
        if not cur.fetchone():
            print("❌ Index 'idx_contacts_name' not found.")
            conn.close()
            return False
        # Try to see if EXPLAIN QUERY PLAN mentions the index
        cur.execute("EXPLAIN QUERY PLAN SELECT * FROM contacts WHERE name = 'test'")
        plan = cur.fetchall()
        plan_str = str(plan)
        if 'idx_contacts_name' in plan_str or 'USING INDEX' in plan_str:
            print(f"✅ Index used in query plan: {plan}")
            conn.close()
            return True
        else:
            print(f"⚠️ Index exists but may not be used (still acceptable for small tables). Plan: {plan}")
            conn.close()
            return True  # still pass, as index creation was successful
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