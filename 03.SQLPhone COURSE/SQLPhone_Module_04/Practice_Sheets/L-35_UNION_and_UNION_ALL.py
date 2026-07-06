# L-35_UNION_and_UNION_ALL.py
# SQLPhone Emperor – SQL Module 04
# Practice: UNION and UNION ALL.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create two tables 'current_employees' and 'former_employees', both with columns (id, name).")
    print("Insert rows; make sure some names appear in both tables.")
    print("Write a UNION query to get a combined list without duplicates.")
    print("Write a UNION ALL query to get all rows (including duplicates).")
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
        # Check union removes duplicates
        cur.execute("SELECT COUNT(*) FROM (SELECT name FROM current_employees UNION SELECT name FROM former_employees)")
        union_count = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM (SELECT name FROM current_employees UNION ALL SELECT name FROM former_employees)")
        union_all_count = cur.fetchone()[0]
        if union_all_count > union_count:
            print(f"✅ UNION ({union_count} rows) removed duplicates compared to UNION ALL ({union_all_count} rows).")
            conn.close()
            return True
        else:
            print("❌ UNION ALL should have more rows than UNION if duplicates exist. Insert duplicate names.")
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