import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE users (username TEXT);
INSERT INTO users VALUES ('admin');
SELECT * FROM users WHERE username = admin;"""

EXPECTED = "[('admin',)]"

HINTS = [
    "The string in the WHERE clause is not quoted.",
    "String literals must be enclosed in single quotes.",
    "Change `admin` to 'admin'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L73 – Parameterized INSERT & SELECT (Anti‑Injection)",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
