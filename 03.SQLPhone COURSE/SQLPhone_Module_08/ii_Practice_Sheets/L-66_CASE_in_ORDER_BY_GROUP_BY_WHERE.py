import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE tickets(id INTEGER PRIMARY KEY, severity TEXT, created_date TEXT)")
    cur.executemany("INSERT INTO tickets(severity, created_date) VALUES (?,?)", [('medium','2026-01-01'),('critical','2026-01-02'),('high','2026-01-03'),('low','2026-01-04')])
    return True

easy = Task("We have 'tickets'. Write a query that orders by severity: critical first, then high, then medium, then low using CASE in ORDER BY.",
            verify_easy, Level.EASY,
            hints=["SELECT * FROM tickets ORDER BY CASE severity WHEN 'critical' THEN 1 WHEN 'high' THEN 2 WHEN 'medium' THEN 3 ELSE 4 END;"])

def verify_medium(cur, conn):
    cur.execute("SELECT severity FROM tickets ORDER BY CASE severity WHEN 'critical' THEN 1 WHEN 'high' THEN 2 WHEN 'medium' THEN 3 ELSE 4 END")
    rows = [r[0] for r in cur.fetchall()]
    return rows == ['critical','high','medium','low']

medium = Task("The order must be: critical, high, medium, low.",
              verify_medium, Level.MEDIUM,
              hints=["Check the numeric mapping."])

def verify_hard(cur, conn):
    cur.execute("SELECT CASE WHEN severity IN ('critical','high') THEN 'urgent' ELSE 'normal' END AS urgency, COUNT(*) FROM tickets GROUP BY urgency")
    rows = cur.fetchall()
    return len(rows) == 2

hard = Task("Group by urgency (critical/high -> 'urgent', others -> 'normal') and count tickets per urgency.",
            verify_hard, Level.HARD,
            hints=["SELECT CASE WHEN severity IN ('critical','high') THEN 'urgent' ELSE 'normal' END, COUNT(*) FROM tickets GROUP BY 1;"])


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
