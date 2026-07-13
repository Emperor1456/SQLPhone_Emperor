import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
UPDATE soldiers SET rank = 'General' WHERE soldier_name = 'Rahim';
SELECT * FROM soldiers WHERE id = 2;"""

EXPECTED = "[(2, 'Rahim', 'General')]"

SETUP = """\
CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT);
INSERT INTO soldiers VALUES (1,'Emperor','General'), (2,'Rahim','Colonel');"""

HINTS = [
    "The UPDATE statement uses a column that does not exist.",
    "Check the column names in the soldiers table.",
    "The WHERE clause should use 'name' instead of 'soldier_name'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L51 – UPDATE – Modifying Rows",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
