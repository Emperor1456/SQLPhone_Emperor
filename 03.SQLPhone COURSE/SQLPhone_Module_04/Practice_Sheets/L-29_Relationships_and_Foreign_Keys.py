# L-29_Relationships_and_Foreign_Keys.py
# SQLPhone Emperor – SQL Module 04
# Practice: Define relationships and foreign keys.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create two tables: 'departments' (id, name) and 'employees' (id, name, dept_id).")
    print("Add a FOREIGN KEY on dept_id referencing departments(id).")
    print("Insert a department, then insert an employee with that dept_id.")
    print("Then try to insert an employee with a non‑existent dept_id (should fail if FK is enforced).")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    user_sql = input("Enter your SQL (include PRAGMA if needed):\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    try:
        # Verify that the FK violation fails
        # We'll try an invalid insert ourselves to confirm enforcement
        try:
            cur.execute("INSERT INTO employees (name, dept_id) VALUES ('Test', 9999)")
            conn.commit()
            print("❌ Foreign key NOT enforced. Make sure PRAGMA foreign_keys = ON and table definition includes FOREIGN KEY.")
            conn.close()
            return False
        except sqlite3.IntegrityError:
            print("✅ Foreign key enforced correctly. Invalid insert blocked.")
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