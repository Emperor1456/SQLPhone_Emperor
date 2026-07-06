# L-48_DELETE_Removing_Rows.py
# SQLPhone Emperor – SQL Module 06
# Practice: DELETE rows safely.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'logs' (id, message, level).")
    print("Insert rows with level 'INFO', 'ERROR', etc.")
    print("Write a DELETE that removes all rows with level = 'DEBUG'.")
    print("Then SELECT to confirm they are gone, but others remain.")
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
        cur.execute("SELECT COUNT(*) FROM logs")
        total = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM logs WHERE level='DEBUG'")
        debug_count = cur.fetchone()[0]
        if debug_count > 0:
            print(f"❌ DEBUG rows still exist ({debug_count}). DELETE must have failed or used wrong condition.")
            conn.close()
            return False
        if total == 0:
            print("❌ All rows deleted. Ensure you kept non‑DEBUG rows.")
            conn.close()
            return False
        print(f"✅ DEBUG rows removed. {total} rows remain (non‑DEBUG).")
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