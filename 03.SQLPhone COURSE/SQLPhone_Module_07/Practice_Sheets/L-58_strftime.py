# L-58_strftime.py
# SQLPhone Emperor – SQL Module 07
# Practice: Custom date formatting with strftime.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Use the 'events' table (or create another).")
    print("Write a query that shows each event's name and its formatted date as 'DD/MM/YYYY'.")
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
        # Check that strftime output matches DD/MM/YYYY pattern
        cur.execute("SELECT strftime('%d/%m/%Y', event_date) FROM events LIMIT 1")
        sample = cur.fetchone()
        if sample and len(sample[0]) == 10 and sample[0][2] == '/' and sample[0][5] == '/':
            print(f"✅ Formatted date: {sample[0]}")
            conn.close()
            return True
        else:
            print(f"❌ Format not DD/MM/YYYY or no data. Sample: {sample}")
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