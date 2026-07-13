import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE sales (id INTEGER, amount REAL, sale_date TEXT);
INSERT INTO sales VALUES (1,300,'2026-01-15'),(2,250,'2026-01-20'),(3,100,'2026-02-10');
SELECT strftime('%Y-%m', sale_date) AS month, SUM(amount) AS total
FROM sales
GROUP BY month
WHERE total > 500;
"""

EXPECTED = "[('2026-01', 550.0)]"

HINTS = [
    "The WHERE clause cannot be used after GROUP BY.",
    "To filter groups, use HAVING instead of WHERE.",
    "Replace WHERE with HAVING."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L30 – Module 3 Capstone – Monthly Revenue Reports",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
