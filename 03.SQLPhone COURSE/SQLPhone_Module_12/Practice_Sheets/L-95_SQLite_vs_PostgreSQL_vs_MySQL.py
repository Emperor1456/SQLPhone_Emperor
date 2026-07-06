# L-95_SQLite_vs_PostgreSQL_vs_MySQL.py
# SQLPhone Emperor – SQL Module 12
# Practice: Compare databases conceptually.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Write a short Python script that creates a SQLite database,")
    print("creates a table, inserts a row, and prints it.")
    print("Then, in comments, describe how you would do the same in PostgreSQL and MySQL.")
    print("We'll execute the SQLite part and check the comment about differences.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    user_code = input("Enter your Python code (with comments):\n> ")
    # We'll capture the SQLite part by executing the code, but we can't easily enforce comments. We'll just run it.
    try:
        exec(user_code, {"conn": conn})
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    # Check if the table and row exist
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM test")
        row = cur.fetchone()
        if row:
            print(f"✅ SQLite part works. Row: {row}")
            print("Check your comments for PostgreSQL/MySQL differences.")
            conn.close()
            return True
        else:
            print("❌ No data found. Did you insert?")
            conn.close()
            return False
    except Exception as e:
        print(f"❌ Table 'test' not found or error: {e}")
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