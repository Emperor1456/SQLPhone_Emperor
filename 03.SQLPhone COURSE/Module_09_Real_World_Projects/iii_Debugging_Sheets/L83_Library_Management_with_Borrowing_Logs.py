import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
SELECT m.name, b.title, bo.due_date
FROM borrowings bo
JOIN members m ON bo.member_id = m.member_id
JOIN books b ON bo.book_id = b.book_id
WHERE bo.return_date IS NULL AND bo.due_date < date('now')"""

EXPECTED = "[('Emperor', 'SQL Mastery', '2026-06-15')]"

SETUP = """\
CREATE TABLE members (member_id INTEGER PRIMARY KEY, name TEXT NOT NULL, join_date TEXT DEFAULT (date('now')));
INSERT INTO members VALUES (1,'Emperor','2026-06-01'),(2,'Rahim','2026-06-15');
CREATE TABLE books (book_id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL, isbn TEXT UNIQUE);
INSERT INTO books VALUES (1,'SQL Mastery','Data King','ISBN-001'),(2,'Python Basics','Code Queen','ISBN-002');
CREATE TABLE borrowings (borrow_id INTEGER PRIMARY KEY, book_id INTEGER, member_id INTEGER, borrow_date TEXT DEFAULT (date('now')), due_date TEXT, return_date TEXT, FOREIGN KEY (book_id) REFERENCES books(book_id), FOREIGN KEY (member_id) REFERENCES members(member_id));
INSERT INTO borrowings VALUES (1,1,1,'2026-06-01','2026-06-15',NULL),(2,2,1,'2026-07-01','2026-07-15','2026-07-10'),(3,1,2,'2026-07-05','2026-07-19',NULL),(4,3,2,'2026-07-01','2026-07-15',NULL);"""

HINTS = [
    "The query is missing a semicolon at the end, but that's not the main issue.",
    "Check the spelling of the table 'borrowings' – it might be misspelled.",
    "In the broken code, the table is written as 'borrowings' but the actual table name is 'borrowings' – that's correct. The bug is actually a missing comma in the SELECT? No. I'll make the broken code have 'borowings' (missing 'r') to be fixed.",
    "Fix the table name 'borowings' to 'borrowings'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L83 – Library Management with Borrowing Logs",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
