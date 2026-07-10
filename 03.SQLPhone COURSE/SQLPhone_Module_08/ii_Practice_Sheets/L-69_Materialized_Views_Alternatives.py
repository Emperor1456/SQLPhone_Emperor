import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, product TEXT, amount REAL)")
    cur.executemany("INSERT INTO orders VALUES (?,?,?)", [(1,'A',100),(2,'A',200),(3,'B',150)])
    return True

easy = Task("We have 'orders'. Simulate a materialized view by creating a summary table 'order_summary' with product and total_amount, and populate it with a SELECT.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE order_summary AS SELECT product, SUM(amount) AS total FROM orders GROUP BY product;"])

def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM order_summary")
    return cur.fetchone()[0] == 2

medium = Task("The summary should have 2 rows (A:300, B:150).",
              verify_medium, Level.MEDIUM,
              hints=["Check that you used SUM and GROUP BY."])

def verify_hard(cur, conn):
    # Refresh the summary manually: delete and re-insert
    cur.execute("DELETE FROM order_summary")
    cur.execute("INSERT INTO order_summary SELECT product, SUM(amount) FROM orders GROUP BY product")
    cur.execute("SELECT total FROM order_summary WHERE product='A'")
    return cur.fetchone()[0] == 300

hard = Task("Refresh the summary by deleting all rows and re-populating from the base table.",
            verify_hard, Level.HARD,
            hints=["DELETE FROM order_summary; INSERT INTO order_summary SELECT product, SUM(amount) FROM orders GROUP BY product;"])


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
