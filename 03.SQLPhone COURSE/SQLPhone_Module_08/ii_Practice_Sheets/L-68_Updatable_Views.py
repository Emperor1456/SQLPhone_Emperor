import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE products(id INTEGER PRIMARY KEY, name TEXT, price REAL, stock INTEGER)")
    cur.executemany("INSERT INTO products VALUES (?,?,?,?)", [(1,'Widget',9.99,5),(2,'Gadget',19.99,0),(3,'Doohickey',4.99,15)])
    return True

easy = Task("We have 'products'. Create a view 'low_stock' showing products with stock < 10.",
            verify_easy, Level.EASY,
            hints=["CREATE VIEW low_stock AS SELECT id, name, stock FROM products WHERE stock < 10;"])

def verify_medium(cur, conn):
    cur.execute("UPDATE low_stock SET stock = stock + 20 WHERE name = 'Widget'")
    cur.execute("SELECT stock FROM products WHERE name='Widget'")
    return cur.fetchone()[0] == 25

medium = Task("Through the view, increase the stock of 'Widget' by 20. Verify the base table changed.",
              verify_medium, Level.MEDIUM,
              hints=["UPDATE low_stock SET stock = stock + 20 WHERE name = 'Widget'; SELECT * FROM products;"])

def verify_hard(cur, conn):
    try:
        cur.execute("INSERT INTO low_stock (name, price, stock) VALUES ('New',1.99,100)")
        return False
    except:
        return True

hard = Task("Try inserting into the view a product with stock >=10. It should fail because view filters stock<10, and insert can't enforce that directly. (Just try, we expect an error).",
            verify_hard, Level.HARD,
            hints=["INSERT INTO low_stock (name, price, stock) VALUES ('New',1.99,100); -- will likely fail or not appear in view"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
