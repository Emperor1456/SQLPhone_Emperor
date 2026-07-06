# L-34_Self_Join.py
# SQLPhone Emperor – SQL Module 04
# Practice: Self‑join.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'staff' (id, name, manager_id).")
    print("Insert rows forming a hierarchy: some employees have a manager (manager_id points to another staff.id).")
    print("Write a self‑join query that displays employee name and their manager's name.")
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
        cur.execute("SELECT COUNT(*) FROM staff")
        if cur.fetchone()[0] < 3:
            print("❌ Need at least 3 staff rows.")
            conn.close()
            return False
        cur.execute("""
            SELECT e.name, m.name
            FROM staff e
            LEFT JOIN staff m ON e.manager_id = m.id
        """)
        rows = cur.fetchall()
        if rows:
            print(f"✅ Self‑join returned {len(rows)} rows. Sample: {rows[0]}")
            conn.close()
            return True
        else:
            print("❌ Self‑join returned no rows. Check manager_id values.")
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