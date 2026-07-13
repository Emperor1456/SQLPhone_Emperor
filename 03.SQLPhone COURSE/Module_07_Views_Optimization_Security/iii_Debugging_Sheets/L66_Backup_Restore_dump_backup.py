import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT);
INSERT INTO soldiers VALUES (1,'Emperor');
.backup soldiers_backup.db
SELECT * FROM soldiers;
"""

EXPECTED = "[(1, 'Emperor')]"

HINTS = [
    "The .backup command is a dot‑command that works only in the SQLite shell, not in standard SQL.",
    "For a portable backup, use the .dump command to generate SQL, but here you just need to remove the invalid line.",
    "Delete the .backup line so the script runs correctly."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L66 – Backup & Restore – .dump & .backup",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
