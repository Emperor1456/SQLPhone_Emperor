# L-17_IN.py
# SQLPhone Emperor – SQL Module 02
# Practice: Filter with IN.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'contacts' (id, name, city).")
    print("Insert at least 5 rows covering different cities.")
    print("Write a query that selects contacts whose city is in ('London','Paris','Berlin').")
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
        cur.execute("SELECT COUNT(*) FROM contacts WHERE city IN ('London','Paris','Berlin')")
        count = cur.fetchone()[0]
        if count > 0:
            print(f"✅ Query returned {count} contacts in those cities.")
            conn.close()
            return True
        else:
            print("❌ No matching cities found. Insert data with at least one of those cities.")
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