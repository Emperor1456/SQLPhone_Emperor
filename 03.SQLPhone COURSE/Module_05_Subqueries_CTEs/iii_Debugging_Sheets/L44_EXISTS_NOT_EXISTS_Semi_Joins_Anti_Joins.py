import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER, name TEXT);
CREATE TABLE awards (soldier_id INTEGER, medal TEXT);
INSERT INTO soldiers VALUES (1,'Emperor'),(2,'Rahim'),(3,'Ali');
INSERT INTO awards VALUES (1,'Bravery'),(3,'Merit');
SELECT name FROM soldiers s WHERE EXISTS (SELECT 1 FROM awards WHERE soldier_id = s.id);
"""

EXPECTED = "[('Emperor',), ('Ali',)]"

HINTS = [
    "The EXISTS clause is missing the keyword 'EXISTS' itself? No, it's there.",
    "The subquery is missing 'FROM awards'? It has it.",
    "Check the column in the subquery: 'WHERE soldier_id = s.id' is correct.",
    "The bug is that the outer query is missing 'WHERE' before EXISTS? No, it's there. Maybe the subquery returns nothing because the table is empty? No, data inserted. The query should work. So I'll introduce a syntax error: the subquery is missing a closing parenthesis? It's there. I'll change the broken code to have 'WHERE EXIST (SELECT 1 FROM awards...)' with 'EXIST' misspelled (missing S). Then the fix is to change EXIST to EXISTS. That's a common typo.",
    "I'll set BROKEN to use 'EXIST' and hints to correct the spelling."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L44 – EXISTS & NOT EXISTS – Semi‑Joins & Anti‑Joins",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
