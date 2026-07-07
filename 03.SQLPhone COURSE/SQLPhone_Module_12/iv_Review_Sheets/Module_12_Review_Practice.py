import sys, io, textwrap, traceback
sys.path.append("../..")
from practice_engine import Task, Level

def run_python_task(task):
    print("=" * 44)
    print(f"🧱 TASK [{task.level.upper()}]")
    wrapped = textwrap.fill(task.description, width=48,
                            initial_indent="  📋 ", subsequent_indent="     ")
    print(wrapped)
    print("-" * 44)

    attempts = 0
    while True:
        attempts += 1
        print("\nEnter your Python code below.")
        print("(Blank line to finish, :hint, :quit)")
        lines = []
        while True:
            raw = input("... " if lines else ">>> ").rstrip('\n')
            if raw.strip().lower() in (":quit", "exit"):
                print("Exiting task.")
                return False
            if raw.strip().lower() == ":hint":
                hint = task.next_hint()
                if hint:
                    print(f"💡 HINT: {hint}")
                else:
                    print("No more hints.")
                continue
            if raw == "":
                break
            lines.append(raw)
        user_code = "\n".join(lines)
        if not user_code.strip():
            print("⚠️ No code entered. Try again.")
            continue

        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        user_globals = {}
        try:
            exec(user_code, user_globals)
            output = sys.stdout.getvalue()
        except Exception as e:
            sys.stdout = old_stdout
            print("❌ Error during execution:")
            traceback.print_exc()
            continue
        finally:
            sys.stdout = old_stdout

        if output.strip() == task.expected_output.strip():
            print(f"✅ Correct! ({attempts} attempt{'s' if attempts != 1 else ''})")
            return True
        else:
            print("❌ Output mismatch.")
            print("Expected:")
            print(task.expected_output)
            print("Got:")
            print(output.strip())

# ─── Easy: Connect and fetch with parameterized query ───
easy = Task(
    description="Using sqlite3 and an in‑memory database:\n"
                "- Create table 'users' (id INTEGER PRIMARY KEY, username TEXT, email TEXT)\n"
                "- Insert one row: (1, 'emperor', 'emperor@pyphone.dev')\n"
                "- Use a parameterized query to select the user with username='emperor'\n"
                "- Print the result row exactly as returned by fetchone()",
    expected_output="(1, 'emperor', 'emperor@pyphone.dev')",
    level=Level.EASY,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cur = conn.cursor()",
        "cur.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, email TEXT)')",
        "cur.execute('INSERT INTO users VALUES (1, ?, ?)', ('emperor', 'emperor@pyphone.dev'))",
        "conn.commit()",
        "cur.execute('SELECT * FROM users WHERE username = ?', ('emperor',))",
        "print(cur.fetchone())"
    ]
)

# ─── Medium: Error‑handling with duplicate UNIQUE ─────
medium = Task(
    description="Create table 'contacts' (id INTEGER PRIMARY KEY, email TEXT UNIQUE).\n"
                "Insert two rows with distinct emails, then try to insert a duplicate email.\n"
                "Catch the IntegrityError and print 'Duplicate email'.\n"
                "After that, print all existing rows (one per line).\n"
                "Expected output exactly:\n"
                "(1, 'a@x.com')\n(2, 'b@x.com')\nDuplicate email",
    expected_output="(1, 'a@x.com')\n(2, 'b@x.com')\nDuplicate email",
    level=Level.MEDIUM,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cur = conn.cursor()",
        "cur.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY, email TEXT UNIQUE)')",
        "cur.execute(\"INSERT INTO contacts VALUES (1, 'a@x.com')\")",
        "cur.execute(\"INSERT INTO contacts VALUES (2, 'b@x.com')\")",
        "conn.commit()",
        "try:\n    cur.execute(\"INSERT INTO contacts VALUES (3, 'a@x.com')\")\nexcept sqlite3.IntegrityError:\n    print('Duplicate email')",
        "cur.execute('SELECT * FROM contacts')",
        "for row in cur.fetchall():\n    print(row)"
    ]
)

# ─── Hard: Mini sales report with Python and SQL ─────
hard = Task(
    description="Build a sales report script with Python and SQLite.\n\n"
                "1. Create tables:\n"
                "   - products (id INTEGER PRIMARY KEY, name TEXT, price REAL)\n"
                "   - orders (id INTEGER PRIMARY KEY, product_id INTEGER, qty INTEGER,\n"
                "     FOREIGN KEY(product_id) REFERENCES products(id))\n"
                "2. Insert products: (1,'Widget',10.0), (2,'Gadget',20.0), (3,'Doohickey',5.0)\n"
                "3. Insert orders: (1,1,5), (2,2,3), (3,1,2), (4,3,10)\n"
                "4. Use Python to compute total revenue per product (qty * price) and store in a dict.\n"
                "5. Print each product's name and total revenue, sorted by product name.\n"
                "6. Print the overall total revenue exactly as 'Total: $130.00'\n\n"
                "Expected output:\n"
                "Doohickey 50.00\n"
                "Gadget 60.00\n"
                "Widget 70.00\n"
                "Total: $180.00",
    expected_output="Doohickey 50.00\nGadget 60.00\nWidget 70.00\nTotal: $180.00",
    level=Level.HARD,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cur = conn.cursor()",
        "cur.execute('CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL)')",
        "cur.execute('CREATE TABLE orders (id INTEGER PRIMARY KEY, product_id INTEGER, qty INTEGER, FOREIGN KEY(product_id) REFERENCES products(id))')",
        "cur.executemany('INSERT INTO products VALUES (?,?,?)', [(1,'Widget',10.0), (2,'Gadget',20.0), (3,'Doohickey',5.0)])",
        "cur.executemany('INSERT INTO orders VALUES (?,?,?)', [(1,1,5), (2,2,3), (3,1,2), (4,3,10)])",
        "conn.commit()",
        "cur.execute('SELECT p.name, SUM(o.qty * p.price) FROM products p JOIN orders o ON p.id = o.product_id GROUP BY p.id ORDER BY p.name')",
        "rows = cur.fetchall()",
        "total = 0",
        "for name, rev in rows:",
        "    print(f'{name} {rev:.2f}')",
        "    total += rev",
        "print(f'Total: ${total:.2f}')"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    task = tasks.get(c, easy)
    run_python_task(task)

if __name__ == "__main__":
    main()
