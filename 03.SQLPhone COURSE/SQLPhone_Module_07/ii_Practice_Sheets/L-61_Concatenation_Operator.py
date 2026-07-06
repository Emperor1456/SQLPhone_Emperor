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
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
