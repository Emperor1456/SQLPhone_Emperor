import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE A(id INTEGER, val TEXT)")
    cur.execute("CREATE TABLE B(id INTEGER, val TEXT)")
    cur.executemany("INSERT INTO A VALUES (?,?)", [(1,'a1'),(2,'a2')])
    cur.executemany("INSERT INTO B VALUES (?,?)", [(2,'b2'),(3,'b3')])
    return True

easy = Task("We have tables A and B with some matching and non-matching ids. Simulate a FULL OUTER JOIN using UNION of two LEFT JOINs.",
            verify_easy, Level.EASY,
            hints=["SELECT A.id, A.val, B.val FROM A LEFT JOIN B USING(id) UNION SELECT B.id, A.val, B.val FROM B LEFT JOIN A USING(id) WHERE A.id IS NULL;"])

def verify_medium(cur, conn):
    cur.execute("""
        SELECT id, A.val AS av, B.val AS bv FROM A LEFT JOIN B USING(id)
        UNION
        SELECT id, A.val, B.val FROM B LEFT JOIN A USING(id) WHERE A.id IS NULL
    """)
    rows = cur.fetchall()
    return len(rows) == 3

medium = Task("The result should have exactly 3 rows: id 1 (A only), id 2 (both), id 3 (B only).",
              verify_medium, Level.MEDIUM,
              hints=["Check that the UNION doesn't duplicate id 2."])

def verify_hard(cur, conn):
    cur.execute("""
        SELECT id, COALESCE(A.val, 'N/A') AS av, COALESCE(B.val, 'N/A') AS bv FROM A LEFT JOIN B USING(id)
        UNION
        SELECT id, A.val, B.val FROM B LEFT JOIN A USING(id) WHERE A.id IS NULL
    """)
    row = cur.fetchone()
    return row is not None

hard = Task("Use COALESCE to replace NULLs with 'N/A' in the simulated full outer join.",
            verify_hard, Level.HARD,
            hints=["COALESCE(column, 'N/A')"])


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
