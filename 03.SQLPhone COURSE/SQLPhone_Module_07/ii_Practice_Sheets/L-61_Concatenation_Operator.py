import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE contacts(first_name TEXT, last_name TEXT, title TEXT)")
    cur.executemany("INSERT INTO contacts VALUES (?,?,?)", [('John','Doe','Mr.'),('Jane','Smith',NULL)])
    return True

easy = Task("We have 'contacts'. Write a query that concatenates title, first_name, last_name into 'Title First Last'. Handle NULL title with COALESCE.",
            verify_easy, Level.EASY,
            hints=["SELECT COALESCE(title || ' ', '') || first_name || ' ' || last_name FROM contacts;"])

def verify_medium(cur, conn):
    cur.execute("SELECT COALESCE(title || ' ', '') || first_name || ' ' || last_name FROM contacts")
    rows = cur.fetchall()
    return rows[0][0] == 'Mr. John Doe' and rows[1][0] == 'Jane Smith'

medium = Task("First row should be 'Mr. John Doe', second 'Jane Smith' (no NULL appearing).",
              verify_medium, Level.MEDIUM,
              hints=["Use COALESCE to avoid NULL concatenation."])

def verify_hard(cur, conn):
    cur.execute("SELECT first_name || ' ' || last_name AS full_name, LENGTH(first_name || ' ' || last_name) AS len FROM contacts ORDER BY len DESC")
    rows = cur.fetchall()
    return rows[0][1] >= rows[1][1]

hard = Task("Create a full_name column and sort by its length descending.",
            verify_hard, Level.HARD,
            hints=["SELECT first_name || ' ' || last_name AS full_name, LENGTH(first_name || ' ' || last_name) AS len FROM contacts ORDER BY len DESC;"])


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
