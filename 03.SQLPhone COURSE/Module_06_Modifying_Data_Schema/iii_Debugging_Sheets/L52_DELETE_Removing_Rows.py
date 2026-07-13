import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
DELETE FROM soldiers WHERE id = 4;
SELECT * FROM soldiers ORDER BY id;"""

EXPECTED = "[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0), (3, 'Ali', 'Colonel', 4500.0)]"

SETUP = """\
CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL);
INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Ali','Colonel',4500), (4,'Hasan','Private',3500);"""

HINTS = [
    "The DELETE statement targets id=4, but is the table name correct?",
    "The table might be called 'soldiers' – check the spelling.",
    "The table name should be 'soldiers' not 'soldier'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L52 – DELETE – Removing Rows",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
