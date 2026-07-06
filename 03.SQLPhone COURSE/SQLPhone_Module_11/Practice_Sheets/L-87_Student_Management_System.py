# L-87_Student_Management_System.py
# SQLPhone Emperor – SQL Module 11
# Practice: Build the Student Management System.

import sqlite3, os

DB = "student_mgmt.db"

def task():
    print("=" * 50)
    print("🧱 PROJECT 1: Student Management System")
    print("Create tables: Student, Course, Enrollment.")
    print("Insert sample data and run the required queries.")
    print("We'll verify the schema and data presence.")
    print("=" * 50)
    if os.path.exists(DB):
        os.remove(DB)
    user_sql = input("Paste your full SQL script:\n> ")
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    # Verify tables and data
    try:
        for tbl in ['Student','Course','Enrollment']:
            cur.execute(f"SELECT COUNT(*) FROM {tbl}")
            cnt = cur.fetchone()[0]
            if cnt == 0:
                print(f"❌ Table {tbl} is empty.")
                conn.close()
                return False
        # Check for required queries? We'll just check the existence of a few.
        print("✅ All tables have data. Execute your query set now (check your file).")
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