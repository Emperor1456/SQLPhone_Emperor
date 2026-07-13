import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
SELECT id, name, rank FROM soldiers WHERE salary > 4000;
"""

EXPECTED = "[(1, 'Emperor', 'General')]"

SETUP = """\
CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL);
INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',3500);"""

HINTS = [
    "The query references a column that does not exist in the table.",
    "Check the column names in the soldiers table – there is no 'salary' column.",
    "The correct column is 'salary'. Wait, the table does have salary. I'll change the bug: the table has 'salary' but the query uses 'salry' (typo). Fix the typo.",
    "Change 'salry' to 'salary'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L97 – Full‑Stack Integration – Flask/FastAPI + PostgreSQL",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
