import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📚  Imperial Library – Build the Catalog\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates the three tables:\n"
        "     members, books, borrowings\n"
        "     (exact schema from the lecture).\n"
        "  3. Inserts seed data:\n"
        "     • 2 members: Emperor (1), Rahim (2)\n"
        "     • 4 books:\n"
        "       (1,'SQL Mastery','Data King','ISBN-001')\n"
        "       (2,'Python Basics','Code Queen','ISBN-002')\n"
        "       (3,'Data Science','Analytics Guru','ISBN-003')\n"
        "       (4,'Advanced SQL','Data King','ISBN-004')\n"
        "  4. Commits, then SELECTs all book titles\n"
        "     sorted alphabetically and prints them.\n\n"
        "Expected output:\n[('Advanced SQL',), ('Data Science',), ('Python Basics',), ('SQL Mastery',)]"
    ),
    expected_output="[('Advanced SQL',), ('Data Science',), ('Python Basics',), ('SQL Mastery',)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript('''",
        "CREATE TABLE members (member_id INTEGER PRIMARY KEY, name TEXT NOT NULL, join_date TEXT DEFAULT (date('now')));",
        "CREATE TABLE books (book_id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL, isbn TEXT UNIQUE);",
        "CREATE TABLE borrowings (borrow_id INTEGER PRIMARY KEY, book_id INTEGER, member_id INTEGER, borrow_date TEXT DEFAULT (date('now')), due_date TEXT, return_date TEXT, FOREIGN KEY (book_id) REFERENCES books(book_id), FOREIGN KEY (member_id) REFERENCES members(member_id));",
        "''')",
        "conn.executescript('''",
        "INSERT INTO members VALUES (1,'Emperor','2026-06-01');",
        "INSERT INTO members VALUES (2,'Rahim','2026-06-15');",
        "INSERT INTO books VALUES (1,'SQL Mastery','Data King','ISBN-001');",
        "INSERT INTO books VALUES (2,'Python Basics','Code Queen','ISBN-002');",
        "INSERT INTO books VALUES (3,'Data Science','Analytics Guru','ISBN-003');",
        "INSERT INTO books VALUES (4,'Advanced SQL','Data King','ISBN-004');",
        "''')",
        "conn.commit()",
        "cursor = conn.execute('SELECT title FROM books ORDER BY title')",
        "print(cursor.fetchall())",
    ]
)

easy2 = Task(
    description=(
        "🔗  Active Borrowings – Who Has What\n\n"
        "The library database is already seeded with borrowings.\n"
        "Write Python code that joins borrowings, members, and\n"
        "books to show each borrowing with:\n"
        "  member name, book title, borrow_date, due_date,\n"
        "  return_date.\n"
        "Sort by borrow_id.\n\n"
        "Expected output:\n"
        "[(1,'Emperor','SQL Mastery','2026-06-01','2026-06-15',None),\n"
        " (2,'Emperor','Python Basics','2026-07-01','2026-07-15','2026-07-10'),\n"
        " (3,'Rahim','SQL Mastery','2026-07-05','2026-07-19',None),\n"
        " (4,'Rahim','Data Science','2026-07-01','2026-07-15',None)]"
    ),
    setup_sql=(
        "CREATE TABLE members (member_id INTEGER PRIMARY KEY, name TEXT NOT NULL, join_date TEXT DEFAULT (date('now')));"
        "INSERT INTO members VALUES (1,'Emperor','2026-06-01');"
        "INSERT INTO members VALUES (2,'Rahim','2026-06-15');"
        "CREATE TABLE books (book_id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL, isbn TEXT UNIQUE);"
        "INSERT INTO books VALUES (1,'SQL Mastery','Data King','ISBN-001');"
        "INSERT INTO books VALUES (2,'Python Basics','Code Queen','ISBN-002');"
        "INSERT INTO books VALUES (3,'Data Science','Analytics Guru','ISBN-003');"
        "INSERT INTO books VALUES (4,'Advanced SQL','Data King','ISBN-004');"
        "CREATE TABLE borrowings (borrow_id INTEGER PRIMARY KEY, book_id INTEGER, member_id INTEGER, borrow_date TEXT DEFAULT (date('now')), due_date TEXT, return_date TEXT, FOREIGN KEY (book_id) REFERENCES books(book_id), FOREIGN KEY (member_id) REFERENCES members(member_id));"
        "INSERT INTO borrowings VALUES (1,1,1,'2026-06-01','2026-06-15',NULL);"
        "INSERT INTO borrowings VALUES (2,2,1,'2026-07-01','2026-07-15','2026-07-10');"
        "INSERT INTO borrowings VALUES (3,1,2,'2026-07-05','2026-07-19',NULL);"
        "INSERT INTO borrowings VALUES (4,3,2,'2026-07-01','2026-07-15',NULL);"
    ),
    expected_output=(
        "[(1, 'Emperor', 'SQL Mastery', '2026-06-01', '2026-06-15', None), "
        "(2, 'Emperor', 'Python Basics', '2026-07-01', '2026-07-15', '2026-07-10'), "
        "(3, 'Rahim', 'SQL Mastery', '2026-07-05', '2026-07-19', None), "
        "(4, 'Rahim', 'Data Science', '2026-07-01', '2026-07-15', None)]"
    ),
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT bo.borrow_id, m.name, b.title, bo.borrow_date, bo.due_date, bo.return_date",
        "FROM borrowings bo JOIN members m ON bo.member_id = m.member_id",
        "JOIN books b ON bo.book_id = b.book_id",
        "ORDER BY bo.borrow_id",
        "''')",
        "print(cursor.fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "⚠️  Overdue Books – Past Due & Not Returned\n\n"
        "The library database is seeded.\n"
        "Write Python code that lists overdue books as of\n"
        "the fixed date '2026-07-13':\n"
        "  • books whose due_date is before '2026-07-13'\n"
        "  • and return_date IS NULL.\n"
        "Show member name, book title, due_date.\n"
        "Sort by due_date.\n\n"
        "Expected output:\n[('Emperor','SQL Mastery','2026-06-15')]"
    ),
    setup_sql=(
        "CREATE TABLE members (member_id INTEGER PRIMARY KEY, name TEXT NOT NULL, join_date TEXT DEFAULT (date('now')));"
        "INSERT INTO members VALUES (1,'Emperor','2026-06-01');"
        "INSERT INTO members VALUES (2,'Rahim','2026-06-15');"
        "CREATE TABLE books (book_id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL, isbn TEXT UNIQUE);"
        "INSERT INTO books VALUES (1,'SQL Mastery','Data King','ISBN-001');"
        "INSERT INTO books VALUES (2,'Python Basics','Code Queen','ISBN-002');"
        "INSERT INTO books VALUES (3,'Data Science','Analytics Guru','ISBN-003');"
        "INSERT INTO books VALUES (4,'Advanced SQL','Data King','ISBN-004');"
        "CREATE TABLE borrowings (borrow_id INTEGER PRIMARY KEY, book_id INTEGER, member_id INTEGER, borrow_date TEXT DEFAULT (date('now')), due_date TEXT, return_date TEXT, FOREIGN KEY (book_id) REFERENCES books(book_id), FOREIGN KEY (member_id) REFERENCES members(member_id));"
        "INSERT INTO borrowings VALUES (1,1,1,'2026-06-01','2026-06-15',NULL);"
        "INSERT INTO borrowings VALUES (2,2,1,'2026-07-01','2026-07-15','2026-07-10');"
        "INSERT INTO borrowings VALUES (3,1,2,'2026-07-05','2026-07-19',NULL);"
        "INSERT INTO borrowings VALUES (4,3,2,'2026-07-01','2026-07-15',NULL);"
    ),
    expected_output="[('Emperor', 'SQL Mastery', '2026-06-15')]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT m.name, b.title, bo.due_date",
        "FROM borrowings bo JOIN members m ON bo.member_id = m.member_id",
        "JOIN books b ON bo.book_id = b.book_id",
        "WHERE bo.return_date IS NULL AND bo.due_date < '2026-07-13'",
        "ORDER BY bo.due_date",
        "''')",
        "print(cursor.fetchall())",
    ]
)

medium2 = Task(
    description=(
        "📊  Members with Books Currently Out\n\n"
        "The library database is seeded.\n"
        "Write Python code that counts how many books each\n"
        "member currently has borrowed (return_date IS NULL).\n"
        "Show member name and the count.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Emperor', 1), ('Rahim', 2)]"
    ),
    setup_sql=(
        "CREATE TABLE members (member_id INTEGER PRIMARY KEY, name TEXT NOT NULL, join_date TEXT DEFAULT (date('now')));"
        "INSERT INTO members VALUES (1,'Emperor','2026-06-01');"
        "INSERT INTO members VALUES (2,'Rahim','2026-06-15');"
        "CREATE TABLE books (book_id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL, isbn TEXT UNIQUE);"
        "INSERT INTO books VALUES (1,'SQL Mastery','Data King','ISBN-001');"
        "INSERT INTO books VALUES (2,'Python Basics','Code Queen','ISBN-002');"
        "INSERT INTO books VALUES (3,'Data Science','Analytics Guru','ISBN-003');"
        "INSERT INTO books VALUES (4,'Advanced SQL','Data King','ISBN-004');"
        "CREATE TABLE borrowings (borrow_id INTEGER PRIMARY KEY, book_id INTEGER, member_id INTEGER, borrow_date TEXT DEFAULT (date('now')), due_date TEXT, return_date TEXT, FOREIGN KEY (book_id) REFERENCES books(book_id), FOREIGN KEY (member_id) REFERENCES members(member_id));"
        "INSERT INTO borrowings VALUES (1,1,1,'2026-06-01','2026-06-15',NULL);"
        "INSERT INTO borrowings VALUES (2,2,1,'2026-07-01','2026-07-15','2026-07-10');"
        "INSERT INTO borrowings VALUES (3,1,2,'2026-07-05','2026-07-19',NULL);"
        "INSERT INTO borrowings VALUES (4,3,2,'2026-07-01','2026-07-15',NULL);"
    ),
    expected_output="[('Emperor', 1), ('Rahim', 2)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT m.name, COUNT(bo.borrow_id) AS books_out",
        "FROM members m JOIN borrowings bo ON m.member_id = bo.member_id",
        "WHERE bo.return_date IS NULL GROUP BY m.member_id ORDER BY m.name",
        "''')",
        "print(cursor.fetchall())",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🏆  Most Borrowed Books – Top 3\n\n"
        "The library database is seeded with multiple borrowings.\n"
        "Write Python code that lists the three most borrowed\n"
        "books (counting all borrowings, even returned).\n"
        "Show title and borrow count.\n"
        "Order by count descending, then title ascending.\n\n"
        "Expected output:\n[('SQL Mastery',2), ('Data Science',1), ('Python Basics',1)]"
    ),
    setup_sql=(
        "CREATE TABLE members (member_id INTEGER PRIMARY KEY, name TEXT NOT NULL, join_date TEXT DEFAULT (date('now')));"
        "INSERT INTO members VALUES (1,'Emperor','2026-06-01');"
        "INSERT INTO members VALUES (2,'Rahim','2026-06-15');"
        "CREATE TABLE books (book_id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL, isbn TEXT UNIQUE);"
        "INSERT INTO books VALUES (1,'SQL Mastery','Data King','ISBN-001');"
        "INSERT INTO books VALUES (2,'Python Basics','Code Queen','ISBN-002');"
        "INSERT INTO books VALUES (3,'Data Science','Analytics Guru','ISBN-003');"
        "INSERT INTO books VALUES (4,'Advanced SQL','Data King','ISBN-004');"
        "CREATE TABLE borrowings (borrow_id INTEGER PRIMARY KEY, book_id INTEGER, member_id INTEGER, borrow_date TEXT DEFAULT (date('now')), due_date TEXT, return_date TEXT, FOREIGN KEY (book_id) REFERENCES books(book_id), FOREIGN KEY (member_id) REFERENCES members(member_id));"
        "INSERT INTO borrowings VALUES (1,1,1,'2026-06-01','2026-06-15',NULL);"
        "INSERT INTO borrowings VALUES (2,2,1,'2026-07-01','2026-07-15','2026-07-10');"
        "INSERT INTO borrowings VALUES (3,1,2,'2026-07-05','2026-07-19',NULL);"
        "INSERT INTO borrowings VALUES (4,3,2,'2026-07-01','2026-07-15',NULL);"
    ),
    expected_output="[('SQL Mastery', 2), ('Data Science', 1), ('Python Basics', 1)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT b.title, COUNT(bo.borrow_id) AS times_borrowed",
        "FROM books b JOIN borrowings bo ON b.book_id = bo.book_id",
        "GROUP BY b.book_id ORDER BY times_borrowed DESC, b.title ASC LIMIT 3",
        "''')",
        "print(cursor.fetchall())",
    ]
)

hard2 = Task(
    description=(
        "🔍  Books Never Borrowed\n\n"
        "The library database contains a book that has never\n"
        "been borrowed ('Advanced SQL').\n"
        "Write Python code that finds the titles of all books\n"
        "that do not appear in the borrowings table.\n"
        "Sort by title.\n\n"
        "Expected output:\n[('Advanced SQL',)]"
    ),
    setup_sql=(
        "CREATE TABLE members (member_id INTEGER PRIMARY KEY, name TEXT NOT NULL, join_date TEXT DEFAULT (date('now')));"
        "INSERT INTO members VALUES (1,'Emperor','2026-06-01');"
        "INSERT INTO members VALUES (2,'Rahim','2026-06-15');"
        "CREATE TABLE books (book_id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL, isbn TEXT UNIQUE);"
        "INSERT INTO books VALUES (1,'SQL Mastery','Data King','ISBN-001');"
        "INSERT INTO books VALUES (2,'Python Basics','Code Queen','ISBN-002');"
        "INSERT INTO books VALUES (3,'Data Science','Analytics Guru','ISBN-003');"
        "INSERT INTO books VALUES (4,'Advanced SQL','Data King','ISBN-004');"
        "CREATE TABLE borrowings (borrow_id INTEGER PRIMARY KEY, book_id INTEGER, member_id INTEGER, borrow_date TEXT DEFAULT (date('now')), due_date TEXT, return_date TEXT, FOREIGN KEY (book_id) REFERENCES books(book_id), FOREIGN KEY (member_id) REFERENCES members(member_id));"
        "INSERT INTO borrowings VALUES (1,1,1,'2026-06-01','2026-06-15',NULL);"
        "INSERT INTO borrowings VALUES (2,2,1,'2026-07-01','2026-07-15','2026-07-10');"
        "INSERT INTO borrowings VALUES (3,1,2,'2026-07-05','2026-07-19',NULL);"
        "INSERT INTO borrowings VALUES (4,3,2,'2026-07-01','2026-07-15',NULL);"
    ),
    expected_output="[('Advanced SQL',)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''SELECT title FROM books WHERE book_id NOT IN (SELECT book_id FROM borrowings) ORDER BY title''')",
        "print(cursor.fetchall())",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L83.json",
        module_name="Module_09_Real_World_Projects",
        lesson_name="L83_Library_Management_with_Borrowing_Logs"
    )