import sys, io, textwrap, traceback
# Re‑use the data classes from the engine, but supply our own Python‑aware runner.
sys.path.append("../..")
from practice_engine import Task, Level  # keep the same task definitions

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

# ─── Easy: Connect, create table, insert, select ───
easy = Task(
    description="Write a Python script that uses sqlite3 to:\n"
                "- Connect to ':memory:'\n"
                "- Create table 'test' (id INT, val TEXT)\n"
                "- Insert (1, 'Emperor')\n"
                "- Select all rows and print the result",
    expected_output="(1, 'Emperor')",
    level=Level.EASY,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cur = conn.cursor()",
        "cur.execute('CREATE TABLE test (id INT, val TEXT)')",
        "cur.execute(\"INSERT INTO test VALUES (1, 'Emperor')\")",
        "conn.commit()",
        "cur.execute('SELECT * FROM test')",
        "print(cur.fetchone())"
    ]
)

# ─── Medium: Parameterized insert and fetchall ─────
medium = Task(
    description="Using an in‑memory database:\n"
                "- Create table 'users' (id INTEGER PRIMARY KEY, name TEXT, email TEXT)\n"
                "- Insert two rows using parameterized queries (?, ?)\n"
                "- Select all rows and print them (one per line)",
    expected_output="(1, 'Alice', 'a@x.com')\n(2, 'Bob', 'b@x.com')",
    level=Level.MEDIUM,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cur = conn.cursor()",
        "cur.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)')",
        "cur.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('Alice', 'a@x.com'))",
        "cur.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('Bob', 'b@x.com'))",
        "conn.commit()",
        "cur.execute('SELECT * FROM users')",
        "for row in cur.fetchall(): print(row)"
    ]
)

# ─── Hard: Mini Contact Book (CRUD) ────────────────
hard = Task(
    description="Build a mini contact book with sqlite3.\n"
                "- Connect to ':memory:'\n"
                "- Create table 'contacts' (id INTEGER PRIMARY KEY, name TEXT, phone TEXT UNIQUE)\n"
                "- Insert two contacts:\n"
                "  ('Emperor', '000') and ('Alice', '123')\n"
                "- Update Alice's phone to '456'\n"
                "- Delete Emperor\n"
                "- Select remaining contacts and print each row on a separate line.\n"
                "Expected output exactly:\n"
                "(2, 'Alice', '456')",
    expected_output="(2, 'Alice', '456')",
    level=Level.HARD,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cur = conn.cursor()",
        "cur.execute('CREATE TABLE contacts (id INTEGER PRIMARY KEY, name TEXT, phone TEXT UNIQUE)')",
        "cur.execute(\"INSERT INTO contacts (name, phone) VALUES ('Emperor', '000')\")",
        "cur.execute(\"INSERT INTO contacts (name, phone) VALUES ('Alice', '123')\")",
        "cur.execute(\"UPDATE contacts SET phone = '456' WHERE name = 'Alice'\")",
        "cur.execute(\"DELETE FROM contacts WHERE name = 'Emperor'\")",
        "conn.commit()",
        "cur.execute('SELECT * FROM contacts')",
        "for row in cur.fetchall(): print(row)"
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
