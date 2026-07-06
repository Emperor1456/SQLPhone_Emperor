# L-22_SUM_and_AVG.py
# SQLPhone Emperor – SQL Module 03
# Practice: SUM and AVG.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'sales' (id, product, amount).")
    print("Insert at least 4 rows with different amounts.")
    print("Write queries to show:")
    print("1. Total sum of amounts.")
    print("2. Average amount.")
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
        cur.execute("SELECT COUNT(*) FROM sales")
        if cur.fetchone()[0] < 4:
            print("❌ Need at least 4 rows.")
            conn.close()
            return False
        cur.execute("SELECT SUM(amount) FROM sales")
        total = cur.fetchone()[0]
        cur.execute("SELECT AVG(amount) FROM sales")
        avg = cur.fetchone()[0]
        if total is not None and avg is not None:
            print(f"✅ Total: {total}, Average: {avg:.2f}")
            conn.close()
            return True
        else:
            print("❌ Aggregation failed. Check data types.")
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