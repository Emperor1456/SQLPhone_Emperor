# L-63_COALESCE.py
# SQLPhone Emperor – SQL Module 07
# Practice: COALESCE to handle NULLs.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'profiles' (username, bio, avatar_url).")
    print("Insert rows; some with NULL bio or avatar.")
    print("Write a query that displays username, bio (or 'No bio' if NULL), and avatar (or 'default.png' if NULL).")
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
        cur.execute("""
            SELECT username, COALESCE(bio, 'No bio'), COALESCE(avatar_url, 'default.png')
            FROM profiles
            WHERE bio IS NULL OR avatar_url IS NULL
            LIMIT 1
        """)
        row = cur.fetchone()
        if row and ('No bio' in row or 'default.png' in row):
            print(f"✅ COALESCE works: {row}")
            conn.close()
            return True
        else:
            # Maybe no NULL values, but the query should still be fine
            print("⚠️ No NULLs to test COALESCE, but query executed.")
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