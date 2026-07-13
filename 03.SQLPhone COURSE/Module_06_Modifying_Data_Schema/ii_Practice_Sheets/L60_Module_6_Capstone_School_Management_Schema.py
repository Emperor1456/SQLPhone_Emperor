import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏗️  Imperial Academy – Create All Tables\n\n"
        "Create five tables with full constraints:\n\n"
        "1. `teachers`:\n"
        "  • teacher_id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • email TEXT UNIQUE NOT NULL\n"
        "  • hire_date TEXT DEFAULT (date('now'))\n\n"
        "2. `courses`:\n"
        "  • course_id INTEGER PRIMARY KEY\n"
        "  • course_name TEXT NOT NULL\n"
        "  • teacher_id INTEGER REFERENCES teachers\n"
        "  • credits INTEGER CHECK(credits > 0)\n\n"
        "3. `students`:\n"
        "  • student_id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • enrollment_date TEXT DEFAULT (date('now'))\n\n"
        "4. `enrollments`:\n"
        "  • student_id INTEGER\n"
        "  • course_id INTEGER\n"
        "  • enrolled_date TEXT DEFAULT (date('now'))\n"
        "  • PRIMARY KEY (student_id, course_id)\n"
        "  • FKs with ON DELETE CASCADE\n\n"
        "5. `grades`:\n"
        "  • grade_id INTEGER PRIMARY KEY\n"
        "  • student_id INTEGER NOT NULL REFERENCES students\n"
        "  • course_id INTEGER NOT NULL REFERENCES courses\n"
        "  • grade TEXT CHECK(grade IN ('A','B','C','D','F'))\n"
        "  • graded_date TEXT DEFAULT (date('now'))\n"
        "  • UNIQUE(student_id, course_id)\n\n"
        "After creating, query sqlite_master to list all tables.\n\n"
        "Expected output:\n[('courses',), ('enrollments',), ('grades',), ('students',), ('teachers',)]"
    ),
    expected_output="[('courses',), ('enrollments',), ('grades',), ('students',), ('teachers',)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE teachers (teacher_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, hire_date TEXT DEFAULT (date('now')));",
        "CREATE TABLE courses (course_id INTEGER PRIMARY KEY, course_name TEXT NOT NULL, teacher_id INTEGER REFERENCES teachers, credits INTEGER CHECK(credits > 0));",
        "CREATE TABLE students (student_id INTEGER PRIMARY KEY, name TEXT NOT NULL, enrollment_date TEXT DEFAULT (date('now')));",
        "CREATE TABLE enrollments (student_id INTEGER, course_id INTEGER, enrolled_date TEXT DEFAULT (date('now')), PRIMARY KEY(student_id, course_id), FOREIGN KEY(student_id) REFERENCES students(student_id) ON DELETE CASCADE, FOREIGN KEY(course_id) REFERENCES courses(course_id) ON DELETE CASCADE);",
        "CREATE TABLE grades (grade_id INTEGER PRIMARY KEY, student_id INTEGER NOT NULL REFERENCES students, course_id INTEGER NOT NULL REFERENCES courses, grade TEXT CHECK(grade IN ('A','B','C','D','F')), graded_date TEXT DEFAULT (date('now')), UNIQUE(student_id, course_id));",
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
    ]
)

easy2 = Task(
    description=(
        "📋  Seed the Academy – Insert Data\n\n"
        "Insert data into all five tables:\n\n"
        "Teachers: 2 (Dr. Karim, Prof. Begum)\n"
        "Courses: 2 (Database Systems, Calculus)\n"
        "Students: 3 (Emperor, Rahim, Karim)\n"
        "Enrollments: 4 (Emperor in both courses,\n"
        "  Rahim and Karim in Database Systems)\n"
        "Grades: 3 (Emperor: A in DB, B in Calc;\n"
        "  Rahim: C in DB)\n\n"
        "Then SELECT student names sorted alphabetically.\n\n"
        "Expected output:\n[('Emperor',), ('Karim',), ('Rahim',)]"
    ),
    expected_output="[('Emperor',), ('Karim',), ('Rahim',)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE teachers (teacher_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, hire_date TEXT DEFAULT (date('now')));",
        "CREATE TABLE courses (course_id INTEGER PRIMARY KEY, course_name TEXT NOT NULL, teacher_id INTEGER REFERENCES teachers, credits INTEGER CHECK(credits > 0));",
        "CREATE TABLE students (student_id INTEGER PRIMARY KEY, name TEXT NOT NULL, enrollment_date TEXT DEFAULT (date('now')));",
        "CREATE TABLE enrollments (student_id INTEGER, course_id INTEGER, enrolled_date TEXT DEFAULT (date('now')), PRIMARY KEY(student_id, course_id), FOREIGN KEY(student_id) REFERENCES students(student_id) ON DELETE CASCADE, FOREIGN KEY(course_id) REFERENCES courses(course_id) ON DELETE CASCADE);",
        "CREATE TABLE grades (grade_id INTEGER PRIMARY KEY, student_id INTEGER NOT NULL REFERENCES students, course_id INTEGER NOT NULL REFERENCES courses, grade TEXT CHECK(grade IN ('A','B','C','D','F')), graded_date TEXT DEFAULT (date('now')), UNIQUE(student_id, course_id));",
        "INSERT INTO teachers VALUES (1,'Dr. Karim','karim@academy.edu','2025-01-15'), (2,'Prof. Begum','begum@academy.edu','2025-02-01');",
        "INSERT INTO courses VALUES (1,'Database Systems',1,3), (2,'Calculus',2,4);",
        "INSERT INTO students VALUES (1,'Emperor','2026-01-10'), (2,'Rahim','2026-02-15'), (3,'Karim','2026-03-20');",
        "INSERT INTO enrollments VALUES (1,1,'2026-06-01'), (1,2,'2026-06-01'), (2,1,'2026-06-01'), (3,1,'2026-06-01');",
        "INSERT INTO grades (student_id, course_id, grade) VALUES (1,1,'A'), (1,2,'B'), (2,1,'C');",
        "SELECT name FROM students ORDER BY name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📊  Student Transcript – JOIN Query\n\n"
        "The tables are seeded.\n"
        "Write a query that returns a transcript for\n"
        "a specific student (Emperor, student_id=1).\n"
        "Show the course name and the grade.\n"
        "Sort by course name.\n\n"
        "Expected output:\n[('Calculus','B'), ('Database Systems','A')]"
    ),
    setup_sql=(
        "CREATE TABLE teachers (teacher_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, hire_date TEXT DEFAULT (date('now')));"
        "INSERT INTO teachers VALUES (1,'Dr. Karim','karim@academy.edu','2025-01-15'), (2,'Prof. Begum','begum@academy.edu','2025-02-01');"
        "CREATE TABLE courses (course_id INTEGER PRIMARY KEY, course_name TEXT NOT NULL, teacher_id INTEGER REFERENCES teachers, credits INTEGER CHECK(credits > 0));"
        "INSERT INTO courses VALUES (1,'Database Systems',1,3), (2,'Calculus',2,4);"
        "CREATE TABLE students (student_id INTEGER PRIMARY KEY, name TEXT NOT NULL, enrollment_date TEXT DEFAULT (date('now')));"
        "INSERT INTO students VALUES (1,'Emperor','2026-01-10'), (2,'Rahim','2026-02-15'), (3,'Karim','2026-03-20');"
        "CREATE TABLE enrollments (student_id INTEGER, course_id INTEGER, enrolled_date TEXT DEFAULT (date('now')), PRIMARY KEY(student_id, course_id), FOREIGN KEY(student_id) REFERENCES students(student_id) ON DELETE CASCADE, FOREIGN KEY(course_id) REFERENCES courses(course_id) ON DELETE CASCADE);"
        "INSERT INTO enrollments VALUES (1,1,'2026-06-01'), (1,2,'2026-06-01'), (2,1,'2026-06-01'), (3,1,'2026-06-01');"
        "CREATE TABLE grades (grade_id INTEGER PRIMARY KEY, student_id INTEGER NOT NULL REFERENCES students, course_id INTEGER NOT NULL REFERENCES courses, grade TEXT CHECK(grade IN ('A','B','C','D','F')), graded_date TEXT DEFAULT (date('now')), UNIQUE(student_id, course_id));"
        "INSERT INTO grades (student_id, course_id, grade) VALUES (1,1,'A'), (1,2,'B'), (2,1,'C');"
    ),
    expected_output="[('Calculus', 'B'), ('Database Systems', 'A')]",
    level=Level.MEDIUM,
    hints=[
        "SELECT c.course_name, g.grade FROM grades g JOIN courses c ON g.course_id = c.course_id WHERE g.student_id = 1 ORDER BY c.course_name;"
    ]
)

medium2 = Task(
    description=(
        "📈  Course Enrollment Count – Aggregation\n\n"
        "The tables are seeded.\n"
        "Write a query that returns the course name and\n"
        "the number of students enrolled in each course.\n"
        "Include courses with ZERO enrollments.\n"
        "Use LEFT JOIN and GROUP BY.\n"
        "Sort by enrolled_count descending.\n\n"
        "Expected output:\n[('Database Systems',3), ('Calculus',1)]"
    ),
    setup_sql=(
        "CREATE TABLE teachers (teacher_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, hire_date TEXT DEFAULT (date('now')));"
        "INSERT INTO teachers VALUES (1,'Dr. Karim','karim@academy.edu','2025-01-15'), (2,'Prof. Begum','begum@academy.edu','2025-02-01');"
        "CREATE TABLE courses (course_id INTEGER PRIMARY KEY, course_name TEXT NOT NULL, teacher_id INTEGER REFERENCES teachers, credits INTEGER CHECK(credits > 0));"
        "INSERT INTO courses VALUES (1,'Database Systems',1,3), (2,'Calculus',2,4);"
        "CREATE TABLE students (student_id INTEGER PRIMARY KEY, name TEXT NOT NULL, enrollment_date TEXT DEFAULT (date('now')));"
        "INSERT INTO students VALUES (1,'Emperor','2026-01-10'), (2,'Rahim','2026-02-15'), (3,'Karim','2026-03-20');"
        "CREATE TABLE enrollments (student_id INTEGER, course_id INTEGER, enrolled_date TEXT DEFAULT (date('now')), PRIMARY KEY(student_id, course_id), FOREIGN KEY(student_id) REFERENCES students(student_id) ON DELETE CASCADE, FOREIGN KEY(course_id) REFERENCES courses(course_id) ON DELETE CASCADE);"
        "INSERT INTO enrollments VALUES (1,1,'2026-06-01'), (1,2,'2026-06-01'), (2,1,'2026-06-01'), (3,1,'2026-06-01');"
        "CREATE TABLE grades (grade_id INTEGER PRIMARY KEY, student_id INTEGER NOT NULL REFERENCES students, course_id INTEGER NOT NULL REFERENCES courses, grade TEXT CHECK(grade IN ('A','B','C','D','F')), graded_date TEXT DEFAULT (date('now')), UNIQUE(student_id, course_id));"
        "INSERT INTO grades (student_id, course_id, grade) VALUES (1,1,'A'), (1,2,'B'), (2,1,'C');"
    ),
    expected_output="[('Database Systems', 3), ('Calculus', 1)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT c.course_name, COUNT(e.student_id) AS enrolled_count FROM courses c LEFT JOIN enrollments e ON c.course_id = e.course_id GROUP BY c.course_id ORDER BY enrolled_count DESC;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  GPA Calculation – CASE + Aggregation\n\n"
        "The tables are seeded with grades.\n"
        "Write a query that computes each student's GPA\n"
        "on a 4.0 scale:\n"
        "  • A = 4, B = 3, C = 2, D = 1, F = 0\n"
        "Return student name and ROUND(AVG(...), 2) as gpa.\n"
        "Include students with no grades (show NULL).\n"
        "Sort by gpa descending (NULLs last).\n\n"
        "Expected output:\n[('Emperor',3.5), ('Rahim',2.0), ('Karim',None)]"
    ),
    setup_sql=(
        "CREATE TABLE teachers (teacher_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, hire_date TEXT DEFAULT (date('now')));"
        "INSERT INTO teachers VALUES (1,'Dr. Karim','karim@academy.edu','2025-01-15'), (2,'Prof. Begum','begum@academy.edu','2025-02-01');"
        "CREATE TABLE courses (course_id INTEGER PRIMARY KEY, course_name TEXT NOT NULL, teacher_id INTEGER REFERENCES teachers, credits INTEGER CHECK(credits > 0));"
        "INSERT INTO courses VALUES (1,'Database Systems',1,3), (2,'Calculus',2,4);"
        "CREATE TABLE students (student_id INTEGER PRIMARY KEY, name TEXT NOT NULL, enrollment_date TEXT DEFAULT (date('now')));"
        "INSERT INTO students VALUES (1,'Emperor','2026-01-10'), (2,'Rahim','2026-02-15'), (3,'Karim','2026-03-20');"
        "CREATE TABLE enrollments (student_id INTEGER, course_id INTEGER, enrolled_date TEXT DEFAULT (date('now')), PRIMARY KEY(student_id, course_id), FOREIGN KEY(student_id) REFERENCES students(student_id) ON DELETE CASCADE, FOREIGN KEY(course_id) REFERENCES courses(course_id) ON DELETE CASCADE);"
        "INSERT INTO enrollments VALUES (1,1,'2026-06-01'), (1,2,'2026-06-01'), (2,1,'2026-06-01'), (3,1,'2026-06-01');"
        "CREATE TABLE grades (grade_id INTEGER PRIMARY KEY, student_id INTEGER NOT NULL REFERENCES students, course_id INTEGER NOT NULL REFERENCES courses, grade TEXT CHECK(grade IN ('A','B','C','D','F')), graded_date TEXT DEFAULT (date('now')), UNIQUE(student_id, course_id));"
        "INSERT INTO grades (student_id, course_id, grade) VALUES (1,1,'A'), (1,2,'B'), (2,1,'C');"
    ),
    expected_output="[('Emperor', 3.5), ('Rahim', 2.0), ('Karim', None)]",
    level=Level.HARD,
    hints=[
        "SELECT s.name, ROUND(AVG(CASE g.grade WHEN 'A' THEN 4 WHEN 'B' THEN 3 WHEN 'C' THEN 2 WHEN 'D' THEN 1 WHEN 'F' THEN 0 END), 2) AS gpa FROM students s LEFT JOIN grades g ON s.student_id = g.student_id GROUP BY s.student_id ORDER BY gpa DESC;"
    ]
)

hard2 = Task(
    description=(
        "🔄  Add Department Column – Migration\n\n"
        "The `teachers` table exists.\n"
        "Create a new `departments` table and migrate\n"
        "teacher data. Steps:\n"
        "  1. CREATE TABLE departments (dept_id INTEGER PK,\n"
        "     dept_name TEXT UNIQUE)\n"
        "  2. INSERT departments: 'Science','Arts','Commerce'\n"
        "  3. ALTER TABLE teachers ADD COLUMN dept_id INTEGER\n"
        "     DEFAULT 1 REFERENCES departments(dept_id)\n"
        "  4. UPDATE teachers SET dept_id = appropriate value\n"
        "     (Dr. Karim = Science=1, Prof. Begum = Arts=2)\n"
        "  5. SELECT teacher name and their department name\n"
        "     using a JOIN.\n\n"
        "Expected output:\n[('Dr. Karim','Science'), ('Prof. Begum','Arts')]"
    ),
    setup_sql=(
        "CREATE TABLE teachers (teacher_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, hire_date TEXT DEFAULT (date('now')));"
        "INSERT INTO teachers VALUES (1,'Dr. Karim','karim@academy.edu','2025-01-15'), (2,'Prof. Begum','begum@academy.edu','2025-02-01');"
        "CREATE TABLE courses (course_id INTEGER PRIMARY KEY, course_name TEXT NOT NULL, teacher_id INTEGER REFERENCES teachers, credits INTEGER CHECK(credits > 0));"
        "INSERT INTO courses VALUES (1,'Database Systems',1,3), (2,'Calculus',2,4);"
        "CREATE TABLE students (student_id INTEGER PRIMARY KEY, name TEXT NOT NULL, enrollment_date TEXT DEFAULT (date('now')));"
        "INSERT INTO students VALUES (1,'Emperor','2026-01-10'), (2,'Rahim','2026-02-15'), (3,'Karim','2026-03-20');"
        "CREATE TABLE enrollments (student_id INTEGER, course_id INTEGER, enrolled_date TEXT DEFAULT (date('now')), PRIMARY KEY(student_id, course_id), FOREIGN KEY(student_id) REFERENCES students(student_id) ON DELETE CASCADE, FOREIGN KEY(course_id) REFERENCES courses(course_id) ON DELETE CASCADE);"
        "INSERT INTO enrollments VALUES (1,1,'2026-06-01'), (1,2,'2026-06-01'), (2,1,'2026-06-01'), (3,1,'2026-06-01');"
        "CREATE TABLE grades (grade_id INTEGER PRIMARY KEY, student_id INTEGER NOT NULL REFERENCES students, course_id INTEGER NOT NULL REFERENCES courses, grade TEXT CHECK(grade IN ('A','B','C','D','F')), graded_date TEXT DEFAULT (date('now')), UNIQUE(student_id, course_id));"
        "INSERT INTO grades (student_id, course_id, grade) VALUES (1,1,'A'), (1,2,'B'), (2,1,'C');"
    ),
    expected_output="[('Dr. Karim', 'Science'), ('Prof. Begum', 'Arts')]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, dept_name TEXT UNIQUE);",
        "INSERT INTO departments (dept_name) VALUES ('Science'), ('Arts'), ('Commerce');",
        "ALTER TABLE teachers ADD COLUMN dept_id INTEGER DEFAULT 1 REFERENCES departments(dept_id);",
        "UPDATE teachers SET dept_id = 1 WHERE teacher_id = 1;",
        "UPDATE teachers SET dept_id = 2 WHERE teacher_id = 2;",
        "SELECT t.name, d.dept_name FROM teachers t JOIN departments d ON t.dept_id = d.dept_id ORDER BY t.name;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L60.json",
        module_name="Module_06_Modifying_Data_Schema",
        lesson_name="L60_Module_6_Capstone"
    )
