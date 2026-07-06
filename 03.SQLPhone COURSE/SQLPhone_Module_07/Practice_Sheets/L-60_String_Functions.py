# L-60_String_Functions.py
# SQLPhone Emperor – SQL Module 07
# Practice: String manipulation.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'users' (id, full_name, email).")
    print("Insert at least 3 rows.")
    print("Write a query that extracts the first 3 characters of the name and appends '...' (use SUBSTR and ||).")
    print("Also convert email to lowercase using LOWER().")
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
        # Check that at least one row has a valid transformed email and short name
        cur.execute("SELECT SUBSTR(full_name, 1, 3) || '...', LOWER(email) FROM users LIMIT 1")
        row = cur.fetchone()
        if row and len(row[0]) == 6 and row[1].islower():
            print(f"✅ Short name: {row[0]}, Email: {row[1]}")
            conn.close()
            return True
        else:
            print(f"❌ String transformation not as expected. Row: {row}")
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