import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

# ─── Easy: INNER JOIN ───────────────────────────────
def verify_easy(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('students','courses','enrollments')")
    if len(cur.fetchall()) != 3:
        return False
    cur.execute("SELECT COUNT(*) FROM students")
    if cur.fetchone()[0] < 2: return False
    cur.execute("SELECT COUNT(*) FROM courses")
    if cur.fetchone()[0] < 2: return False
    cur.execute("SELECT COUNT(*) FROM enrollments")
    if cur.fetchone()[0] < 2: return False
    # Verify they can do an inner join
    cur.execute("""
        SELECT s.name, c.title
        FROM enrollments e
        JOIN students s ON e.student_id = s.id
        JOIN courses c ON e.course_id = c.id
    """)
    return len(cur.fetchall()) >= 2

easy = Task(
    description="Create tables: students (id, name), courses (id, title),\n"
                "enrollments (student_id, course_id). Insert at least 2 students,\n"
                "2 courses, and 2 enrollments. Write an INNER JOIN query that shows\n"
                "student name and course title for all enrollments.",
    verify_func=verify_easy,
    level=Level.EASY,
    hints=[
        "CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT);",
        "CREATE TABLE courses (id INTEGER PRIMARY KEY, title TEXT);",
        "CREATE TABLE enrollments (student_id INTEGER, course_id INTEGER);",
        "INSERT INTO students VALUES (1,'Alice'),(2,'Bob');",
        "INSERT INTO courses VALUES (1,'Math'),(2,'English');",
        "INSERT INTO enrollments VALUES (1,1),(2,2);",
        "SELECT s.name, c.title FROM enrollments e JOIN students s ON e.student_id=s.id JOIN courses c ON e.course_id=c.id;"
    ]
)

# ─── Medium: LEFT JOIN with NULL check ──────────────
def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM students")
    if cur.fetchone()[0] < 2: return False
    cur.execute("SELECT COUNT(*) FROM enrollments")
    if cur.fetchone()[0] < 2: return False
    # Verify they can find students with no enrollments
    cur.execute("""
        SELECT s.name
        FROM students s
        LEFT JOIN enrollments e ON s.id = e.student_id
        WHERE e.student_id IS NULL
    """)
    rows = cur.fetchall()
    return len(rows) == 1 and rows[0][0] == 'Charlie'

medium = Task(
    description="Add a third student 'Charlie' with no enrollments.\n"
                "Write a LEFT JOIN query that lists all students who have NOT enrolled\n"
                "in any course (use IS NULL). The output should show 'Charlie'.",
    verify_func=verify_medium,
    level=Level.MEDIUM,
    hints=[
        "INSERT INTO students VALUES (3,'Charlie');",
        "SELECT s.name FROM students s LEFT JOIN enrollments e ON s.id=e.student_id WHERE e.student_id IS NULL;"
    ]
)

# ─── Hard: FULL OUTER JOIN simulation + UNION ──────
def verify_hard(cur, conn):
    cur.execute("SELECT COUNT(*) FROM employees")
    if cur.fetchone()[0] < 2: return False
    cur.execute("SELECT COUNT(*) FROM contractors")
    if cur.fetchone()[0] < 2: return False
    expected = "Alice Internal\nBob External\nCharlie Internal"
    cur.execute("""
        SELECT name, type FROM employees
        UNION
        SELECT name, type FROM contractors
        ORDER BY name
    """)
    rows = cur.fetchall()
    result = "\n".join(f"{r[0]} {r[1]}" for r in rows)
    return result == expected

hard = Task(
    description="Build a company directory with UNION:\n"
                "1. Create table 'employees' (id INTEGER PRIMARY KEY, name TEXT, type TEXT).\n"
                "   Insert rows: (1,'Alice','Internal'), (2,'Bob','Internal').\n"
                "2. Create table 'contractors' (id INTEGER PRIMARY KEY, name TEXT, type TEXT).\n"
                "   Insert rows: (1,'Bob','External'), (2,'Charlie','Internal').\n"
                "3. Use UNION to combine all unique names and their type.\n"
                "   Sort the result by name.\n"
                "Exact output must be:\n"
                "Alice Internal\n"
                "Bob External\n"
                "Charlie Internal",
    verify_func=verify_hard,
    level=Level.HARD,
    hints=[
        "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, type TEXT);",
        "INSERT INTO employees VALUES (1,'Alice','Internal'),(2,'Bob','Internal');",
        "CREATE TABLE contractors (id INTEGER PRIMARY KEY, name TEXT, type TEXT);",
        "INSERT INTO contractors VALUES (1,'Bob','External'),(2,'Charlie','Internal');",
        "SELECT name, type FROM employees UNION SELECT name, type FROM contractors ORDER BY name;"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()
