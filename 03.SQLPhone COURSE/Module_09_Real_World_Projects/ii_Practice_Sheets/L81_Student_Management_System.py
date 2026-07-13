import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏗️  Imperial Academy – Build the Schema\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates the four tables:\n"
        "     students, courses, enrollments, grades\n"
        "     (use the exact schema from the lecture).\n"
        "  3. Inserts the seed data (2 students, 2 courses,\n"
        "     3 enrollments, 3 grades).\n"
        "  4. Commits, then SELECTs all student names\n"
        "     sorted alphabetically and prints them.\n\n"
        "Expected output:\n[('Emperor',), ('Rahim',)]"
    ),
    expected_output="[('Emperor',), ('Rahim',)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript('''",
        "CREATE TABLE students (student_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, enrollment_date TEXT DEFAULT (date('now')));",
        "CREATE TABLE courses (course_id INTEGER PRIMARY KEY, course_name TEXT NOT NULL, credits INTEGER CHECK(credits > 0));",
        "CREATE TABLE enrollments (student_id INTEGER, course_id INTEGER, semester TEXT NOT NULL, PRIMARY KEY (student_id, course_id, semester), FOREIGN KEY (student_id) REFERENCES students(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id));",
        "CREATE TABLE grades (student_id INTEGER, course_id INTEGER, grade TEXT CHECK(grade IN ('A','B','C','D','F')), graded_date TEXT DEFAULT (date('now')), PRIMARY KEY (student_id, course_id), FOREIGN KEY (student_id) REFERENCES students(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id));",
        "''')",
        "conn.executescript('''",
        "INSERT INTO students VALUES (1,'Emperor','emperor@academy.edu','2026-01-10');",
        "INSERT INTO students VALUES (2,'Rahim','rahim@academy.edu','2026-02-15');",
        "INSERT INTO courses VALUES (1,'Database Systems',3);",
        "INSERT INTO courses VALUES (2,'Calculus',4);",
        "INSERT INTO enrollments VALUES (1,1,'2026-Spring');",
        "INSERT INTO enrollments VALUES (1,2,'2026-Spring');",
        "INSERT INTO enrollments VALUES (2,1,'2026-Spring');",
        "INSERT INTO grades VALUES (1,1,'A','2026-06-15');",
        "INSERT INTO grades VALUES (1,2,'B','2026-06-16');",
        "INSERT INTO grades VALUES (2,1,'C','2026-06-15');",
        "''')",
        "conn.commit()",
        "cursor = conn.execute('SELECT name FROM students ORDER BY name')",
        "print(cursor.fetchall())",
    ]
)

easy2 = Task(
    description=(
        "📜  Student Transcript – Emperor's Grades\n\n"
        "The Academy database is already seeded.\n"
        "Write Python code that:\n"
        "  1. Connects to the database (the engine provides\n"
        "     the seeded connection).\n"
        "  2. Executes a query to show Emperor's transcript:\n"
        "     course_name and grade, sorted by course_name.\n"
        "  3. Prints the result.\n\n"
        "Expected output:\n[('Calculus', 'B'), ('Database Systems', 'A')]"
    ),
    setup_sql=(
        "CREATE TABLE students (student_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, enrollment_date TEXT DEFAULT (date('now')));"
        "INSERT INTO students VALUES (1,'Emperor','emperor@academy.edu','2026-01-10');"
        "INSERT INTO students VALUES (2,'Rahim','rahim@academy.edu','2026-02-15');"
        "CREATE TABLE courses (course_id INTEGER PRIMARY KEY, course_name TEXT NOT NULL, credits INTEGER CHECK(credits > 0));"
        "INSERT INTO courses VALUES (1,'Database Systems',3);"
        "INSERT INTO courses VALUES (2,'Calculus',4);"
        "CREATE TABLE enrollments (student_id INTEGER, course_id INTEGER, semester TEXT NOT NULL, PRIMARY KEY (student_id, course_id, semester), FOREIGN KEY (student_id) REFERENCES students(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id));"
        "INSERT INTO enrollments VALUES (1,1,'2026-Spring');"
        "INSERT INTO enrollments VALUES (1,2,'2026-Spring');"
        "INSERT INTO enrollments VALUES (2,1,'2026-Spring');"
        "CREATE TABLE grades (student_id INTEGER, course_id INTEGER, grade TEXT CHECK(grade IN ('A','B','C','D','F')), graded_date TEXT DEFAULT (date('now')), PRIMARY KEY (student_id, course_id), FOREIGN KEY (student_id) REFERENCES students(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id));"
        "INSERT INTO grades VALUES (1,1,'A','2026-06-15');"
        "INSERT INTO grades VALUES (1,2,'B','2026-06-16');"
        "INSERT INTO grades VALUES (2,1,'C','2026-06-15');"
    ),
    expected_output="[('Calculus', 'B'), ('Database Systems', 'A')]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "# setup_sql has already been run by the engine,",
        "# so just write the query using the open connection `conn`.",
        "cursor = conn.execute('''",
        "SELECT c.course_name, g.grade",
        "FROM grades g JOIN courses c ON g.course_id = c.course_id",
        "WHERE g.student_id = 1 ORDER BY c.course_name",
        "''')",
        "print(cursor.fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📊  GPA Report – All Students\n\n"
        "The Academy database is seeded.\n"
        "Write Python code that computes the GPA for every\n"
        "student (A=4, B=3, C=2, D=1, F=0) and prints the\n"
        "result as a list of tuples (name, gpa), sorted by\n"
        "name.\n\n"
        "Expected output:\n[('Emperor', 3.5), ('Rahim', 2.0)]"
    ),
    setup_sql=(
        "CREATE TABLE students (student_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, enrollment_date TEXT DEFAULT (date('now')));"
        "INSERT INTO students VALUES (1,'Emperor','emperor@academy.edu','2026-01-10');"
        "INSERT INTO students VALUES (2,'Rahim','rahim@academy.edu','2026-02-15');"
        "CREATE TABLE courses (course_id INTEGER PRIMARY KEY, course_name TEXT NOT NULL, credits INTEGER CHECK(credits > 0));"
        "INSERT INTO courses VALUES (1,'Database Systems',3);"
        "INSERT INTO courses VALUES (2,'Calculus',4);"
        "CREATE TABLE enrollments (student_id INTEGER, course_id INTEGER, semester TEXT NOT NULL, PRIMARY KEY (student_id, course_id, semester), FOREIGN KEY (student_id) REFERENCES students(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id));"
        "INSERT INTO enrollments VALUES (1,1,'2026-Spring');"
        "INSERT INTO enrollments VALUES (1,2,'2026-Spring');"
        "INSERT INTO enrollments VALUES (2,1,'2026-Spring');"
        "CREATE TABLE grades (student_id INTEGER, course_id INTEGER, grade TEXT CHECK(grade IN ('A','B','C','D','F')), graded_date TEXT DEFAULT (date('now')), PRIMARY KEY (student_id, course_id), FOREIGN KEY (student_id) REFERENCES students(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id));"
        "INSERT INTO grades VALUES (1,1,'A','2026-06-15');"
        "INSERT INTO grades VALUES (1,2,'B','2026-06-16');"
        "INSERT INTO grades VALUES (2,1,'C','2026-06-15');"
    ),
    expected_output="[('Emperor', 3.5), ('Rahim', 2.0)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT s.name, ROUND(AVG(CASE g.grade",
        "    WHEN 'A' THEN 4 WHEN 'B' THEN 3",
        "    WHEN 'C' THEN 2 WHEN 'D' THEN 1 ELSE 0 END), 2) AS gpa",
        "FROM students s JOIN grades g ON s.student_id = g.student_id",
        "GROUP BY s.student_id ORDER BY s.name",
        "''')",
        "print(cursor.fetchall())",
    ]
)

medium2 = Task(
    description=(
        "📈  Course Enrollment Count\n\n"
        "The Academy database is seeded.\n"
        "Write Python code that lists every course and the\n"
        "number of students enrolled, sorted by course_name.\n"
        "Include courses with zero enrollments.\n\n"
        "Expected output:\n[('Calculus', 1), ('Database Systems', 2)]"
    ),
    setup_sql=(
        "CREATE TABLE students (student_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, enrollment_date TEXT DEFAULT (date('now')));"
        "INSERT INTO students VALUES (1,'Emperor','emperor@academy.edu','2026-01-10');"
        "INSERT INTO students VALUES (2,'Rahim','rahim@academy.edu','2026-02-15');"
        "CREATE TABLE courses (course_id INTEGER PRIMARY KEY, course_name TEXT NOT NULL, credits INTEGER CHECK(credits > 0));"
        "INSERT INTO courses VALUES (1,'Database Systems',3);"
        "INSERT INTO courses VALUES (2,'Calculus',4);"
        "CREATE TABLE enrollments (student_id INTEGER, course_id INTEGER, semester TEXT NOT NULL, PRIMARY KEY (student_id, course_id, semester), FOREIGN KEY (student_id) REFERENCES students(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id));"
        "INSERT INTO enrollments VALUES (1,1,'2026-Spring');"
        "INSERT INTO enrollments VALUES (1,2,'2026-Spring');"
        "INSERT INTO enrollments VALUES (2,1,'2026-Spring');"
        "CREATE TABLE grades (student_id INTEGER, course_id INTEGER, grade TEXT CHECK(grade IN ('A','B','C','D','F')), graded_date TEXT DEFAULT (date('now')), PRIMARY KEY (student_id, course_id), FOREIGN KEY (student_id) REFERENCES students(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id));"
        "INSERT INTO grades VALUES (1,1,'A','2026-06-15');"
        "INSERT INTO grades VALUES (1,2,'B','2026-06-16');"
        "INSERT INTO grades VALUES (2,1,'C','2026-06-15');"
    ),
    expected_output="[('Calculus', 1), ('Database Systems', 2)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT c.course_name, COUNT(e.student_id) AS enrolled",
        "FROM courses c LEFT JOIN enrollments e ON c.course_id = e.course_id",
        "GROUP BY c.course_id ORDER BY c.course_name",
        "''')",
        "print(cursor.fetchall())",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🔍  Unenrolled Students – Missing a Course\n\n"
        "The Academy database is seeded with an extra student\n"
        "('Ali') who has no enrollments.\n"
        "Write Python code that finds students NOT enrolled\n"
        "in the '2026-Spring' semester and prints their names.\n\n"
        "Expected output:\n[('Ali',)]"
    ),
    setup_sql=(
        "CREATE TABLE students (student_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, enrollment_date TEXT DEFAULT (date('now')));"
        "INSERT INTO students VALUES (1,'Emperor','emperor@academy.edu','2026-01-10');"
        "INSERT INTO students VALUES (2,'Rahim','rahim@academy.edu','2026-02-15');"
        "INSERT INTO students VALUES (3,'Ali','ali@academy.edu','2026-03-01');"
        "CREATE TABLE courses (course_id INTEGER PRIMARY KEY, course_name TEXT NOT NULL, credits INTEGER CHECK(credits > 0));"
        "INSERT INTO courses VALUES (1,'Database Systems',3);"
        "INSERT INTO courses VALUES (2,'Calculus',4);"
        "CREATE TABLE enrollments (student_id INTEGER, course_id INTEGER, semester TEXT NOT NULL, PRIMARY KEY (student_id, course_id, semester), FOREIGN KEY (student_id) REFERENCES students(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id));"
        "INSERT INTO enrollments VALUES (1,1,'2026-Spring');"
        "INSERT INTO enrollments VALUES (1,2,'2026-Spring');"
        "INSERT INTO enrollments VALUES (2,1,'2026-Spring');"
        "CREATE TABLE grades (student_id INTEGER, course_id INTEGER, grade TEXT CHECK(grade IN ('A','B','C','D','F')), graded_date TEXT DEFAULT (date('now')), PRIMARY KEY (student_id, course_id), FOREIGN KEY (student_id) REFERENCES students(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id));"
        "INSERT INTO grades VALUES (1,1,'A','2026-06-15');"
        "INSERT INTO grades VALUES (1,2,'B','2026-06-16');"
        "INSERT INTO grades VALUES (2,1,'C','2026-06-15');"
    ),
    expected_output="[('Ali',)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT s.name FROM students s",
        "WHERE s.student_id NOT IN (",
        "    SELECT student_id FROM enrollments",
        "    WHERE semester = '2026-Spring'",
        ") ORDER BY s.name",
        "''')",
        "print(cursor.fetchall())",
    ]
)

hard2 = Task(
    description=(
        "✏️  Late Enrollment – Add a Grade for Rahim\n\n"
        "The Academy database is seeded.\n"
        "Write Python code that:\n"
        "  1. Inserts a new enrollment for Rahim (student_id=2)\n"
        "     in 'Calculus' (course_id=2) for '2026-Spring'.\n"
        "  2. Inserts a grade 'B' for Rahim in Calculus.\n"
        "  3. Commits.\n"
        "  4. Then prints Rahim's full transcript (all courses\n"
        "     with grades, sorted by course_name).\n\n"
        "Expected output:\n[('Calculus', 'B'), ('Database Systems', 'C')]"
    ),
    setup_sql=(
        "CREATE TABLE students (student_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, enrollment_date TEXT DEFAULT (date('now')));"
        "INSERT INTO students VALUES (1,'Emperor','emperor@academy.edu','2026-01-10');"
        "INSERT INTO students VALUES (2,'Rahim','rahim@academy.edu','2026-02-15');"
        "CREATE TABLE courses (course_id INTEGER PRIMARY KEY, course_name TEXT NOT NULL, credits INTEGER CHECK(credits > 0));"
        "INSERT INTO courses VALUES (1,'Database Systems',3);"
        "INSERT INTO courses VALUES (2,'Calculus',4);"
        "CREATE TABLE enrollments (student_id INTEGER, course_id INTEGER, semester TEXT NOT NULL, PRIMARY KEY (student_id, course_id, semester), FOREIGN KEY (student_id) REFERENCES students(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id));"
        "INSERT INTO enrollments VALUES (1,1,'2026-Spring');"
        "INSERT INTO enrollments VALUES (1,2,'2026-Spring');"
        "INSERT INTO enrollments VALUES (2,1,'2026-Spring');"
        "CREATE TABLE grades (student_id INTEGER, course_id INTEGER, grade TEXT CHECK(grade IN ('A','B','C','D','F')), graded_date TEXT DEFAULT (date('now')), PRIMARY KEY (student_id, course_id), FOREIGN KEY (student_id) REFERENCES students(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id));"
        "INSERT INTO grades VALUES (1,1,'A','2026-06-15');"
        "INSERT INTO grades VALUES (1,2,'B','2026-06-16');"
        "INSERT INTO grades VALUES (2,1,'C','2026-06-15');"
    ),
    expected_output="[('Calculus', 'B'), ('Database Systems', 'C')]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "# engine already ran setup_sql; just do the insertions",
        "conn.execute(\"INSERT INTO enrollments VALUES (2,2,'2026-Spring')\")",
        "conn.execute(\"INSERT INTO grades (student_id, course_id, grade) VALUES (2,2,'B')\")",
        "conn.commit()",
        "cursor = conn.execute('''",
        "SELECT c.course_name, g.grade FROM grades g",
        "JOIN courses c ON g.course_id = c.course_id",
        "WHERE g.student_id = 2 ORDER BY c.course_name",
        "''')",
        "print(cursor.fetchall())",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L81.json",
        module_name="Module_09_Real_World_Projects",
        lesson_name="L81_Student_Management_System"
    )