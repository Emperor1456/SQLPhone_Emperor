import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT UNIQUE);
INSERT INTO users VALUES (1, 'emperor@empire.com');
INSERT INTO users VALUES (2, 'emperor@empire.com');
SELECT COUNT(*) FROM users;"""

EXPECTED = "[(1,)]"

HINTS = [
    "The second INSERT violates a UNIQUE constraint on the email column.",
    "Duplicate emails are not allowed. Change the email in the second INSERT to a unique value.",
    "Use 'rahim@empire.com' for the second user."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L96 – Cloud Databases – AWS RDS, Supabase, PlanetScale",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
