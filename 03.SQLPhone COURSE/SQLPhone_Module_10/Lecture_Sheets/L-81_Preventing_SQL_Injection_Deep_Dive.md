# L-81_Preventing_SQL_Injection_Deep_Dive.py
# SQLPhone Emperor – SQL Module 10
# Practice: Exploit a vulnerable query and fix it.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: We have a table 'users' with a row 'admin'.")
    print("A vulnerable SELECT uses string formatting. Try to inject SQL to return the admin row without knowing the name.")
    print("Then rewrite the query using parameterized substitution to prevent injection.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    conn.execute("INSERT INTO users (username, password) VALUES ('admin', 'secret')")
    conn.commit()
    # Part 1: Show vulnerable example
    print("Vulnerable query: SELECT * FROM users WHERE username = '{}'".format(input("Enter username: ")))
    user_input = input("Try injection (e.g., ' OR 1=1 --): ")
    try:
        # Simulate vulnerable execution (do not really use format in production)
        cur = conn.execute("SELECT * FROM users WHERE username = '{}'".format(user_input))
        rows = cur.fetchall()
        if len(rows) > 1 or (len(rows) == 1 and rows[0][1] == 'admin'):
            print(f"⚠️ Injection likely succeeded! Returned rows: {rows}")
        else:
            print("No extra rows returned.")
    except Exception as e:
        print(f"Error: {e}")
    # Part 2: Fix
    print("\nNow write a safe parameterized query using ?:")
    safe_sql = input("Enter your safe query (should use ? placeholder): ")
    # We'll execute with a safe parameter 'admin' to see if it works.
    try:
        cur = conn.execute(safe_sql, ('admin',))
        row = cur.fetchone()
        if row and row[1] == 'admin':
            print("✅ Safe query works correctly.")
            conn.close()
            return True
        else:
            print("❌ Safe query did not return admin.")
            conn.close()
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
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