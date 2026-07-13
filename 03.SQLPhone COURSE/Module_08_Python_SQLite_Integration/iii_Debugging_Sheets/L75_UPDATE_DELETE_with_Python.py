import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT);
INSERT INTO soldiers VALUES (1,'Emperor','General'),(2,'Rahim','Colonel');
UDATE soldiers SET rank = 'General' WHERE name = 'Rahim';
SELECT * FROM soldiers WHERE id = 2;"""

EXPECTED = "[(2, 'Rahim', 'General')]"

HINTS = [
    "The DML statement has a typo in the command.",
    "The correct keyword starts with UPD…",
    "Change `UDATE` to `UPDATE`."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L75 – UPDATE & DELETE with Python",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
