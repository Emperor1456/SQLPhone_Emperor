# L-93_Movie_Rating_System.py
# SQLPhone Emperor – SQL Module 11
# Practice: Movie ratings.

import sqlite3, os

DB = "movies.db"

def task():
    print("=" * 50)
    print("🧱 PROJECT 7: Movie Rating System")
    print("Create User, Movie, Rating tables. Insert diverse ratings.")
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
        for tbl in ['User','Movie','Rating']:
            cur.execute(f"SELECT COUNT(*) FROM {tbl}")
            if cur.fetchone()[0] == 0:
                print(f"❌ Table {tbl} empty.")
                conn.close()
                return False
        print("✅ Ratings database ready. Check average ratings per movie.")
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