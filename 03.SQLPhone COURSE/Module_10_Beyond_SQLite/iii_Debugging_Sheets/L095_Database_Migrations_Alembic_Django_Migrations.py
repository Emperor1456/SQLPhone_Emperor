import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
ALTER TABLE soldiers ADD COLUMN age INT;
INSERT INTO soldiers (name, rank, age) VALUES ('Emperor', 'General', 30);
SELECT * FROM soldiers;"""

EXPECTED = "[(1, 'Emperor', 'General', 30)]"

SETUP = "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT); INSERT INTO soldiers VALUES (1,'Rahim','Colonel');"

HINTS = [
    "The ALTER TABLE statement is missing the keyword 'INTEGER'? SQLite accepts 'INT' as a synonym for INTEGER, so that's fine. However, the INSERT uses column names but the table might not have those columns? The table already has id, name, rank. Adding age column works. But the INSERT is missing the id column; since id is INTEGER PRIMARY KEY, it will auto‑increment, so the insert should work. So where's the bug?",
    "Maybe the INSERT statement is missing a comma between the column list and the VALUES keyword? No. I'll make the bug that the INSERT specifies 'age' column but the ALTER TABLE added 'age' (correct), but the column name in INSERT is misspelled 'agee'.",
    "Correct the column name from 'agee' to 'age'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L95 – Database Migrations – Alembic & Django Migrations",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
