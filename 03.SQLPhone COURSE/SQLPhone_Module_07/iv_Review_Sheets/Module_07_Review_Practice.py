import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

# ─── Easy: Date/time functions ──────────────────────
def verify_easy(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='events'")
    if not cur.fetchone(): return False
    cur.execute("SELECT COUNT(*) FROM events")
    if cur.fetchone()[0] < 3: return False
    # Must select events in the next 7 days (relative to 'now' we can't hardcode output)
    # Instead, verify that a query using date('now') runs and returns at least one row.
    cur.execute("SELECT * FROM events WHERE event_date BETWEEN date('now') AND date('now', '+7 days')")
    return len(cur.fetchall()) >= 1

easy = Task(
    description="Create table 'events' (id INTEGER PRIMARY KEY, name TEXT, event_date TEXT).\n"
                "Insert at least three events, one of which falls within the next 7 days.\n"
                "Write a query that shows all events happening between today and 7 days from now.",
    verify_func=verify_easy,
    level=Level.EASY,
    hints=[
        "CREATE TABLE events (id INTEGER PRIMARY KEY, name TEXT, event_date TEXT);",
        "INSERT INTO events VALUES (1,'Meeting', date('now','+2 days')), (2,'Workshop', date('now','+10 days')), (3,'Hackathon', date('now','+5 days'));",
        "SELECT * FROM events WHERE event_date BETWEEN date('now') AND date('now', '+7 days');"
    ]
)

# ─── Medium: strftime formatting ────────────────────
def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM events")
    if cur.fetchone()[0] < 2: return False
    cur.execute("SELECT strftime('%d/%m/%Y', event_date) FROM events LIMIT 1")
    row = cur.fetchone()
    return row is not None and '/' in row[0]

medium = Task(
    description="Using the 'events' table from Easy, write a query that shows each event's\n"
                "name and its date formatted as 'DD/MM/YYYY'. Use strftime.",
    verify_func=verify_medium,
    level=Level.MEDIUM,
    hints=[
        "SELECT name, strftime('%d/%m/%Y', event_date) FROM events;"
    ]
)

# ─── Hard: Aggregate by month, COALESCE, and CAST ───
def verify_hard(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sales'")
    if not cur.fetchone(): return False
    cur.execute("SELECT COUNT(*) FROM sales")
    if cur.fetchone()[0] < 4: return False
    expected = "2026-01 2 75.00\n2026-02 2 130.00"
    cur.execute("""
        SELECT strftime('%Y-%m', sale_date) AS month,
               COUNT(*),
               COALESCE(SUM(CAST(amount AS REAL)), 0)
        FROM sales
        GROUP BY month
        ORDER BY month
    """)
    rows = cur.fetchall()
    result = "\n".join(f"{r[0]} {r[1]} {r[2]:.2f}" for r in rows)
    return result == expected

hard = Task(
    description="Sales Summary Report:\n"
                "1. Create table 'sales' (id INTEGER PRIMARY KEY, product TEXT, amount TEXT, sale_date TEXT).\n"
                "   Insert at least 4 rows spanning two months, where amount is stored as TEXT.\n"
                "2. Write a query that shows, for each month (formatted as YYYY‑MM):\n"
                "   - The number of sales\n"
                "   - The total amount (use CAST to convert amount to REAL, and COALESCE to handle NULLs)\n"
                "   Sort by month.\n"
                "Exact output must be:\n"
                "2026-01 2 75.00\n"
                "2026-02 2 130.00",
    verify_func=verify_hard,
    level=Level.HARD,
    hints=[
        "CREATE TABLE sales (id INTEGER PRIMARY KEY, product TEXT, amount TEXT, sale_date TEXT);",
        "INSERT INTO sales VALUES (1,'A','25.00','2026-01-10'), (2,'B','50.00','2026-01-20'), (3,'C','80.00','2026-02-05'), (4,'A','50.00','2026-02-15');",
        "SELECT strftime('%Y-%m', sale_date) AS month, COUNT(*), COALESCE(SUM(CAST(amount AS REAL)),0) FROM sales GROUP BY month ORDER BY month;"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()
