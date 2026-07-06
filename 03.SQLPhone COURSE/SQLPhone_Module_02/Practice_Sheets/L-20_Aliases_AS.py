# L-20_Aliases_AS.py
# SQLPhone Emperor – SQL Module 02
# Practice: Use aliases for columns and tables.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create two tables: 'departments' (id, dept_name) and 'staff' (id, name, dept_id).")
    print("Insert at least 3 departments and 4 staff members assigned to them.")
    print("Write a query that joins the tables and uses aliases to display 'Employee Name' and 'Department'.")
    print("Also alias the tables as 's' and 'd'.")
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
        cur.execute("""
            SELECT s.name AS "Employee Name", d.dept_name AS "Department"
            FROM staff s
            JOIN departments d ON s.dept_id = d.id
        """)
        rows = cur.fetchall()
        if len(rows) > 0:
            print(f"✅ Join with aliases returned {len(rows)} rows. Example: {rows[0]}")
            conn.close()
            return True
        else:
            print("❌ Join returned no rows. Ensure data and join condition correct.")
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