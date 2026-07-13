import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
ALTER TABLE soldiers ADD COLUMN age INTEGER DEFAULT 0;
ALTER TABLE soldiers DROP COLUMN age;
SELECT * FROM soldiers WHERE id = 1;"""

EXPECTED = "[(1, 'Emperor', 'General')]"

SETUP = """\
CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT);
INSERT INTO soldiers VALUES (1,'Emperor','General'), (2,'Rahim','Colonel');"""

HINTS = [
    "The ALTER TABLE ... DROP COLUMN syntax is not correct.",
    "You must include the keyword 'COLUMN' after DROP.",
    "Use 'ALTER TABLE soldiers DROP COLUMN age;'"
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L53 – ALTER TABLE & DROP TABLE – Schema Evolution",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
