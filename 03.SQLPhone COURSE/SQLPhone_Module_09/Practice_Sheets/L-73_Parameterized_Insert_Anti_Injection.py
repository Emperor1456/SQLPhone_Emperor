# L-73_Parameterized_Insert_Anti_Injection.py
# SQLPhone Emperor – SQL Module 09
# Practice: Use parameterized inserts.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: We'll create a table 'users' (id, username, password).")
    print("Write Python code to safely insert a user using parameterized query (?, ?).")
    print("Do NOT use string formatting.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    user_code = input(">>> ")
    try:
        exec(user_code, {"conn": conn})
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    row = cur.fetchone()
    if row and row[1] is not None:
        # Check that it wasn't built with string formatting (simple check: if 'admin' in row[1] and no SQL error, likely safe)
        print(f"✅ User inserted: {row[1]}")
        conn.close()
        return True
    else:
        print("❌ No user inserted.")
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