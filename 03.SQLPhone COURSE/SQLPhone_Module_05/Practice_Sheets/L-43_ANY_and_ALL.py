# L-43_ANY_and_ALL.py
# SQLPhone Emperor – SQL Module 05
# Practice: ANY and ALL comparisons.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'scores' (player TEXT, points INTEGER).")
    print("Insert at least 4 rows.")
    print("Write a query to find players with points greater than ANY score from a specific player, e.g., 'Alice'.")
    print("Also write a query to find players with points greater than ALL scores of 'Alice'.")
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
        # Ensure 'Alice' exists
        cur.execute("SELECT COUNT(*) FROM scores WHERE player='Alice'")
        if cur.fetchone()[0] == 0:
            print("❌ Insert a player named 'Alice' with at least one score.")
            conn.close()
            return False
        # Test > ANY
        cur.execute("""
            SELECT player, points FROM scores
            WHERE points > ANY (SELECT points FROM scores WHERE player='Alice')
            AND player != 'Alice'
        """)
        any_rows = cur.fetchall()
        # Test > ALL
        cur.execute("""
            SELECT player, points FROM scores
            WHERE points > ALL (SELECT points FROM scores WHERE player='Alice')
            AND player != 'Alice'
        """)
        all_rows = cur.fetchall()
        if any_rows or all_rows:
            print(f"✅ > ANY found: {any_rows}")
            print(f"✅ > ALL found: {all_rows}")
            conn.close()
            return True
        else:
            print("❌ No rows returned. Ensure Alice has some scores and other players have higher/lower points.")
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