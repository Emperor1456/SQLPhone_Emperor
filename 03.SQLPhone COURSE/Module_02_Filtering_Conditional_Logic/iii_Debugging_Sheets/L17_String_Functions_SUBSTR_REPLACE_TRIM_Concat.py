import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT);
INSERT INTO soldiers VALUES (1,'Emperor','General'),(2,'Rahim','Colonel');
SELECT name, REPLACE(rank 'General', 'GEN') AS short_rank FROM soldiers;
"""

EXPECTED = "[('Emperor', 'GEN'), ('Rahim', 'Colonel')]"

HINTS = [
    "Check the function arguments – there's a missing punctuation mark.",
    "Function arguments must be separated by commas.",
    "REPLACE(rank, 'General', 'GEN')"
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L17 – String Functions – SUBSTR, REPLACE, TRIM, ||",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
