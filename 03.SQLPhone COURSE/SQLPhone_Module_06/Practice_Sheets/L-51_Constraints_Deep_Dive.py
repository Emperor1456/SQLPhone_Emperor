# L-51_Constraints_Deep_Dive.py
# SQLPhone Emperor – SQL Module 06
# Practice: Apply multiple constraints.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'users' with columns: id INTEGER PRIMARY KEY, username TEXT NOT NULL UNIQUE, age INTEGER CHECK(age>=18), email TEXT UNIQUE.")
    print("Insert a valid row, then try inserting a duplicate username (should fail). Catch the error.")
    print("We'll verify the schema and the failed insert behavior.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    user_sql = input("Enter your SQL (include a failed insert test):\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error (expected if duplicate): {e}")
        # Expected that a duplicate throws an error, but it's okay if user didn't handle it gracefully.
        conn.close()
        return False
    try:
        # Verify constraints exist via PRAGMA (indirectly)
        cur.execute("PRAGMA table_info('users')")
        cols = cur.fetchall()
        if len(cols) < 4:
            print("❌ Table must have 4 columns.")
            conn.close()
            return False
        # Try a duplicate insert now to ensure constraint is active
        try:
            cur.execute("INSERT INTO users (username, age, email) VALUES ('admin', 30, 'admin@test.com')")
            cur.execute("INSERT INTO users (username, age, email) VALUES ('admin', 25, 'admin2@test.com')")
            print("❌ Duplicate username didn't throw an error. Constraint not enforced.")
            conn.close()
            return False
        except sqlite3.IntegrityError:
            print("✅ Duplicate correctly rejected.")
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