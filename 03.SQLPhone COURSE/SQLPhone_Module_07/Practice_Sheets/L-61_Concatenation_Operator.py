# L-61_Concatenation_Operator.py
# SQLPhone Emperor – SQL Module 07
# Practice: Concatenation with ||.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'contacts' (first_name, last_name, title).")
    print("Insert rows; some with NULL title.")
    print("Write a query that concatenates title, first_name, last_name into 'Title First Last'.")
    print("Handle NULL title with COALESCE to avoid NULL results.")
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
        cur.execute("""
            SELECT COALESCE(title || ' ', '') || first_name || ' ' || last_name
            FROM contacts
            LIMIT 1
        """)
        full = cur.fetchone()
        if full and full[0] and not full[0].startswith('None'):
            print(f"✅ Concatenated: {full[0]}")
            conn.close()
            return True
        else:
            print(f"❌ Result is NULL or starts with 'None': {full}")
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