# L-92_Expense_Tracker.py
# SQLPhone Emperor – SQL Module 11
# Practice: Expense tracker.

import sqlite3, os

DB = "expenses.db"

def task():
    print("=" * 50)
    print("🧱 PROJECT 6: Expense Tracker")
    print("Create Category and Expense tables. Populate 20+ expenses.")
    print("We'll check the data.")
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
        cur.execute("SELECT COUNT(*) FROM Expense")
        cnt = cur.fetchone()[0]
        if cnt < 20:
            print(f"❌ Need at least 20 expenses, got {cnt}.")
            conn.close()
            return False
        cur.execute("SELECT COUNT(*) FROM Category")
        if cur.fetchone()[0] == 0:
            print("❌ Category table empty.")
            conn.close()
            return False
        print("✅ Expense tracker data ready. Run your monthly summary queries.")
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