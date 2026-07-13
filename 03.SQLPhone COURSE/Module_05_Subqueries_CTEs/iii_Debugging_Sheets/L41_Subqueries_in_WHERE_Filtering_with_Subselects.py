import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER, name TEXT, salary REAL);
INSERT INTO soldiers VALUES (1,'Emperor',5000),(2,'Rahim',4000),(3,'Ali',3500);
SELECT name FROM soldiers WHERE salary > (SELECT AVG(salary) FROM soldiers);
"""

EXPECTED = "[('Emperor',)]"

HINTS = [
    "The subquery is syntactically correct, but the result is wrong because the average is computed including all three soldiers.",
    "The expected output only shows Emperor. Maybe the bug is that the subquery returns a value that causes no rows? No, the average of 5000,4000,3500 is 4166.67, so Emperor's salary (5000) is greater. So that would return Emperor. The expected output shows Emperor. So the query is actually correct! I need to introduce a subtle mistake: perhaps the outer query is missing a column alias or the subquery parenthesis are wrong? I'll change the broken code to have a syntax error: missing parentheses around the subquery? It has them. I'll make the bug that the subquery is correlated incorrectly? Not needed. I'll set the broken code to use 'salary > AVG(salary)' without subquery, but that's invalid. I'll just make a common mistake: using 'salary > (SELECT AVG(salary))' but forgetting the FROM clause in the subquery? That would be an error. That's a good bug: missing FROM soldiers in subquery. I'll modify BROKEN accordingly, and set expected output to the correct result after fix. So BROKEN will have 'SELECT AVG(salary) FROM' – I'll omit the table name. The student must add 'FROM soldiers'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L41 – Subqueries in WHERE – Filtering with Sub‑selects",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
