import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT UNIQUE)")
    cur.execute("INSERT INTO users(email) VALUES ('test@example.com')")
    return True

easy = Task(
    "We have a 'users' table with UNIQUE email. Write Python code that tries to insert a duplicate email and handles the IntegrityError.",
    verify_easy, Level.EASY,
    hints=["try:\n    cur.execute(\"INSERT INTO users(email) VALUES ('test@example.com')\")\nexcept sqlite3.IntegrityError:\n    print('Duplicate!')"]
)

def verify_medium(cur, conn):
    # The user code should have caught the exception; we'll check that the row count is still 1.
    cur.execute("SELECT COUNT(*) FROM users")
    return cur.fetchone()[0] == 1

medium = Task(
    "Only the original row should remain; the duplicate insert was caught.",
    verify_medium, Level.MEDIUM,
    hints=["Check the number of rows with SELECT COUNT(*)."]
)

def verify_hard(cur, conn):
    # Attempt to insert with incorrect column (OperationalError)
    try:
        cur.execute("INSERT INTO users(id, email) VALUES (2, 'test2@example.com')")
        conn.commit()
    except:
        return True
    return False  # shouldn't reach here; we just want to show error handling

hard = Task(
    "Try to insert a row with a missing column (should raise OperationalError). Catch it and print a custom message.",
    verify_hard, Level.HARD,
    hints=["Use a generic except sqlite3.Error and print('Database error occurred')."]
)

def main():
    print("1 Easy  2 Medium  3 Hard")
    c = input("> ")
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))
if __name__ == "__main__": main()
