import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT);
INSERT INTO soldiers VALUES (1,'Emperor','General'),(2,'Rahim','Colonel'),(3,'Ali','Private');
SELECT name,
       CASE rank
           WHEN 'General' THEN 'Officer'
           WHEN 'Colonel' THEN 'Officer'
           ELSE 'Enlisted'
       END AS role
FROM soldiers;
"""

EXPECTED = "[('Emperor', 'Officer'), ('Rahim', 'Officer'), ('Ali', 'Enlisted')]"

HINTS = [
    "The CASE expression is missing a closing keyword.",
    "Every CASE must end with END.",
    "Add END after the ELSE clause."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L15 – CASE – Simple & Searched Conditional Logic",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
