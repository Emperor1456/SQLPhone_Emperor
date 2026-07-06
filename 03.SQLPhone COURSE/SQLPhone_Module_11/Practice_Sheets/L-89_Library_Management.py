# L-89_Library_Management.py
# SQLPhone Emperor – SQL Module 11
# Practice: Library management.

import sqlite3, os

DB = "library.db"

def task():
    print("=" * 50)
    print("🧱 PROJECT 3: Library Management")
    print("Create Book, Member, Loan tables. Populate and query.")
    print("We'll check tables and data.")
    print("=" * 50)
    if os.path.exists(DB):
        os.remove(DB)
    user_sql = input("Paste your SQL:\n> ")
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
        for tbl in ['Book','Member','Loan']:
            cur.execute(f"SELECT COUNT(*) FROM {tbl}")
            if cur.fetchone()[0] == 0:
                print(f"❌ Table {tbl} empty.")
                conn.close()
                return False
        print("✅ Library database ready. Check your overdue queries.")
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