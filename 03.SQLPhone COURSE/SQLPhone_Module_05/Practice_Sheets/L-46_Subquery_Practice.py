# L-46_Subquery_Practice.py
# SQLPhone Emperor – SQL Module 05
# Practice: Full subquery challenge set.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 MODULE 05 CHALLENGE: Subqueries & CTEs")
    print("Create tables: departments, employees, projects, assignments.")
    print("Insert sample data. Write the five required queries from the lecture.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    user_sql = input("Enter your full SQL script:\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    try:
        # Minimum data check
        cur.execute("SELECT COUNT(*) FROM employees")
        emp = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM departments")
        dep = cur.fetchone()[0]
        if emp < 3 or dep < 2:
            print("❌ Need at least 3 employees and 2 departments.")
            conn.close()
            return False
        # Test query 1: above department avg (correlated)
        cur.execute("""
            SELECT e.name FROM employees e
            WHERE e.salary > (SELECT AVG(salary) FROM employees WHERE dept_id = e.dept_id)
        """)
        q1 = cur.fetchall()
        # Test query 2: EXISTS department with high earner
        cur.execute("""
            SELECT d.name FROM departments d
            WHERE EXISTS (SELECT 1 FROM employees e WHERE e.dept_id = d.id AND e.salary > 100000)
        """)
        q2 = cur.fetchall()
        # If we got here, queries executed
        print(f"✅ Queries executed. Q1 (above avg): {len(q1)} employees; Q2 (EXISTS): {[r[0] for r in q2]}")
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