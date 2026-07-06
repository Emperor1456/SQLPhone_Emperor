# L-53_PRIMARY_KEY_and_Composite_Keys.py
# SQLPhone Emperor – SQL Module 06
# Practice: Composite primary key.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create a junction table 'memberships' with columns user_id, group_id, joined_date.")
    print("Use PRIMARY KEY (user_id, group_id) to prevent duplicate memberships.")
    print("Insert two rows, then try inserting a duplicate pair (should fail).")
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
        # Check composite key enforcement
        try:
            cur.execute("INSERT INTO memberships (user_id, group_id, joined_date) VALUES (1, 1, date('now'))")
            cur.execute("INSERT INTO memberships (user_id, group_id, joined_date) VALUES (1, 1, date('now'))")
            print("❌ Duplicate composite key not rejected.")
            conn.close()
            return False
        except sqlite3.IntegrityError:
            print("✅ Duplicate (user_id, group_id) correctly rejected.")
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