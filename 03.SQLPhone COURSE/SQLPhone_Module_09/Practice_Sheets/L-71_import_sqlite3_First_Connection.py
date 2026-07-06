# L-71_import_sqlite3_First_Connection.py
# SQLPhone Emperor – SQL Module 09
# Practice: Connect and create a table.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Connect to ':memory:', create table 'test' (id INT), insert a row, and fetch it.")
    print("We will execute your Python code snippet and verify the row.")
    print("Enter your code (use 'conn' for connection, we'll provide it):")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    user_code = input(">>> ")
    try:
        exec(user_code, {"conn": conn})
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    # Verify
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM test")
        row = cur.fetchone()
        if row:
            print(f"✅ Row found: {row}")
            conn.close()
            return True
        else:
            print("❌ No row in table 'test'.")
            conn.close()
            return False
    except Exception as e:
        print(f"❌ Table 'test' doesn't exist or other error: {e}")
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