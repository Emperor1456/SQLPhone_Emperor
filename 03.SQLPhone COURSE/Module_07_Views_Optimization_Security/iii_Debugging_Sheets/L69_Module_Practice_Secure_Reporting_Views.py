import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, salary REAL);
INSERT INTO employees VALUES (1,'Emperor',5000),(2,'Rahim',4000);
CREATE VIEW public_info AS SELECT id, name FROM employees;
SELECT * FROM public_info ORDER BY name;
"""

EXPECTED = "[('Emperor',), ('Rahim',)]"

HINTS = [
    "The view selects id and name, but the outer query expects only the name column.",
    "Adjust the SELECT statement to return only the column that matches the expected output.",
    "Change 'SELECT * FROM public_info ORDER BY name' to 'SELECT name FROM public_info ORDER BY name'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L69 – Module Practice: Secure Reporting Views",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
