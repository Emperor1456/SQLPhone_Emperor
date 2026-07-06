# L-69_Materialized_Views_Alternatives.py
# SQLPhone Emperor – SQL Module 08
# Practice: Simulate a materialized view.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'orders' (id, product, amount).")
    print("Insert data. Create a summary table 'order_summary' with product and total_amount.")
    print("Populate it with a SELECT, then refresh it manually (delete and re‑insert).")
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
        # Check that order_summary table has data
        cur.execute("SELECT COUNT(*) FROM order_summary")
        cnt = cur.fetchone()[0]
        if cnt > 0:
            print(f"✅ Summary table created with {cnt} rows.")
            conn.close()
            return True
        else:
            print("❌ Summary table is empty. Did you insert after creating?")
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