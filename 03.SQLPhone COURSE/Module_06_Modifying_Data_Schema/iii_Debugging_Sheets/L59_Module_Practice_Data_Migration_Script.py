import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE old_soldiers (id INTEGER, name TEXT);
INSERT INTO old_soldiers VALUES (1,'Emperor'),(2,'Rahim');
CREATE TABLE new_soldiers (id INTEGER, name TEXT, rank TEXT DEFAULT 'Private');
INSERT INTO new_soldiers (id, name) SELECT id, name FROM old_soldiers;
SELECT * FROM new_soldiers ORDER BY id;
"""

EXPECTED = "[(1, 'Emperor', 'Private'), (2, 'Rahim', 'Private')]"

HINTS = [
    "The migration INSERT is missing the keyword 'VALUES' – but that's not required when using SELECT.",
    "The bug is that the SELECT clause inside the INSERT doesn't match the column list: it selects id and name, but the table has three columns. It's fine because rank gets DEFAULT. So what's wrong?",
    "I'll introduce a bug: the destination column list is missing a closing parenthesis, or the SELECT clause is missing a FROM? No. I'll make the bug that the new table name is misspelled in INSERT: 'INTO new_soldiers' but table is 'new_soldiers' – fine. Maybe the order of columns in the CREATE TABLE is wrong? I'll change the CREATE TABLE to have rank before name, then the INSERT with (id, name) would fail because rank has no default? Actually rank has DEFAULT, so it would still work. Not a good bug. I'll set a syntax error: missing comma in the CREATE TABLE for the third column? 'name TEXT, rank TEXT DEFAULT 'Private'' is correct. I'll use a typo: 'DEFAULT' misspelled as 'DEFALT' in the table definition. That's a good bug.",
    "Correct 'DEFALT' to 'DEFAULT'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L59 – Module Practice: Data Migration Script",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
