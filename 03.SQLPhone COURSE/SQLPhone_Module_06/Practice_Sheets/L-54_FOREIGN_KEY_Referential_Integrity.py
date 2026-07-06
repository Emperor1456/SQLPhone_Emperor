# L-54_FOREIGN_KEY_Referential_Integrity.py
# SQLPhone Emperor – SQL Module 06
# Practice: Foreign key cascade.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create 'departments' (id, name) and 'employees' (id, name, dept_id, FOREIGN KEY ... ON DELETE CASCADE).")
    print("Enable foreign keys. Insert a department and an employee in it.")
    print("Delete the department; the employee should disappear.")
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
        cur.execute("SELECT COUNT(*) FROM employees")
        if cur.fetchone()[0] != 0:
            print("❌ Employee still exists after deleting department. CASCADE not working.")
            conn.close()
            return False
        print("✅ Employee deleted via CASCADE.")
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