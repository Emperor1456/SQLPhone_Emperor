# L-76_Executing_sql_Files_from_Python.py
# SQLPhone Emperor – SQL Module 09
# Practice: Execute SQL from file.

import sqlite3, os

def task():
    print("=" * 50)
    print("🧱 TASK: I'll create a temp file 'test.sql' with a CREATE TABLE and INSERT.")
    print("Write Python code to read and execute it using conn.")
    print("=" * 50)
    sql = "CREATE TABLE temp(id INT); INSERT INTO temp VALUES(42);"
    with open("test.sql", "w") as f:
        f.write(sql)
    conn = sqlite3.connect(":memory:")
    user_code = input(">>> ")
    try:
        exec(user_code, {"conn": conn, "os": os})
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        os.unlink("test.sql")
        return False
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM temp")
        row = cur.fetchone()
        if row and row[0] == 42:
            print("✅ SQL file executed correctly.")
            conn.close()
            os.unlink("test.sql")
            return True
        else:
            print("❌ Expected row with 42 not found.")
            conn.close()
            os.unlink("test.sql")
            return False
    except Exception as e:
        print(f"❌ Table doesn't exist or error: {e}")
        conn.close()
        os.unlink("test.sql")
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