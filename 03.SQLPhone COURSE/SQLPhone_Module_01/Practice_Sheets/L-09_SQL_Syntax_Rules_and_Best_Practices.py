# L-09_SQL_Syntax_Rules_and_Best_Practices.py
# SQLPhone Emperor – SQL Module 01
# Practice: Write a readable, well-formatted query.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'users' (id, username, email, active).")
    print("Insert sample users (include both active=1 and active=0).")
    print("Write a nicely formatted SELECT with proper indentation, uppercase keywords, and a comment.")
    print("=" * 50)
    user_sql = input("Enter your SQL:\n> ")
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    try:
        cur.execute("SELECT COUNT(*) FROM users WHERE active=1")
        active_count = cur.fetchone()[0]
        if active_count > 0:
            print(f"✅ Query ran. Active users: {active_count}")
            conn.close()
            return True
        else:
            print("❌ No active users found. Ensure you have active=1 rows and the SELECT filters correctly.")
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