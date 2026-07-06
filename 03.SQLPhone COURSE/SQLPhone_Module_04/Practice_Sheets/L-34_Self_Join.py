import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE staff(id INTEGER PRIMARY KEY, name TEXT, manager_id INTEGER)")
    cur.executemany("INSERT INTO staff VALUES (?,?,?)", [(1,'Alice',NULL),(2,'Bob',1),(3,'Charlie',1),(4,'Dave',2)])
    return True

easy = Task("We've created 'staff' with a self-referencing manager_id. Write a self‑join to display each employee's name and their manager's name.",
            verify_easy, Level.EASY,
            hints=["SELECT e.name AS employee, m.name AS manager FROM staff e LEFT JOIN staff m ON e.manager_id = m.id;"])

def verify_medium(cur, conn):
    cur.execute("SELECT e.name, m.name FROM staff e LEFT JOIN staff m ON e.manager_id = m.id")
    rows = cur.fetchall()
    return len(rows) == 4 and any(r[0]=='Alice' and r[1] is None for r in rows)

medium = Task("Your self‑join must show Alice with NULL manager, and 4 rows total.",
              verify_medium, Level.MEDIUM,
              hints=["Use LEFT JOIN so Alice is included."])

def verify_hard(cur, conn):
    cur.execute("SELECT e.name FROM staff e JOIN staff m ON e.manager_id = m.id WHERE m.name = 'Alice'")
    rows = cur.fetchall()
    return {r[0] for r in rows} == {'Bob', 'Charlie'}

hard = Task("Find employees whose manager is Alice (using self‑join with INNER JOIN).",
            verify_hard, Level.HARD,
            hints=["SELECT e.name FROM staff e JOIN staff m ON e.manager_id = m.id WHERE m.name = 'Alice';"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
