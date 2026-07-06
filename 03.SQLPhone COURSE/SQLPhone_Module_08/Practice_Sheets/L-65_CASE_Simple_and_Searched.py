# L-65_CASE_Simple_and_Searched.py
# SQLPhone Emperor – SQL Module 08
# Practice: CASE expressions.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'students' (name, score).")
    print("Insert at least 4 rows with different scores.")
    print("Write a query that shows name, score, and a grade column using a searched CASE:")
    print("score >= 90 -> 'A', >= 80 -> 'B', >= 70 -> 'C', else 'F'.")
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
        cur.execute("SELECT name, score, CASE WHEN score>=90 THEN 'A' WHEN score>=80 THEN 'B' WHEN score>=70 THEN 'C' ELSE 'F' END FROM students")
        rows = cur.fetchall()
        if len(rows) < 4:
            print("❌ Need at least 4 rows.")
            conn.close()
            return False
        print(f"✅ Graded {len(rows)} students. Sample: {rows[0]}")
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