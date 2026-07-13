import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER, name TEXT, regiment_id INTEGER);
CREATE TABLE deployments (soldier_id INTEGER, location TEXT);
INSERT INTO soldiers VALUES (1,'Emperor',1),(2,'Rahim',2),(3,'Ali',1);
INSERT INTO deployments VALUES (1,'North'),(3,'South');
SELECT name FROM soldiers WHERE id IN (SELECT soldier_id FROM deployments);
"""

EXPECTED = "[('Ali',), ('Emperor',)]"

HINTS = [
    "The subquery is missing the table name in the FROM clause.",
    "The inner SELECT must specify 'FROM deployments'.",
    "Add 'FROM deployments' inside the subquery."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L43 – Subqueries with IN & NOT IN",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
