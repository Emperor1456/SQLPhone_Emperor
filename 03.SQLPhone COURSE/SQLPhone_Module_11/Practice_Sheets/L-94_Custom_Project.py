# L-94_Custom_Project.py
# SQLPhone Emperor – SQL Module 11
# Practice: Your own project.

import sqlite3, os

DB = "custom_project.db"

def task():
    print("=" * 50)
    print("🧱 PROJECT 8: Custom Database")
    print("Design and implement any database of your choice with at least 4 tables.")
    print("Include a many‑to‑many relationship and constraints.")
    print("We'll verify that you have the required number of tables and data.")
    print("=" * 50)
    if os.path.exists(DB):
        os.remove(DB)
    user_sql = input("Paste your full SQL script:\n> ")
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    try:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [r[0] for r in cur.fetchall()]
        if len(tables) < 4:
            print(f"❌ Need at least 4 tables, got {len(tables)}: {tables}")
            conn.close()
            return False
        # Check each table has at least 5 rows
        for t in tables:
            cur.execute(f"SELECT COUNT(*) FROM {t}")
            if cur.fetchone()[0] < 5:
                print(f"❌ Table {t} has fewer than 5 rows.")
                conn.close()
                return False
        print(f"✅ Custom project with {len(tables)} tables and sufficient data. Great job!")
        conn.close()
        return True
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