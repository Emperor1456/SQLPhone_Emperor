# L-21_COUNT.py
# SQLPhone Emperor – SQL Module 03
# Practice: COUNT rows.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'employees' (id, name, department, phone).")
    print("Insert at least 4 rows; leave phone NULL for one row.")
    print("Write queries:")
    print("1. Total number of employees (COUNT(*)).")
    print("2. Number of employees with a phone (COUNT(phone)).")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    user_sql = input("Enter your SQL (include both queries separated by ;):\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    try:
        # Check table exists
        cur.execute("SELECT COUNT(*) FROM employees")
        total = cur.fetchone()[0]
        if total < 4:
            print("❌ Need at least 4 rows.")
            conn.close()
            return False
        cur.execute("SELECT COUNT(phone) FROM employees")
        phone_count = cur.fetchone()[0]
        if phone_count >= total:
            print("❌ At least one row should have phone NULL to see difference.")
            conn.close()
            return False
        print(f"✅ Total employees: {total}, with phone: {phone_count}.")
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