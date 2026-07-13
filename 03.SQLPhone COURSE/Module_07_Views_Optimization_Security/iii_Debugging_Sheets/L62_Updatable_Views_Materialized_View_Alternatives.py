import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT);
INSERT INTO soldiers VALUES (1,'Emperor','General'), (2,'Rahim','Colonel');
CREATE VIEW officer_view AS SELECT id, name FROM soldiers WHERE rank = 'General';
INSERT INTO officer_view VALUES (2, 'NewOfficer');
SELECT * FROM soldiers;
"""

EXPECTED = "[(1, 'Emperor', 'General'), (2, 'Rahim', 'Colonel'), (2, 'NewOfficer', 'General')]"

HINTS = [
    "INSERTing into a view that filters rows (WHERE clause) is not directly allowed.",
    "To add a new officer, insert into the base table 'soldiers' with the appropriate rank.",
    "Replace 'INSERT INTO officer_view ...' with 'INSERT INTO soldiers (id, name, rank) VALUES (2, 'NewOfficer', 'General');'"
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L62 – Updatable Views & Materialized View Alternatives",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
