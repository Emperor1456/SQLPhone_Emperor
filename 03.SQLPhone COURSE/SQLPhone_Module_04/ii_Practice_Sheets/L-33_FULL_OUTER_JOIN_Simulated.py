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
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
