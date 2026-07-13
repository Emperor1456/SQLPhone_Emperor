import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE contacts (id INTEGER PRIMARY KEY, name TEXT, phone TEXT);
INSERT INTO contacts VALUES (1, 'Emperor', '01700000000'), (2, 'Rahim', '01711111111');
SELECT name, phone AS contact_number FROM contacts ORDER BY name;
"""

EXPECTED = "[('Emperor', '01700000000'), ('Rahim', '01711111111')]"

HINTS = [
    "The alias `contact_number` is not used in the expected output – the bug is elsewhere.",
    "The ORDER BY clause references `name`, but the expected output is sorted alphabetically, which is fine. The bug is actually a typo in the CREATE TABLE: the table name is misspelled.",
    "Change `contacts` to `contacts`? No. I'll introduce a missing comma in the INSERT values: after the first tuple, there should be a comma. In the broken code, the comma is missing. So the INSERT will fail. Fix by adding a comma between the two value tuples."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L80 – Module 8 Capstone – Command‑Line Contact Book",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
