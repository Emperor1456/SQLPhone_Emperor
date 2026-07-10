import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE inventory(id INTEGER PRIMARY KEY, item TEXT, quantity INTEGER)")
    cur.executemany("INSERT INTO inventory VALUES (?,?,?)", [(1,'widget',10),(2,'gadget',5),(3,'doohickey',20)])
    return True

easy = Task("We have 'inventory'. Update the quantity of 'widget' to 15. Then SELECT to verify.",
            verify_easy, Level.EASY,
            hints=["UPDATE inventory SET quantity = 15 WHERE item = 'widget'; SELECT * FROM inventory;"])

def verify_medium(cur, conn):
    cur.execute("SELECT quantity FROM inventory WHERE item='widget'")
    row = cur.fetchone()
    return row and row[0] == 15 and len(cur.execute("SELECT * FROM inventory").fetchall()) == 3

medium = Task("Ensure only widget's quantity changed, others unchanged.",
              verify_medium, Level.MEDIUM,
              hints=["Add a WHERE clause to target the row."])

def verify_hard(cur, conn):
    cur.execute("UPDATE inventory SET quantity = quantity + 1 WHERE quantity < 20")
    cur.execute("SELECT COUNT(*) FROM inventory WHERE quantity IN (6, 16)")
    return cur.fetchone()[0] == 2

hard = Task("Increase quantity by 1 for all items that currently have quantity < 20.",
            verify_hard, Level.HARD,
            hints=["UPDATE inventory SET quantity = quantity + 1 WHERE quantity < 20;"])


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
