import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE suppliers(id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("CREATE TABLE products(id INTEGER PRIMARY KEY, name TEXT, supplier_id INTEGER)")
    cur.executemany("INSERT INTO suppliers VALUES (?,?)", [(1,'S1'),(2,'S2')])
    cur.executemany("INSERT INTO products VALUES (?,?,?)", [(1,'P1',1),(2,'P2',1),(3,'P3',NULL)])
    return True

easy = Task("We have 'suppliers' and 'products'. Simulate a RIGHT JOIN to list all products and their supplier (even if supplier missing).",
            verify_easy, Level.EASY,
            hints=["Use a LEFT JOIN with swapped table order: SELECT p.name, s.name FROM products p LEFT JOIN suppliers s ON p.supplier_id = s.id;"])

def verify_medium(cur, conn):
    cur.execute("SELECT p.name, s.name FROM products p LEFT JOIN suppliers s ON p.supplier_id = s.id")
    rows = cur.fetchall()
    return len(rows) == 3 and rows[2][1] is None

medium = Task("The result must have 3 rows; product 'P3' should have NULL supplier.",
              verify_medium, Level.MEDIUM,
              hints=["SELECT p.name, s.name FROM products p LEFT JOIN suppliers s ON p.supplier_id = s.id;"])

def verify_hard(cur, conn):
    cur.execute("SELECT p.name FROM products p LEFT JOIN suppliers s ON p.supplier_id = s.id WHERE s.id IS NULL")
    return cur.fetchone() == ('P3',)

hard = Task("Using the simulation, find the product(s) with no supplier.",
            verify_hard, Level.HARD,
            hints=["Add WHERE s.id IS NULL to the LEFT JOIN."])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
