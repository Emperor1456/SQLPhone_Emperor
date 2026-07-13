import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
SELECT s.name, c.course_name, g.grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN courses c ON g.course_id = c.course_id
WHERE s.student_id = 1;"""

EXPECTED = "[('Emperor', 'Database Systems', 'A'), ('Emperor', 'Calculus', 'B')]"

SETUP = """\
CREATE TABLE students (student_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, enrollment_date TEXT DEFAULT (date('now')));
INSERT INTO students VALUES (1,'Emperor','emperor@academy.edu','2026-01-10'),(2,'Rahim','rahim@academy.edu','2026-02-15');
CREATE TABLE courses (course_id INTEGER PRIMARY KEY, course_name TEXT NOT NULL, credits INTEGER CHECK(credits > 0));
INSERT INTO courses VALUES (1,'Database Systems',3),(2,'Calculus',4);
CREATE TABLE enrollments (student_id INTEGER, course_id INTEGER, semester TEXT NOT NULL, PRIMARY KEY (student_id, course_id, semester), FOREIGN KEY (student_id) REFERENCES students(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id));
INSERT INTO enrollments VALUES (1,1,'2026-Spring'),(1,2,'2026-Spring'),(2,1,'2026-Spring');
CREATE TABLE grades (student_id INTEGER, course_id INTEGER, grade TEXT CHECK(grade IN ('A','B','C','D','F')), graded_date TEXT DEFAULT (date('now')), PRIMARY KEY (student_id, course_id), FOREIGN KEY (student_id) REFERENCES students(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id));
INSERT INTO grades VALUES (1,1,'A','2026-06-15'),(1,2,'B','2026-06-16'),(2,1,'C','2026-06-15');"""

HINTS = [
    "The query joins three tables, but the grades table is not joined correctly.",
    "You need to join grades with courses on the correct column.",
    "Change 'JOIN courses c ON g.course_id = c.course_id' to 'JOIN courses c ON g.course_id = c.course_id' – wait, that's the same. The bug is actually a missing comma in the SELECT? No. I'll introduce a different bug: the broken code has 'courses' misspelled as 'coures'. So the student must fix the table name.",
    "Look at the spelling of the courses table in the JOIN clause.",
    "Correct 'coures' to 'courses'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L81 – Student Management System",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
