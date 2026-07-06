# L-62_CAST.py
# SQLPhone Emperor – SQL Module 07
# Practice: CAST values.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'measurements' (sensor TEXT, reading TEXT).")
    print("Insert numeric readings as text (e.g., '42.5').")
    print("Write a query that casts reading to REAL and computes the average.")
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
        cur.execute("SELECT AVG(CAST(reading AS REAL)) FROM measurements")
        avg = cur.fetchone()[0]
        if avg is not None and avg > 0:
            print(f"✅ Average of cast values: {avg}")
            conn.close()
            return True
        else:
            print("❌ Could not compute average. Check data types.")
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