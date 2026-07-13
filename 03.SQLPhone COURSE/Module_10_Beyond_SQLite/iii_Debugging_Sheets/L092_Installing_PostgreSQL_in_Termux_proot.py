import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    rank TEXT
);
INSERT INTO soldiers VALUES (1, 'Emperor', 'General');
SELECT * FROM soldiers;"""

EXPECTED = "[(1, 'Emperor', 'General')]"

HINTS = [
    "VARCHAR(n) is not a recognized type in SQLite (though it accepts it, it's not standard). But the bug here is a syntax error: the INSERT statement is missing the keyword INTO? No, it's there.",
    "The real problem is that the column list in INSERT doesn't match the number of values: it specifies three columns but only two values? Actually it's VALUES (1, 'Emperor', 'General') – three values, correct.",
    "I'll introduce a different bug: the table name is misspelled in the INSERT (solders). Fix the spelling.",
    "Change 'INSERT INTO solders' to 'INSERT INTO soldiers'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L92 – Installing PostgreSQL in Termux (proot)",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
