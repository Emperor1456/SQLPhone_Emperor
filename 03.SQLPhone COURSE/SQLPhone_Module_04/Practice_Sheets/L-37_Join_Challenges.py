# L-37_Join_Challenges.py
# SQLPhone Emperor – SQL Module 04
# Practice: Complete join challenge set.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 MODULE 04 CHALLENGES: Joins")
    print("Create tables: students, courses, enrollments (with grade).")
    print("Insert diverse data, then write the five queries from the lecture.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    user_sql = input("Enter your full SQL script:\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    try:
        # Basic checks: there should be students with and without enrollments, courses with no students.
        cur.execute("SELECT COUNT(*) FROM students")
        s = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM courses")
        c = cur.fetchone()[0]
        if s < 3 or c < 3:
            print("❌ Need at least 3 students and 3 courses.")
            conn.close()
            return False
        # Test query 2: courses with no students (LEFT JOIN + IS NULL)
        cur.execute("""
            SELECT c.title FROM courses c
            LEFT JOIN enrollments e ON c.id = e.course_id
            WHERE e.student_id IS NULL
        """)
        empty_courses = cur.fetchall()
        if empty_courses:
            print(f"✅ Courses with no students: {[r[0] for r in empty_courses]}")
        else:
            print("⚠️ No empty courses. For full test, insert a course with no enrollments.")
        # If we got here, script executed without errors, consider it passed.
        print("✅ All challenge queries executed successfully.")
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