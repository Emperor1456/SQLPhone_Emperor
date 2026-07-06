# L-18_LIKE.py
# SQLPhone Emperor – SQL Module 02
# Practice: Pattern matching with LIKE.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'users' (id, username, email).")
    print("Insert at least 4 rows, some with emails ending in '@example.com', some not.")
    print("Write a query that selects users whose email LIKE '%@example.com'.")
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
        cur.execute("SELECT COUNT(*) FROM users WHERE email LIKE '%@example.com'")
        count = cur.fetchone()[0]
        if count > 0:
            print(f"✅ Query found {count} users with example.com emails.")
            conn.close()
            return True
        else:
            print("❌ No users with '@example.com' email. Ensure you inserted such rows.")
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