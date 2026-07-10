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
    levels = {"1": easy, "2": medium, "3": hard}
    while True:
        print("
Choose difficulty:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")
        print("0 - Exit")
        c = input("> ").strip()
        if c == "0":
            break
        task = levels.get(c)
        if task:
            run_task(task)
            cont = input("Try next level? (y/n): ").strip().lower()
            if cont != "y":
                continue
            next_key = str(min(int(c)+1, 3))
            next_task = levels.get(next_key)
            if next_task:
                print(f"
Moving to {next_task.level}...")
                run_task(next_task)

if __name__ == "__main__": main()
