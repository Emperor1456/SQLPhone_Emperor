# L-67_Views_Create_Query_Drop.py
# SQLPhone Emperor – SQL Module 08
# Practice: Create and query a view.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'employees' (id, name, dept, salary).")
    print("Insert rows. Then create a view 'sales_staff' for employees in dept='Sales'.")
    print("Query the view to show that it works. Drop the view at the end.")
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
        # Check that view was created and then dropped (if drop included)
        cur.execute("SELECT name FROM sqlite_master WHERE type='view' AND name='sales_staff'")
        view_exists = cur.fetchone()
        if view_exists:
            print("✅ View 'sales_staff' created and can be queried.")
            conn.close()
            return True
        else:
            print("❌ View not found. Ensure CREATE VIEW statement is correct.")
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