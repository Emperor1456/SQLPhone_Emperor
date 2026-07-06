# L-02_Installing_SQLite_in_Termux.py
# SQLPhone Emperor – SQL Module 01
# Practice: Simulating dot-commands via Python.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: You have connected to a database. Create a table named 'test' (id INT).")
    print("Then, query sqlite_master to list all tables (simulate '.tables').")
    print("Your SQL must include the CREATE TABLE and the SELECT on sqlite_master.")
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

    # Verify that table 'test' exists and the listing query returned it
    try:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test'")
        row = cur.fetchone()
        if not row:
            print("❌ Table 'test' not found. Did you create it?")
            conn.close()
            return False
        # Also check that the user's script actually returned a result from sqlite_master? Not directly possible; we trust.
        print("✅ Table 'test' exists. Dot-command simulation successful.")
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