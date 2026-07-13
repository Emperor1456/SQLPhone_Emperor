import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE employees (id INTEGER, name TEXT, dept_id INTEGER);
CREATE TABLE sales (id INTEGER, emp_id INTEGER, amount REAL);
INSERT INTO employees VALUES (1,'Emperor',1),(2,'Rahim',2),(3,'Ali',1);
INSERT INTO sales VALUES (1,1,1000),(2,1,500),(3,2,300),(4,3,200);
SELECT e.name, SUM(s.amount) AS total_sales
FROM employees e
JOIN sales s ON e.id = s.emp_id
WHERE total_sales > 500
GROUP BY e.name;
"""

EXPECTED = "[('Emperor', 1500.0)]"

HINTS = [
    "The WHERE clause uses an alias 'total_sales' which is not allowed.",
    "Use HAVING instead of WHERE to filter on aggregate results.",
    "Replace 'WHERE total_sales > 500' with 'HAVING SUM(s.amount) > 500'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L50 – Module 5 Capstone – Employee Performance Tracker",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
