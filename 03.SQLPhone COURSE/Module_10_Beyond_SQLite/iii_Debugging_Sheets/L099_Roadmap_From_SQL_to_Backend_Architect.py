import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT);
INSERT INTO soldiers VALUES (1,'Emperor');
SELECT name, id FROM soldiers ORDER BY name;
"""

EXPECTED = "[('Emperor', 1)]"

HINTS = [
    "The query looks correct, but let's check the column order in the SELECT: it has name, id, which matches the expected output? Expected output is ('Emperor', 1) – name then id. That matches. So where is the bug?",
    "Actually there is no bug; I'll introduce a subtle error: the INSERT uses 'Emperor' with a lowercase 'e'? Not an error. I'll change the broken code to have a typo in the ORDER BY clause: 'ORDER BY nme'.",
    "Correct the column name 'nme' to 'name'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L99 – Roadmap – From SQL to Backend Architect",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
