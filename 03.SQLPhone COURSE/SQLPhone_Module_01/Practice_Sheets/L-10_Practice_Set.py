# L-10_Module_Challenge.py
# SQLPhone Emperor – SQL Module 01
# Practice: Build the entire Imperial Fitness database.

import sqlite3, os

DB_FILE = "imperial_fitness.db"

def task():
    print("=" * 50)
    print("🧱 MODULE CHALLENGE: Imperial Fitness Database")
    print("Create the four tables (Member, Trainer, Class, Enrollment) with all constraints.")
    print("Insert at least 3 rows each. Then write a query showing member name, class name, trainer name, enrollment date, schedule.")
    print("We will execute your script and verify.")
    print("=" * 50)
    # Clean slate
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    user_sql = input("Paste your full SQL script (end with a line containing 'EOF'):\n")
    # Simple way to read multi-line until EOF
    lines = []
    while True:
        line = input()
        if line.strip() == "EOF":
            break
        lines.append(line)
    full_sql = user_sql + "\n" + "\n".join(lines)
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    try:
        cur.executescript(full_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        os.remove(DB_FILE)
        return False
    # Verify tables exist
    try:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
        tables = [r[0] for r in cur.fetchall()]
        required = {'Member', 'Trainer', 'Class', 'Enrollment'}
        if not required.issubset(tables):
            print(f"❌ Missing tables. Found: {tables}")
            conn.close()
            os.remove(DB_FILE)
            return False
        # Check row counts
        for t in ['Member','Trainer','Class','Enrollment']:
            cur.execute(f"SELECT COUNT(*) FROM {t}")
            cnt = cur.fetchone()[0]
            if cnt < 3:
                print(f"❌ Table '{t}' has only {cnt} rows, need at least 3.")
                conn.close()
                os.remove(DB_FILE)
                return False
        # Run the expected business query (user should have it as last statement)
        # We'll attempt to fetch one row from a join
        cur.execute("""
            SELECT m.first_name || ' ' || m.last_name AS MemberName,
                   c.class_name,
                   t.first_name || ' ' || t.last_name AS TrainerName,
                   e.enrollment_date,
                   c.schedule_time
            FROM Enrollment e
            JOIN Member m ON e.member_id = m.member_id
            JOIN Class c ON e.class_id = c.class_id
            JOIN Trainer t ON c.trainer_id = t.trainer_id
            LIMIT 1
        """)
        sample = cur.fetchone()
        if sample:
            print("✅ Imperial Fitness DB built successfully!")
            print(f"Sample report row: {sample}")
            conn.close()
            os.remove(DB_FILE)
            return True
        else:
            print("❌ Business query returned no rows. Check joins and data.")
            conn.close()
            os.remove(DB_FILE)
            return False
    except Exception as e:
        print(f"❌ Verification error: {e}")
        conn.close()
        if os.path.exists(DB_FILE):
            os.remove(DB_FILE)
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