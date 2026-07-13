import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT);
INSERT INTO users VALUES (1,'admin','secret'), (2,'user','pass');
SELECT * FROM users WHERE username = 'admin' OR '1'='1';
"""

EXPECTED = "[(1, 'admin', 'secret')]"

HINTS = [
    "The WHERE clause contains an injection-like pattern that always returns true, but that's not a syntax error.",
    "The bug is that the closing quote after 'admin' is missing, making the string unclosed. But the snippet shown has a proper quote? Let's introduce a real syntax error: remove the closing quote after admin, making the rest of the statement part of the string. That would cause a syntax error. Then the student must add the missing quote.",
    "In the broken code, remove the closing quote after 'admin', so it becomes 'admin OR '1'='1'. The fix is to add the missing quote."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L65 – Preventing SQL Injection – Parameterized Queries",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
