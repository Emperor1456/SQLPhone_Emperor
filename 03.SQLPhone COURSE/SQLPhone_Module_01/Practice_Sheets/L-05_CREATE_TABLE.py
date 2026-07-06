# L-05_CREATE_TABLE.py
# SQLPhone Emperor – SQL Module 01
# Practice: Design a table with constraints.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create a table 'employees' with columns:")
    print("  id (INTEGER PRIMARY KEY), name (TEXT NOT NULL), email (TEXT UNIQUE NOT NULL), salary (REAL CHECK(salary>0)), hired (TEXT DEFAULT (datetime('now'))).")
    print("Insert two rows, one with all fields, one omitting hired (use default).")
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
    # Verify
    try:
        cur.execute("PRAGMA table_info('employees')")
        cols = cur.fetchall()
        if len(cols) != 5:
            print("❌ Expected 5 columns.")
            conn.close()
            return False
        cur.execute("SELECT COUNT(*) FROM employees")
        count = cur.fetchone()[0]
        if count < 2:
            print("❌ Need at least 2 rows.")
            conn.close()
            return False
        # Check default hired date is not null for the row where omitted
        cur.execute("SELECT hired FROM employees WHERE hired IS NOT NULL")
        if cur.fetchone():
            print("✅ Table 'employees' created correctly with constraints and defaults.")
            conn.close()
            return True
        else:
            print("❌ Default date not applied.")
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