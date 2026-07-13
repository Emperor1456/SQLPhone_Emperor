import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📇  Create the Contacts Table\n\n"
        "Write Python code that:\n"
        "  1. Connects to :memory:.\n"
        "  2. Creates a table `contacts` with columns:\n"
        "     id INTEGER PRIMARY KEY,\n"
        "     name TEXT NOT NULL,\n"
        "     phone TEXT NOT NULL,\n"
        "     email TEXT.\n"
        "  3. Inserts one contact:\n"
        "     (1, 'Emperor', '01700000000', 'emperor@empire.com').\n"
        "  4. SELECTs all rows and prints them.\n\n"
        "Expected output:\n[(1, 'Emperor', '01700000000', 'emperor@empire.com')]"
    ),
    expected_output="[(1, 'Emperor', '01700000000', 'emperor@empire.com')]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('''CREATE TABLE contacts (id INTEGER PRIMARY KEY, name TEXT NOT NULL, phone TEXT NOT NULL, email TEXT)''')",
        "conn.execute(\"INSERT INTO contacts VALUES (1, 'Emperor', '01700000000', 'emperor@empire.com')\")",
        "conn.commit()",
        "cur = conn.execute('SELECT * FROM contacts')",
        "print(cur.fetchall())",
    ]
)

easy2 = Task(
    description=(
        "➕  Add Contact Function\n\n"
        "Write a function `add_contact(conn, name, phone, email)`\n"
        "that inserts a new row into `contacts` (id is NULL so\n"
        "it auto‑increments). Then call it to add 'Rahim' with\n"
        "phone '01711111111' and email 'rahim@empire.com'.\n"
        "Commit and SELECT all rows, print the result.\n\n"
        "Expected output:\n[(1, 'Emperor', '01700000000', 'emperor@empire.com'), (2, 'Rahim', '01711111111', 'rahim@empire.com')]"
    ),
    setup_sql=(
        "CREATE TABLE contacts (id INTEGER PRIMARY KEY, name TEXT NOT NULL, phone TEXT NOT NULL, email TEXT);"
        "INSERT INTO contacts VALUES (1, 'Emperor', '01700000000', 'emperor@empire.com');"
    ),
    expected_output="[(1, 'Emperor', '01700000000', 'emperor@empire.com'), (2, 'Rahim', '01711111111', 'rahim@empire.com')]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "def add_contact(conn, name, phone, email):",
        "    conn.execute('INSERT INTO contacts (name, phone, email) VALUES (?,?,?)', (name, phone, email))",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('''CREATE TABLE contacts (id INTEGER PRIMARY KEY, name TEXT NOT NULL, phone TEXT NOT NULL, email TEXT)''')",
        "conn.execute(\"INSERT INTO contacts VALUES (1, 'Emperor', '01700000000', 'emperor@empire.com')\")",
        "add_contact(conn, 'Rahim', '01711111111', 'rahim@empire.com')",
        "conn.commit()",
        "cur = conn.execute('SELECT * FROM contacts ORDER BY id')",
        "print(cur.fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔍  Search Contacts by Name\n\n"
        "The `contacts` table has 3 rows (Emperor, Rahim, Ali).\n"
        "Write a function `search_by_name(conn, keyword)` that\n"
        "uses `LIKE` to find contacts whose name contains the\n"
        "keyword (case‑sensitive). Call it with keyword 'Ra'\n"
        "and print the matching rows.\n\n"
        "Expected output:\n[(2, 'Rahim', '01711111111', 'rahim@empire.com')]"
    ),
    setup_sql=(
        "CREATE TABLE contacts (id INTEGER PRIMARY KEY, name TEXT NOT NULL, phone TEXT NOT NULL, email TEXT);"
        "INSERT INTO contacts VALUES (1,'Emperor','01700000000','emperor@empire.com'),(2,'Rahim','01711111111','rahim@empire.com'),(3,'Ali','01722222222','ali@empire.com');"
    ),
    expected_output="[(2, 'Rahim', '01711111111', 'rahim@empire.com')]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "def search_by_name(conn, keyword):",
        "    cur = conn.execute('SELECT * FROM contacts WHERE name LIKE ?', ('%' + keyword + '%',))",
        "    return cur.fetchall()",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript('''... (create and insert as in setup_sql) ...''')",
        "result = search_by_name(conn, 'Ra')",
        "print(result)",
    ]
)

medium2 = Task(
    description=(
        "✏️  Update Contact Phone Number\n\n"
        "The `contacts` table has 3 rows.\n"
        "Write a function `update_phone(conn, contact_id, new_phone)`\n"
        "that updates the phone number for a given id.\n"
        "Call it to change Ali's phone to '01733333333'.\n"
        "Commit and SELECT the updated row (id=3), print it.\n\n"
        "Expected output:\n(3, 'Ali', '01733333333', 'ali@empire.com')"
    ),
    setup_sql=(
        "CREATE TABLE contacts (id INTEGER PRIMARY KEY, name TEXT NOT NULL, phone TEXT NOT NULL, email TEXT);"
        "INSERT INTO contacts VALUES (1,'Emperor','01700000000','emperor@empire.com'),(2,'Rahim','01711111111','rahim@empire.com'),(3,'Ali','01722222222','ali@empire.com');"
    ),
    expected_output="(3, 'Ali', '01733333333', 'ali@empire.com')",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "def update_phone(conn, contact_id, new_phone):",
        "    conn.execute('UPDATE contacts SET phone = ? WHERE id = ?', (new_phone, contact_id))",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript('''... (create and insert) ...''')",
        "update_phone(conn, 3, '01733333333')",
        "conn.commit()",
        "cur = conn.execute('SELECT * FROM contacts WHERE id = 3')",
        "print(cur.fetchone())",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🗑️  Delete Contact & List All\n\n"
        "The `contacts` table has 3 rows.\n"
        "Write a function `delete_contact(conn, contact_id)`\n"
        "that removes a contact. Call it to delete Rahim (id=2).\n"
        "Commit and then SELECT all remaining rows, ordered by id.\n"
        "Print the result.\n\n"
        "Expected output:\n[(1, 'Emperor', '01700000000', 'emperor@empire.com'), (3, 'Ali', '01722222222', 'ali@empire.com')]"
    ),
    setup_sql=(
        "CREATE TABLE contacts (id INTEGER PRIMARY KEY, name TEXT NOT NULL, phone TEXT NOT NULL, email TEXT);"
        "INSERT INTO contacts VALUES (1,'Emperor','01700000000','emperor@empire.com'),(2,'Rahim','01711111111','rahim@empire.com'),(3,'Ali','01722222222','ali@empire.com');"
    ),
    expected_output="[(1, 'Emperor', '01700000000', 'emperor@empire.com'), (3, 'Ali', '01722222222', 'ali@empire.com')]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "def delete_contact(conn, contact_id):",
        "    conn.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript('''...''')",
        "delete_contact(conn, 2)",
        "conn.commit()",
        "cur = conn.execute('SELECT * FROM contacts ORDER BY id')",
        "print(cur.fetchall())",
    ]
)

hard2 = Task(
    description=(
        "📋  Mini CLI Menu – List / Add / Quit\n\n"
        "Simulate a command‑line interface that:\n"
        "  1. Creates the `contacts` table.\n"
        "  2. Inserts one contact ('Emperor', '01700000000', 'emperor@empire.com').\n"
        "  3. Enters a loop that reads commands:\n"
        "     'list' → prints all contacts\n"
        "     'add' → adds a hardcoded second contact ('Rahim', ...)\n"
        "     'quit' → breaks the loop and prints 'Goodbye!'\n"
        "Instead of real input(), use a predefined list of commands:\n"
        "['list', 'add', 'list', 'quit'] and process them in order.\n"
        "Print each command's result exactly as described.\n\n"
        "Expected output:\n"
        "[(1, 'Emperor', '01700000000', 'emperor@empire.com')]\n"
        "[(1, 'Emperor', '01700000000', 'emperor@empire.com'), (2, 'Rahim', '01711111111', 'rahim@empire.com')]\n"
        "Goodbye!"
    ),
    expected_output="[(1, 'Emperor', '01700000000', 'emperor@empire.com')]\n[(1, 'Emperor', '01700000000', 'emperor@empire.com'), (2, 'Rahim', '01711111111', 'rahim@empire.com')]\nGoodbye!",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('''CREATE TABLE contacts (id INTEGER PRIMARY KEY, name TEXT NOT NULL, phone TEXT NOT NULL, email TEXT)''')",
        "conn.execute(\"INSERT INTO contacts VALUES (1, 'Emperor', '01700000000', 'emperor@empire.com')\")",
        "conn.commit()",
        "commands = ['list', 'add', 'list', 'quit']",
        "for cmd in commands:",
        "    if cmd == 'list':",
        "        cur = conn.execute('SELECT * FROM contacts ORDER BY id')",
        "        print(cur.fetchall())",
        "    elif cmd == 'add':",
        "        conn.execute(\"INSERT INTO contacts (name, phone, email) VALUES ('Rahim', '01711111111', 'rahim@empire.com')\")",
        "        conn.commit()",
        "    elif cmd == 'quit':",
        "        print('Goodbye!')",
        "        break",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L80.json",
        module_name="Module_08_Python_SQLite_Integration",
        lesson_name="L80_Module_8_Capstone_Contact_Book"
    )