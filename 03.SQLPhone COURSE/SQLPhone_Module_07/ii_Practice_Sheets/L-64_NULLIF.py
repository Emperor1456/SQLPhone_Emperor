import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE stats(item TEXT, total_sales REAL, quantity INTEGER)")
    cur.executemany("INSERT INTO stats VALUES (?,?,?)", [('A',100,5),('B',200,0),('C',150,3)])
    return True

easy = Task("We have 'stats'. Write a query that calculates average sale per item (total_sales / quantity), but returns NULL if quantity is 0 using NULLIF.",
            verify_easy, Level.EASY,
            hints=["SELECT item, total_sales / NULLIF(quantity, 0) AS avg_sale FROM stats;"])

def verify_medium(cur, conn):
    cur.execute("SELECT item, total_sales / NULLIF(quantity, 0) FROM stats")
    rows = cur.fetchall()
    return rows[1][1] is None

medium = Task("The row with quantity 0 should show NULL for the average.",
              verify_medium, Level.MEDIUM,
              hints=["Use NULLIF(quantity, 0)."])

def verify_hard(cur, conn):
    cur.execute("SELECT item, COALESCE(total_sales / NULLIF(quantity, 0), 0) AS avg_sale FROM stats")
    rows = cur.fetchall()
    return rows[1][1] == 0

hard = Task("Replace the NULL with 0 using COALESCE for a cleaner output.",
            verify_hard, Level.HARD,
            hints=["COALESCE(total_sales / NULLIF(quantity, 0), 0)"])


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
