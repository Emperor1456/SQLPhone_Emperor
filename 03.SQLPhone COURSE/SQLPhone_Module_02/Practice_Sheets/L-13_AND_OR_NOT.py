# L-13_AND_OR_NOT.py
# SQLPhone Emperor – SQL Module 02
# Practice: Combine conditions with AND, OR, NOT.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'employees' (id, name, dept, salary, status).")
    print("Insert at least 4 rows covering different departments, salaries, statuses (active/inactive).")
    print("Write a SELECT to find active employees in 'Sales' or 'Marketing' with salary > 50000.")
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
            SELECT COUNT(*) FROM employees
            WHERE status='active' AND (dept='Sales' OR dept='Marketing') AND salary>50000
        """)
        count = cur.fetchone()[0]
        if count > 0:
            print(f"✅ Query found {count} employees meeting the criteria.")
            conn.close()
            return True
        else:
            print("❌ No matching rows. Ensure data includes active Sales/Marketing employees with salary>50000.")
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