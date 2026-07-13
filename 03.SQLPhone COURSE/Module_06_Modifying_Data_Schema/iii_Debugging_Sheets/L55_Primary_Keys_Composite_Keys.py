import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE enrollments (student_id INTEGER course_id INTEGER, PRIMARY KEY (student_id, course_id));
INSERT INTO enrollments VALUES (1, 101);
SELECT * FROM enrollments;"""

EXPECTED = "[(1, 101)]"

SETUP = ""

HINTS = [
    "The column definitions in CREATE TABLE are not separated correctly.",
    "A comma is missing between 'student_id INTEGER' and 'course_id INTEGER'.",
    "Add a comma after 'INTEGER' for the first column."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L55 – Primary Keys & Composite Keys",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
