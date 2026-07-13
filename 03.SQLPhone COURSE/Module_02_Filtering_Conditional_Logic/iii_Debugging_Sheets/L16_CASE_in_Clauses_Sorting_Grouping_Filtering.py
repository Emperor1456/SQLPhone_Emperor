import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT);
INSERT INTO soldiers VALUES (1,'Emperor','General'),(2,'Rahim','Colonel'),(3,'Ali','Private');
SELECT name, rank FROM soldiers
ORDER BY CASE rank
    WHEN 'General' THEN 1
    WHEN 'Colonel' THEN 2
    ELSE 3
;
"""

EXPECTED = "[('Emperor', 'General'), ('Rahim', 'Colonel'), ('Ali', 'Private')]"

HINTS = [
    "Look at the CASE expression – it's missing its END.",
    "Every CASE must be closed with END.",
    "Add END after the ELSE clause, before the semicolon."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L16 – CASE in Clauses – Sorting, Grouping, Filtering",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
