# L-44_Correlated_Subqueries.py
# SQLPhone Emperor – SQL Module 05
# Practice: Correlated subquery.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'employees' (id, name, department, salary).")
    print("Insert at least 6 rows across 2 departments with varying salaries.")
    print("Write a correlated subquery to find employees who earn more than the average salary of their own department.")
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
        cur.execute("SELECT COUNT(*) FROM employees")
        if cur.fetchone()[0] < 6:
            print("❌ Need at least 6 employees.")
            conn.close()
            return False
        # Verify the correlated query works
        cur.execute("""
            SELECT e.name, e.salary, e.department
            FROM employees e
            WHERE e.salary > (
                SELECT AVG(salary) FROM employees
                WHERE department = e.department
            )
        """)
        rows = cur.fetchall()
        if rows:
            print(f"✅ Correlated subquery returned {len(rows)} employees above their department average.")
            conn.close()
            return True
        else:
            print("❌ No employees above department average. Ensure data has variation within departments.")
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