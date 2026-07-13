import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE events (id INTEGER, name TEXT, event_date TEXT);
INSERT INTO events VALUES (1,'Battle','2026-07-14');
SELECT name, strftime('%Y-%m-%d' 'now') AS today FROM events;
"""

EXPECTED = "[('Battle', '2026-07-14')]"

HINTS = [
    "The strftime() function requires arguments separated by commas.",
    "There's a missing comma between the format and the date value.",
    "Use: strftime('%Y-%m-%d', 'now')"
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L18 – Date & Time Functions – date(), time(), strftime()",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
