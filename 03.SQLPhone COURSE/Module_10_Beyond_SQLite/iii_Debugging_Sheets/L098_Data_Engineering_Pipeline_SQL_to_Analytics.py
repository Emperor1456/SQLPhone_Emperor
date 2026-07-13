import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
SELECT name, salary * 0.9 AS salary_taxed FROM soldiers WHERE salary_taxed > 4000;
"""

EXPECTED = "[(1, 'Emperor', 4500.0)]"

SETUP = """\
CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, salary REAL);
INSERT INTO soldiers VALUES (1,'Emperor',5000),(2,'Rahim',4000);"""

HINTS = [
    "The WHERE clause uses an alias that is not allowed in the same query level.",
    "You cannot use column aliases in the WHERE clause.",
    "Replace 'salary_taxed' with the full expression: 'salary * 0.9 > 4000'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L98 – Data Engineering Pipeline – SQL to Analytics",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
