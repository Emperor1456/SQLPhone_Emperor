import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE students (student_id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE courses (course_id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE enrollments (
    student_id INTEGER REFERENCES students(student_id),
    course_id INTEGER REFERENCES courses(course_id),
    grade TEXT,
    PRIMARY KEY (student_id, course_id)
);
INSERT INTO students VALUES (1,'Emperor');
INSERT INTO courses VALUES (101,'Math');
INSERT INTO enrollments VALUES (1, 101, 'A');
SELECT s.name, c.name, e.grade FROM students s JOIN enrollments e ON s.student_id = e.student_id JOIN courses c ON e.course_id = c.course_id;
"""

EXPECTED = "[('Emperor', 'Math', 'A')]"

HINTS = [
    "The composite primary key definition is missing the keyword KEY after PRIMARY.",
    "It should be PRIMARY KEY (student_id, course_id).",
    "Add the KEY keyword after PRIMARY."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L60 – Module 6 Capstone – School Management Schema",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
