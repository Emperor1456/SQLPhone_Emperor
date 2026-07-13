import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
EXPLAIN QUERY PLAN SELECT * FROM soldiers WHERE id = 1;
"""

EXPECTED = "[('SEARCH TABLE soldiers USING INTEGER PRIMARY KEY (rowid=?)',)]"

SETUP = "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT); INSERT INTO soldiers VALUES (1,'Emperor');"

HINTS = [
    "The statement has a syntax error: 'EXPLAIN QUERY PLAN' is correct, but maybe a keyword is misspelled?",
    "Check the spelling of 'EXPLAIN' – it might be written as 'EXPLAINN'.",
    "Fix the typo: 'EXPLAIN' instead of 'EXPLAINN'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L63 – EXPLAIN QUERY PLAN – Understanding Performance",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
