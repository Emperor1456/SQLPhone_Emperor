import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE users (id INTEGER, name TEXT, signup_date TEXT);
CREATE TABLE purchases (user_id INTEGER, amount REAL, purchase_date TEXT);
INSERT INTO users VALUES (1,'Emperor','2026-01-01'),(2,'Rahim','2026-01-15');
INSERT INTO purchases VALUES (1,50,'2026-01-05'),(1,30,'2026-02-01'),(2,20,'2026-02-10');
SELECT strftime('%Y-%m', u.signup_date) AS cohort,
       SUM(p.amount) AS total_revenue
FROM users u
JOIN purchases p ON u.id = p.user_id
WHERE p.purchase_date <= date(u.signup_date, '+30 days')
GROUP BY cohort;
"""

EXPECTED = "[('2026-01', 100.0)]"

HINTS = [
    "The WHERE clause filters purchases within 30 days of signup.",
    "The bug is that the GROUP BY uses 'cohort' (an alias), which is allowed in SQLite? Actually SQLite allows column aliases in GROUP BY? No, SQLite doesn't allow aliases in GROUP BY. You must use the expression. So BROKEN has 'GROUP BY cohort' which will cause an error. Fix by using GROUP BY strftime('%Y-%m', u.signup_date).",
    "Replace 'GROUP BY cohort' with 'GROUP BY strftime('%Y-%m', u.signup_date)'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L49 – Module Practice: Cohort Analysis",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
