# L-72_Creating_Tables_via_Python.py
# SQLPhone Emperor – SQL Module 09
# Practice: Execute CREATE TABLE via Python.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Write Python code to create a table 'products' with id, name, price. Include IF NOT EXISTS.")
    print("We will execute your code, then check the schema.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    user_code = input(">>> ")
    try:
        exec(user_code, {"conn": conn})
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    cur = conn.cursor()
    try:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products'")
        if cur.fetchone():
            print("✅ Table 'products' exists.")
            conn.close()
            return True
        else:
            print("❌ Table not found.")
            conn.close()
            return False
    except Exception as e:
        print(f"❌ {e}")
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