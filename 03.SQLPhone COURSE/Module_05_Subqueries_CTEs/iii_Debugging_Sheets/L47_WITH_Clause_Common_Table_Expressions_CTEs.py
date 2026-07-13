import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE sales (id INTEGER, amount REAL, region TEXT);
INSERT INTO sales VALUES (1,100,'North'),(2,200,'South'),(3,150,'North');
WITH regional_sales AS (
    SELECT region, SUM(amount) AS total
    FROM sales
    GROUP BY region
)
SELECT region, total FROM regional_sales
WHERE total > 150;
"""

EXPECTED = "[('North', 250.0)]"

HINTS = [
    "The CTE syntax is correct, but the outer query references a column alias that might not be valid.",
    "Actually the bug is missing the keyword 'WITH' at the beginning? It's there.",
    "Check the GROUP BY: it uses 'region' from the CTE's SELECT, which is fine. But the CTE needs to be defined before the main query? It is. The bug is more subtle: the FROM sales inside the CTE should be 'FROM sales' correct. The error is that there's no comma between the CTE and the main SELECT? The syntax is WITH ... AS (...) SELECT ... no comma needed. So the bug might be the use of 'total' in the WHERE clause without qualifying with the CTE name? But it works. I'll introduce a mistake: the CTE name is misspelled in the outer query: 'regiona_sales' instead of 'regional_sales'. So BROKEN will have that typo, fix to 'regional_sales'.",
    "Hints: The outer query references a CTE that doesn't exist – check the spelling of the CTE name.",
    "Correct the CTE name to 'regional_sales'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L47 – WITH Clause – Common Table Expressions (CTEs)",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
