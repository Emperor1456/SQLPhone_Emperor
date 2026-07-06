# L-82_Index_Usage_Strategy.py
# SQLPhone Emperor – SQL Module 10
# Practice: Create an index and see the difference.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'big' with a column 'value' and insert 1000 rows.")
    print("Run EXPLAIN QUERY PLAN for a query WHERE value = 500 before and after creating an index.")
    print("We'll check if the plan changes from SCAN to SEARCH.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE big (id INTEGER PRIMARY KEY, value INT)")
    cur.executemany("INSERT INTO big (value) VALUES (?)", [(i,) for i in range(1000)])
    conn.commit()
    user_sql = input("Enter your SQL (include EXPLAIN QUERY PLAN and CREATE INDEX):\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    # Check if index was created
    cur.execute("SELECT name FROM sqlite_master WHERE type='index' AND name LIKE 'idx_%'")
    index_names = [r[0] for r in cur.fetchall()]
    if not index_names:
        print("❌ No index created. Use CREATE INDEX.")
        conn.close()
        return False
    # Get query plan for the search
    cur.execute("EXPLAIN QUERY PLAN SELECT * FROM big WHERE value = 500")
    plan = cur.fetchall()
    plan_str = str(plan)
    if 'USING INDEX' in plan_str or 'SEARCH' in plan_str:
        print(f"✅ Index used! Plan: {plan}")
        conn.close()
        return True
    else:
        print(f"❌ Index not used. Plan: {plan}. Check that query matches indexed column.")
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