import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("CREATE TABLE categories(id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("CREATE TABLE items(id INTEGER PRIMARY KEY, name TEXT, cat_id INTEGER, FOREIGN KEY(cat_id) REFERENCES categories(id) ON DELETE CASCADE)")
    return True

easy = Task("Create 'categories' and 'items' with ON DELETE CASCADE foreign key.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE categories(id INTEGER PRIMARY KEY, name TEXT);",
                   "CREATE TABLE items(id INTEGER PRIMARY KEY, name TEXT, cat_id INTEGER, FOREIGN KEY(cat_id) REFERENCES categories(id) ON DELETE CASCADE);"])

def verify_medium(cur, conn):
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("INSERT INTO categories VALUES (1,'C1')")
    cur.execute("INSERT INTO items VALUES (1,'I1',1)")
    cur.execute("DELETE FROM categories WHERE id=1")
    cur.execute("SELECT COUNT(*) FROM items")
    return cur.fetchone()[0] == 0

medium = Task("Insert a category and an item, then delete the category. Item should be cascade-deleted.",
              verify_medium, Level.MEDIUM,
              hints=["INSERT INTO categories VALUES (1,'C1'); INSERT INTO items VALUES (1,'I1',1); DELETE FROM categories WHERE id=1; SELECT * FROM items; -- should be empty"])

def verify_hard(cur, conn):
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("INSERT INTO categories VALUES (2,'C2')")
    cur.execute("INSERT INTO items VALUES (2,'I2',2)")
    try:
        cur.execute("DELETE FROM categories WHERE id=2")
        cur.execute("SELECT COUNT(*) FROM items")
        return cur.fetchone()[0] == 0
    except:
        return False

hard = Task("Test CASCADE again: insert a different category/item, delete category, verify item gone.",
            verify_hard, Level.HARD,
            hints=["Repeat the pattern: INSERT, then DELETE, then check."])


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
