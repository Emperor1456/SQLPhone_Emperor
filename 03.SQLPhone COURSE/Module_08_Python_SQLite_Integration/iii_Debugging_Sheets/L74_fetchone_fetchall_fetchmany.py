import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER, name TEXT);
INSERT INTO soldiers VALUES (1,'Emperor'),(2,'Rahim');
SELECT * FROM soldier;"""

EXPECTED = "[(1, 'Emperor'), (2, 'Rahim')]"

HINTS = [
    "The table name in the SELECT statement does not match the created table.",
    "Check the spelling of the table name.",
    "Change `soldier` to `soldiers`."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L74 – fetchone(), fetchall(), fetchmany()",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
