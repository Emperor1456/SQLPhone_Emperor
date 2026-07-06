# L-26_HAVING.py
# SQLPhone Emperor – SQL Module 03
# Practice: Filter groups with HAVING.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'departments' (dept_name, employee_count).")
    print("Insert at least 4 rows with different counts.")
    print("Write a query that shows departments with more than 5 employees.")
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
        cur.execute("SELECT COUNT(*) FROM departments")
        if cur.fetchone()[0] < 4:
            print("❌ Need at least 4 rows.")
            conn.close()
            return False
        cur.execute("SELECT dept_name, employee_count FROM departments GROUP BY dept_name HAVING employee_count > 5")
        rows = cur.fetchall()
        if rows:
            print(f"✅ HAVING filter returned {len(rows)} departments with >5 employees.")
            conn.close()
            return True
        else:
            print("❌ No department with >5 employees. Make sure some counts exceed 5.")
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