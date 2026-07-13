import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE sales (id INTEGER, amount REAL, sale_date TEXT);
INSERT INTO sales VALUES (1,100,'2026-01-15'),(2,200,'2026-01-20'),(3,150,'2026-02-10');
SELECT strftime('%Y-%m' sale_date) AS month, SUM(amount) FROM sales GROUP BY month;
"""

EXPECTED = "[('2026-01', 300.0), ('2026-02', 150.0)]"

HINTS = [
    "Look at the arguments inside the strftime() function.",
    "Function arguments must be separated by commas.",
    "Add a comma between '%Y-%m' and sale_date."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L28 – Aggregation with Dates – Period Summaries",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
