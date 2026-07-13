import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE accounts (id INTEGER PRIMARY KEY, balance REAL);
INSERT INTO accounts VALUES (1, 1000), (2, 500);
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 200 WHERE id = 1;
UPDATE accounts SET balance = balance + 200 WHERE id = 2;
COMMIT;
SELECT * FROM accounts ORDER BY id;
"""

EXPECTED = "[(1, 800.0), (2, 700.0)]"

HINTS = [
    "The transaction is started with 'BEGIN TRANSACTION' but the 'TRANSACTION' keyword is optional; the bug is that the rollback is not used here, but that's not an error.",
    "The real bug is that the COMMIT statement is misspelled as 'COMMITT'? I'll change it in BROKEN to 'COMMITT' (extra T).",
    "Fix 'COMMITT' to 'COMMIT'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L58 – Transactions – BEGIN, COMMIT, ROLLBACK",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
