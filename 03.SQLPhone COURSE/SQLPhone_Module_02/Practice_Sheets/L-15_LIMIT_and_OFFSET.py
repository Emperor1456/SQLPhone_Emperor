# L-15_LIMIT_and_OFFSET.py
# SQLPhone Emperor – SQL Module 02
# Practice: Paginate results.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'items' (id INTEGER PRIMARY KEY, name TEXT, price REAL).")
    print("Insert at least 10 rows with varied prices.")
    print("Write a query to retrieve the 3rd page of results when ordered by price DESC, page size=3.")
    print("(That is rows 7-9, using OFFSET 6 LIMIT 3).")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    user_sql = input("Enter your SQL (include the paginated query):\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    try:
        cur.execute("SELECT COUNT(*) FROM items")
        count = cur.fetchone()[0]
        if count < 10:
            print("❌ Need at least 10 rows.")
            conn.close()
            return False
        cur.execute("SELECT * FROM items ORDER BY price DESC LIMIT 3 OFFSET 6")
        rows = cur.fetchall()
        if len(rows) == 3:
            print(f"✅ Pagination successful. Third page returned {len(rows)} rows.")
            conn.close()
            return True
        else:
            print(f"❌ Expected 3 rows for page 3, but got {len(rows)}. Check data and pagination.")
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