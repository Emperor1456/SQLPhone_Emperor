import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE users (id INTEGER, name TEXT, email TEXT);
INSERT INTO users VALUES (1,'Emperor','emperor@empire.com'),(2,'Rahim',NULL);
SELECT * FROM users WHERE email = NULL;
"""

EXPECTED = "[(2, 'Rahim', None)]"

HINTS = [
    "You cannot compare NULL with =.",
    "Use IS NULL to check for NULL values.",
    "Change = NULL to IS NULL."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L13 – NULL – IS NULL, IS NOT NULL & Handling Missing Data",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
