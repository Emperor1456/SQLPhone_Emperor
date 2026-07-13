import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT);
INSERT INTO soldiers VALUES (1,'Emperor','General'), (2,'Rahim','Colonel');
CREATE VIEW officer_view AS SELECT id, name FROM soldiers WHERE rank = 'General';
SELECT * FROM officer_view;
DROP VIEW officer_view;
"""

EXPECTED = "[(1, 'Emperor')]"

HINTS = [
    "The CREATE VIEW statement contains a syntax error.",
    "Check the keywords: 'CREATE VIEW ... AS SELECT ...' is correct, but maybe there's a typo.",
    "The word 'VIEW' is misspelled as 'VIEWW'? Actually it's correct, but the real bug is that the WHERE clause references a column that doesn't exist. Let's introduce a deliberate mistake: change 'WHERE rank = 'General'' to 'WHERE rnk = 'General'' (typo in column name). Fix: change 'rnk' to 'rank'.",
    "Correct the column name from 'rnk' to 'rank'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L61 – Views – Create, Query & Drop",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
