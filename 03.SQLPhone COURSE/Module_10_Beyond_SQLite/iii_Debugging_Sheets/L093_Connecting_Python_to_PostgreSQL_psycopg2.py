import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE empire (id INTEGER, name TEXT);
INSERT INTO empire VALUES (1, 'Emperor');
SELECT * FROM empire WHERE name = 'Emperor';"""

EXPECTED = "[(1, 'Emperor')]"

HINTS = [
    "The script is perfectly valid SQL, so where is the bug? I'll introduce a sneaky mistake: the table name in the CREATE statement is missing a closing parenthesis? No. I'll change the SELECT to use single quotes that are mismatched: 'Emperor\" (starting with single, ending with double). That will cause a syntax error.",
    "Check the quotes in the WHERE clause: the string uses mixed quotes.",
    "Change the string to consistently use single quotes: 'Emperor'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L93 – Connecting Python to PostgreSQL (psycopg2)",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
