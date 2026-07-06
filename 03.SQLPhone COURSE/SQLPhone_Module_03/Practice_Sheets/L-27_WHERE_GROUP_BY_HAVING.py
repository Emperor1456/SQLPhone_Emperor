# L-27_WHERE_GROUP_BY_HAVING.py
# SQLPhone Emperor – SQL Module 03
# Practice: Combine all clauses.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'transactions' (id, client, amount, status).")
    print("Insert rows with status 'paid' and 'pending', various amounts.")
    print("Write a query that shows total amount per client for paid transactions, only for clients with total > 100.")
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
        cur.execute("SELECT COUNT(*) FROM transactions")
        if cur.fetchone()[0] < 3:
            print("❌ Need at least 3 rows.")
            conn.close()
            return False
        cur.execute("""
            SELECT client, SUM(amount) as total
            FROM transactions
            WHERE status='paid'
            GROUP BY client
            HAVING total > 100
        """)
        rows = cur.fetchall()
        if rows:
            print(f"✅ Query returned {len(rows)} clients meeting criteria.")
            conn.close()
            return True
        else:
            print("❌ No client with paid total >100. Adjust data.")
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