import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE measurements(sensor TEXT, reading TEXT)")
    cur.executemany("INSERT INTO measurements VALUES (?,?)", [('A','42.5'),('B','58.2'),('C','37.0')])
    return True

easy = Task("We have 'measurements' with text readings. Write a query that casts reading to REAL and computes the average.",
            verify_easy, Level.EASY,
            hints=["SELECT AVG(CAST(reading AS REAL)) FROM measurements;"])

def verify_medium(cur, conn):
    cur.execute("SELECT AVG(CAST(reading AS REAL)) FROM measurements")
    avg = cur.fetchone()[0]
    return round(avg, 1) == 45.9

medium = Task("Average should be approximately 45.9.",
              verify_medium, Level.MEDIUM,
              hints=["Use CAST(reading AS REAL)."])

def verify_hard(cur, conn):
    cur.execute("SELECT sensor, CAST(reading AS REAL) * 2 AS doubled FROM measurements")
    rows = cur.fetchall()
    return len(rows) == 3 and rows[0][1] == 85.0

hard = Task("Show the sensor and double the reading value (as a number).",
            verify_hard, Level.HARD,
            hints=["SELECT sensor, CAST(reading AS REAL) * 2 FROM measurements;"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
