import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
SELECT strftime('%Y-%m', exp_date) AS month,
       SUM(amount) AS total_spent
FROM expenses
GROUP BY month
ORDER BY month;"""

EXPECTED = "[('2026-07', 45.5), ('2026-08', 65.0)]"

SETUP = """\
CREATE TABLE categories (cat_id INTEGER PRIMARY KEY, name TEXT NOT NULL);
INSERT INTO categories VALUES (1,'Food'), (2,'Transport'), (3,'Entertainment');
CREATE TABLE expenses (exp_id INTEGER PRIMARY KEY, amount REAL CHECK(amount > 0), cat_id INTEGER, description TEXT, exp_date TEXT DEFAULT (date('now')), FOREIGN KEY (cat_id) REFERENCES categories(cat_id));
INSERT INTO expenses VALUES (1,15.50,1,'Lunch','2026-07-01'),(2,30.00,2,'Bus pass','2026-07-02'),(3,12.00,1,'Snacks','2026-08-01'),(4,45.00,3,'Cinema','2026-08-05'),(5,8.00,1,'Breakfast','2026-08-10');"""

HINTS = [
    "The query seems correct, but the table name might be misspelled.",
    "Check the FROM clause – it says 'expenses' but the table is 'expenses' (correct). Wait, the bug could be a missing semicolon? No.",
    "I'll introduce a deliberate error: the column 'amount' is misspelled as 'ammount' in the SUM function. Fix it to 'amount'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L86 – Expense Tracker with Monthly Reports",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
