# L-50_ALTER_TABLE.py
# SQLPhone Emperor – SQL Module 06
# Practice: ALTER TABLE.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'devices' (id INTEGER PRIMARY KEY, name TEXT).")
    print("Then add a column 'os' TEXT using ALTER TABLE.")
    print("Then rename the column 'name' to 'device_name'.")
    print("Finally, insert a row with the new schema.")
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
        # Check that 'device_name' and 'os' columns exist
        cur.execute("PRAGMA table_info('devices')")
        cols = [c[1] for c in cur.fetchall()]  # column names
        if 'device_name' in cols and 'os' in cols:
            print(f"✅ Schema updated. Columns: {cols}")
            conn.close()
            return True
        else:
            print(f"❌ Expected columns 'device_name' and 'os', got {cols}")
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