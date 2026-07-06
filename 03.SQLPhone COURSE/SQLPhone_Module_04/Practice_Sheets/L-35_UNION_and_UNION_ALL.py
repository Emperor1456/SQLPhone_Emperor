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
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
