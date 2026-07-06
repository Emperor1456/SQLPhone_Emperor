# L-78_Reusable_Helper_Module.py
# SQLPhone Emperor – SQL Module 09
# Practice: Build a simple Database class.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Write a class `MiniDB` with methods `connect(db_name)`, `execute(sql, params=())`, and `fetch(sql, params=())`.")
    print("Then instantiate it, create a table, insert a row, and fetch it.")
    print("We'll execute your entire code.")
    print("=" * 50)
    user_code = input(">>> ")
    # We'll create a temporary db file
    db_file = "minidb_test.db"
    if os.path.exists(db_file):
        os.unlink(db_file)
    try:
        exec(user_code)
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    # Verify that the class worked by checking the db
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM test")
        row = cur.fetchone()
        if row:
            print(f"✅ MiniDB worked. Row: {row}")
            conn.close()
            os.unlink(db_file)
            return True
        else:
            print("❌ No data found.")
            conn.close()
            os.unlink(db_file)
            return False
    except Exception as e:
        print(f"❌ {e}")
        conn.close()
        os.unlink(db_file)
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