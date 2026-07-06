# L-08_Comments_in_SQL.py
# SQLPhone Emperor – SQL Module 01
# Practice: Write a well-commented SQL script.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create a file-like SQL script (as a string) that includes a header comment, a commented-out line, and an inline comment.")
    print("Your script must create a table 'logs' (id INTEGER, msg TEXT) and insert one row.")
    print("We will execute it and check that comments don't cause errors and the insert succeeds.")
    print("=" * 50)
    user_sql = input("Enter your full SQL script:\n> ")
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
        cur.execute("SELECT COUNT(*) FROM logs")
        count = cur.fetchone()[0]
        if count == 1:
            print("✅ Script executed successfully. Comments did not interfere.")
            conn.close()
            return True
        else:
            print("❌ Expected 1 row in 'logs'. Check your INSERT.")
            conn.close()
            return False
    except Exception as e:
        print(f"❌ Table 'logs' doesn't exist or other error: {e}")
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