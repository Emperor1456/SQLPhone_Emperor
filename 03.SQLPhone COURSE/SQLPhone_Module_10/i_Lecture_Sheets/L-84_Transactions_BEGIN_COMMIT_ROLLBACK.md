# L-84_Transactions_BEGIN_COMMIT_ROLLBACK.py
# SQLPhone Emperor – SQL Module 10
# Practice: Use a transaction to ensure atomicity.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'accounts' (id, balance). Insert two rows with 100 each.")
    print("Write a transaction that transfers 50 from account 1 to account 2.")
    print("If the final balance of account 1 is negative, rollback. Otherwise commit.")
    print("We'll execute your SQL script.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE accounts (id INTEGER PRIMARY KEY, balance REAL)")
    cur.executemany("INSERT INTO accounts (id, balance) VALUES (?, ?)", [(1, 100.0), (2, 100.0)])
    conn.commit()
    user_sql = input("Enter your SQL (include BEGIN, UPDATEs, and COMMIT/ROLLBACK):\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    # Verify balances
    cur.execute("SELECT balance FROM accounts WHERE id=1")
    bal1 = cur.fetchone()[0]
    cur.execute("SELECT balance FROM accounts WHERE id=2")
    bal2 = cur.fetchone()[0]
    if bal1 == 50.0 and bal2 == 150.0:
        print("✅ Transfer committed correctly (50 from 1 to 2).")
        conn.close()
        return True
    else:
        print(f"❌ Balances not as expected: account1={bal1}, account2={bal2}. Check your logic.")
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