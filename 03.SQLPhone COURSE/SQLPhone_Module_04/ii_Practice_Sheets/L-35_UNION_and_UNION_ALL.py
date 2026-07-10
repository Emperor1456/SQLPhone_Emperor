import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE current_employees(id INTEGER, name TEXT)")
    cur.execute("CREATE TABLE former_employees(id INTEGER, name TEXT)")
    cur.executemany("INSERT INTO current_employees VALUES (?,?)", [(1,'Alice'),(2,'Bob')])
    cur.executemany("INSERT INTO former_employees VALUES (?,?)", [(3,'Charlie'),(2,'Bob')])
    return True

easy = Task("We have current and former employees. Write a UNION query to get a combined list without duplicates.",
            verify_easy, Level.EASY,
            hints=["SELECT name FROM current_employees UNION SELECT name FROM former_employees;"])

def verify_medium(cur, conn):
    cur.execute("SELECT name FROM current_employees UNION SELECT name FROM former_employees")
    rows = cur.fetchall()
    return len(rows) == 3  # Alice, Bob, Charlie

medium = Task("UNION should give 3 rows (duplicate 'Bob' removed).",
              verify_medium, Level.MEDIUM,
              hints=["Check that you used UNION (not UNION ALL)."])

def verify_hard(cur, conn):
    cur.execute("SELECT name FROM current_employees UNION ALL SELECT name FROM former_employees")
    rows = cur.fetchall()
    return len(rows) == 4

hard = Task("Now use UNION ALL to get all rows including duplicates (should be 4 rows).",
            verify_hard, Level.HARD,
            hints=["SELECT name FROM current_employees UNION ALL SELECT name FROM former_employees;"])


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

if __name__=="__main__": main()
