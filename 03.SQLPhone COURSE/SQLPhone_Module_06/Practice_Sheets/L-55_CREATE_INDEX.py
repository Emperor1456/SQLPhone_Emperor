import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE contacts(id INTEGER PRIMARY KEY, name TEXT, phone TEXT)")
    cur.executemany("INSERT INTO contacts (name, phone) VALUES (?,?)", [('Alice','123'),('Bob','456'),('Charlie','789'),('Dave','000')])
    return True

easy = Task("We have 'contacts'. Create an index on the 'name' column.",
            verify_easy, Level.EASY,
            hints=["CREATE INDEX idx_contacts_name ON contacts(name);"])

def verify_medium(cur, conn):
    cur.execute("CREATE INDEX idx_contacts_name ON contacts(name)")
    cur.execute("EXPLAIN QUERY PLAN SELECT * FROM contacts WHERE name = 'Alice'")
    plan = str(cur.fetchall())
    return 'USING INDEX' in plan

medium = Task("Create the index, then use EXPLAIN QUERY PLAN to show it's used.",
              verify_medium, Level.MEDIUM,
              hints=["EXPLAIN QUERY PLAN SELECT * FROM contacts WHERE name = 'Alice';"])

def verify_hard(cur, conn):
    cur.execute("DROP INDEX IF EXISTS idx_contacts_name")
    cur.execute("EXPLAIN QUERY PLAN SELECT * FROM contacts WHERE name = 'Alice'")
    plan = str(cur.fetchall())
    return 'SCAN TABLE' in plan

hard = Task("Drop the index and verify the query plan now shows a full table scan.",
            verify_hard, Level.HARD,
            hints=["DROP INDEX idx_contacts_name; EXPLAIN QUERY PLAN ..."])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
