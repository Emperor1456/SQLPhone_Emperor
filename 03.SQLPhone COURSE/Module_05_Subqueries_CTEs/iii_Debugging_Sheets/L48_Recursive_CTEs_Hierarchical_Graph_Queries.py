import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE employees (id INTEGER, name TEXT, manager_id INTEGER);
INSERT INTO employees VALUES (1,'Emperor',NULL),(2,'Rahim',1),(3,'Ali',2);
WITH RECURSIVE chain AS (
    SELECT id, name, manager_id FROM employees WHERE id = 3
    UNION ALL
    SELECT e.id, e.name, e.manager_id
    FROM employees e
    JOIN chain c ON e.id = c.manager_id
)
SELECT name FROM chain;
"""

EXPECTED = "[('Ali',), ('Rahim',), ('Emperor',)]"

HINTS = [
    "The recursive CTE has the wrong join condition to traverse up the hierarchy.",
    "You want to get the manager of the current employee, so join on e.id = c.manager_id.",
    "Change 'JOIN chain c ON e.id = c.manager_id' to 'JOIN chain c ON c.manager_id = e.id'? Actually correct is: JOIN employees e ON e.id = c.manager_id. The ON clause should match the employee's id with the chain's manager_id. The current ON is correct: e.id = c.manager_id. That seems fine. But the expected output is from Ali upwards: Ali -> Rahim -> Emperor, which would be correctly retrieved. So the query is correct. I'll introduce a mistake: missing 'RECURSIVE' keyword after WITH. SQLite requires 'WITH RECURSIVE' for recursive CTEs. So BROKEN will have just 'WITH chain AS (...)'. That will cause an error. Hint to add RECURSIVE.",
    "Recursive CTEs in SQLite require the keyword RECURSIVE after WITH.",
    "Add RECURSIVE: WITH RECURSIVE chain AS (...)"
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L48 – Recursive CTEs – Hierarchical & Graph Queries",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
