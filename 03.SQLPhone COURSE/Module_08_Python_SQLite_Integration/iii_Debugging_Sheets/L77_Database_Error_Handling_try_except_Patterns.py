import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE);
INSERT INTO users VALUES (1, 'emperor');
INSERT INTO users VALUES (2, 'emperor');
SELECT * FROM users;"""

EXPECTED = "[(1, 'emperor')]"

HINTS = [
    "The second INSERT violates the UNIQUE constraint.",
    "Change the second INSERT to use a different username.",
    "Change the second INSERT to: INSERT INTO users VALUES (2, 'rahim');"
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L77 – Database Error Handling – try/except Patterns",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
