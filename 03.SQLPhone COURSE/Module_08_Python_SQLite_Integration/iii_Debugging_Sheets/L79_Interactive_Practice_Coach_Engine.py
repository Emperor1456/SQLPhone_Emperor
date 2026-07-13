import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE tasks (id INTEGER, description TEXT);
INSERT INTO tasks VALUES (1, 'Learn SQL');
SELECT * FROM task;"""

EXPECTED = "[(1, 'Learn SQL')]"

HINTS = [
    "The SELECT statement references a table that does not exist.",
    "The table is named 'tasks' (plural), not 'task'.",
    "Change `task` to `tasks`."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L79 – Interactive Practice Coach Engine",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
