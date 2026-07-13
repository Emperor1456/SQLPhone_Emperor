import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE employees (id INTEGER, name TEXT, manager_id INTEGER);
INSERT INTO employees VALUES (1,'Emperor',NULL),(2,'Rahim',1);
SELECT e.name, m.name AS manager FROM employees e JOIN employees m ON e.manager_id = m.manager_id;
"""

EXPECTED = "[('Rahim', 'Emperor')]"

HINTS = [
    "The self‑join uses the wrong column to link the tables.",
    "You want to match the employee's manager_id with the manager's id.",
    "Change m.manager_id to m.id in the ON clause."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L35 – Self‑Join – Hierarchical Data (Employee‑Manager)",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
