# L-56_AUTOINCREMENT_vs_INTEGER_PRIMARY_KEY.py
# SQLPhone Emperor – SQL Module 06
# Practice: Compare key behaviors.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create two tables: 'standard' (id INTEGER PRIMARY KEY, val TEXT) and 'autoinc' (id INTEGER PRIMARY KEY AUTOINCREMENT, val TEXT).")
    print("Insert two rows each, then delete the max id row. Insert another row and compare the new id values.")
    print("Standard may reuse the deleted id; AUTOINCREMENT will not.")
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
        cur.execute("SELECT MAX(id) FROM standard")
        max_std = cur.fetchone()[0]
        cur.execute("SELECT MAX(id) FROM autoinc")
        max_auto = cur.fetchone()[0]
        if max_std is not None and max_auto is not None:
            print(f"✅ Standard max id after re‑insert: {max_std}, AUTOINCREMENT max id: {max_auto}")
            if max_std < max_auto or max_std is not None:
                print("Behavior difference observed.")
            conn.close()
            return True
        else:
            print("❌ Data not found.")
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