import sys, sqlite3, os
sys.path.append("../..")
from practice_engine import Task, Level, run_task

DB = "contacts_test.db"

def verify_easy(cur, conn):
    # We'll create the table for them? No, they must create it. We'll just check existence.
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='contacts'")
    return cur.fetchone() is not None

easy = Task(
    "Create a 'contacts' table with id, name, phone, email. Include a UNIQUE constraint on email.",
    verify_easy, Level.EASY,
    hints=["CREATE TABLE contacts(id INTEGER PRIMARY KEY, name TEXT NOT NULL, phone TEXT, email TEXT UNIQUE);"]
)

def verify_medium(cur, conn):
    # Insert a contact using parameterized query.
    cur.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", ("Emperor", "000", "e@e.com"))
    conn.commit()
    cur.execute("SELECT name FROM contacts WHERE email = 'e@e.com'")
    return cur.fetchone() == ("Emperor",)

medium = Task(
    "Insert yourself as a contact using a parameterized query.",
    verify_medium, Level.MEDIUM,
    hints=["cur.execute('INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)', ('Emperor', '000', 'e@e.com'))"]
)

def verify_hard(cur, conn):
    # Build a simple menu that lists all contacts.
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    if len(rows) > 0:
        print("Current contacts:")
        for row in rows:
            print(row)
        return True
    return False

hard = Task(
    "Write a loop that displays a menu (1. List contacts, 2. Add contact, 3. Exit) and handles the logic.",
    verify_hard, Level.HARD,
    hints=["Use a while loop with input()."]
)

def main():
    print("1 Easy  2 Medium  3 Hard")
    c = input("> ")
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))
if __name__ == "__main__": main()
