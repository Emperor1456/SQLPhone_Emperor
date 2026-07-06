# L-19_NULL_Values.py
# SQLPhone Emperor – SQL Module 02
# Practice: Handle NULLs.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'tasks' (id, description, completed_date TEXT).")
    print("Insert at least 3 rows, some with completed_date NULL (not finished).")
    print("Write a query that selects all tasks where completed_date IS NULL.")
    print("Also write a query that returns description and 'Pending' if completed_date is NULL using COALESCE.")
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
        cur.execute("SELECT COUNT(*) FROM tasks WHERE completed_date IS NULL")
        null_count = cur.fetchone()[0]
        if null_count == 0:
            print("❌ Insert at least one row with completed_date NULL.")
            conn.close()
            return False
        print(f"✅ Query found {null_count} pending tasks. COALESCE should show 'Pending' for those.")
        conn.close()
        return True
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