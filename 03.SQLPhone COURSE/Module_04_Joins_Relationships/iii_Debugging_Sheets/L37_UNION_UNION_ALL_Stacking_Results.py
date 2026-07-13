import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE active (name TEXT);
CREATE TABLE reserve (name TEXT);
INSERT INTO active VALUES ('Emperor'),('Ali');
INSERT INTO reserve VALUES ('Rahim'),('Hasan');
SELECT name FROM active UNION ALL SELECT name FROM reserve ORDER BY name;
"""

EXPECTED = "[('Ali',), ('Emperor',), ('Hasan',), ('Rahim',)]"

HINTS = [
    "The query looks fine but returns duplicate names if any? No duplicates.",
    "Actually the bug is that UNION ALL keeps duplicates, but the expected output sorted alphabetically with no duplicates – which UNION ALL would produce if there were none. So what's wrong?",
    "Perhaps the ORDER BY clause is applied to the whole UNION, but without parentheses, it might only apply to the second SELECT. No, in SQLite it applies to the whole compound. So the bug is something else.",
    "The bug: the second table is 'reserve', but the column name in CREATE TABLE is also 'name'. All good. The only issue could be that the INSERT into reserve uses 'Rahim' twice? No.",
    "Let's look at the expected output: it's sorted ascending, which is correct. So maybe the bug is a missing comma in the INSERT of active? It has 'Emperor','Ali' – correct. So the bug must be that the ORDER BY is missing the column alias? No. I'll change the broken code to have a subtle mistake: the second SELECT doesn't have a table alias, but that's fine.",
    "I'll instead introduce a bug where the second table name is misspelled: 'reserve' vs 'reserves'? In the broken code, I'll write FROM reserve but table is 'reserve', correct. So no bug. To create a bug, I'll change the broken code to 'SELECT name FROM active UNION SELECT name FROM reserve' which is UNION (removes duplicates), but the expected output has no duplicates anyway. So the behavior is the same. Not a bug.",
    "I'll make the broken code have 'SELECT name FROM active UNION ALL SELECT name FROM reserve' but then the expected output is sorted, but the query might not sort if ORDER BY is missing? I'll remove ORDER BY from broken code, then expected output would be whatever order, but I'll set expected to be sorted, and hint to add ORDER BY. That's a bug: missing ORDER BY. So I'll craft BROKEN without ORDER BY. Then hints: Add ORDER BY name. Expected output sorted. That's a good bug: they need to add ORDER BY to sort.",
    "I'll set BROKEN without ORDER BY, and EXPECTED as sorted list. Hints guide to add ORDER BY name."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L37 – UNION & UNION ALL – Stacking Results",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
