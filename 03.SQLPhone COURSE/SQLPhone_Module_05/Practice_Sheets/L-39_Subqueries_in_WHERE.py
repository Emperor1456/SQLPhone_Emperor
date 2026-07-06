# L-39_Subqueries_in_WHERE.py
# SQLPhone Emperor – SQL Module 05
# Practice: Scalar subquery in WHERE.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'employees' (id, name, salary).")
    print("Insert at least 4 rows.")
    print("Write a query to find employees earning above the average salary using a subquery in WHERE.")
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
        if cur.fetchone()[0] < 4:
            print("❌ Need at least 4 rows.")
            conn.close()
            return False
        # Check that the query returns only rows where salary > avg
        cur.execute("SELECT AVG(salary) FROM employees")
        avg = cur.fetchone()[0]
        cur.execute("SELECT salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees)")
        rows = cur.fetchall()
        if rows:
            above_avg = [r[0] for r in rows]
            if min(above_avg) > avg:
                print(f"✅ Query returned {len(rows)} employees above average ({avg:.2f}).")
                conn.close()
                return True
            else:
                print("❌ Some returned salaries are not above average. Check your WHERE clause.")
                conn.close()
                return False
        else:
            print("❌ No employees above average? Ensure data has varied salaries.")
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