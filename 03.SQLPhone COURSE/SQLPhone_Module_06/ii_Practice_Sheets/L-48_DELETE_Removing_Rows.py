import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE logs(id INTEGER PRIMARY KEY, message TEXT, level TEXT)")
    cur.executemany("INSERT INTO logs VALUES (?,?,?)", [(1,'start','INFO'),(2,'warning','WARN'),(3,'error','ERROR'),(4,'debug','DEBUG')])
    return True

easy = Task("We have 'logs'. Delete all rows with level = 'DEBUG'. Then SELECT to confirm they're gone.",
            verify_easy, Level.EASY,
            hints=["DELETE FROM logs WHERE level = 'DEBUG'; SELECT * FROM logs;"])

def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM logs WHERE level='DEBUG'")
    if cur.fetchone()[0] > 0: return False
    cur.execute("SELECT COUNT(*) FROM logs")
    return cur.fetchone()[0] == 3

medium = Task("Only 3 rows should remain, none with DEBUG level.",
              verify_medium, Level.MEDIUM,
              hints=["Check your WHERE clause."])

def verify_hard(cur, conn):
    cur.execute("DELETE FROM logs WHERE level IN ('WARN','ERROR')")
    cur.execute("SELECT COUNT(*) FROM logs")
    return cur.fetchone()[0] == 1

hard = Task("Now delete all logs with level 'WARN' or 'ERROR'. Only INFO should remain.",
            verify_hard, Level.HARD,
            hints=["DELETE FROM logs WHERE level IN ('WARN','ERROR');"])


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
