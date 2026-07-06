# L-86_Schema_Design_Best_Practices.py
# SQLPhone Emperor – SQL Module 10
# Practice: Apply normalisation and naming conventions.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Design a schema for a 'school' database with students, courses, and enrollments.")
    print("Use proper naming (snake_case, singular table names), primary keys, foreign keys, and constraints.")
    print("Include at least a CHECK constraint and a UNIQUE constraint where logical.")
    print("We'll examine your CREATE TABLE statements.")
    print("=" * 50)
    user_sql = input("Enter your DDL statements:\n> ")
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    # Check naming conventions: all table names should be singular and snake_case
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in cur.fetchall()]
    for t in tables:
        if t[-1] == 's' or ' ' in t or '-' in t:
            print(f"⚠️ Table '{t}' may violate naming conventions (should be singular, snake_case).")
    # Check that there is at least one CHECK or UNIQUE constraint
    has_constraint = False
    for t in tables:
        cur.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{t}'")
        ddl = cur.fetchone()[0]
        if 'CHECK' in ddl or 'UNIQUE' in ddl:
            has_constraint = True
            break
    if has_constraint:
        print("✅ Schema includes constraints. Good practice!")
        conn.close()
        return True
    else:
        print("❌ No CHECK or UNIQUE constraints found. Add at least one.")
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