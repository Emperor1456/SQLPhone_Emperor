import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE students(name TEXT, score INTEGER)")
    cur.executemany("INSERT INTO students VALUES (?,?)", [('Alice',95),('Bob',82),('Charlie',70),('Dave',55)])
    return True

easy = Task("We've created 'students' with scores. Write a query that shows name, score, and a grade column: >=90 'A', >=80 'B', >=70 'C', else 'F' using a searched CASE.",
            verify_easy, Level.EASY,
            hints=["SELECT name, score, CASE WHEN score>=90 THEN 'A' WHEN score>=80 THEN 'B' WHEN score>=70 THEN 'C' ELSE 'F' END AS grade FROM students;"])

def verify_medium(cur, conn):
    cur.execute("SELECT name, score, CASE WHEN score>=90 THEN 'A' WHEN score>=80 THEN 'B' WHEN score>=70 THEN 'C' ELSE 'F' END FROM students")
    rows = cur.fetchall()
    grades = [r[2] for r in rows]
    return grades == ['A','B','C','F']

medium = Task("Grades should be: A, B, C, F in that order.",
              verify_medium, Level.MEDIUM,
              hints=["Check your CASE boundaries."])

def verify_hard(cur, conn):
    cur.execute("SELECT name, score, CASE WHEN score>=90 THEN 'A' WHEN score>=80 THEN 'B' WHEN score>=70 THEN 'C' ELSE 'F' END AS grade FROM students ORDER BY CASE grade WHEN 'A' THEN 1 WHEN 'B' THEN 2 WHEN 'C' THEN 3 ELSE 4 END")
    rows = cur.fetchall()
    return rows[0][2] == 'A'

hard = Task("Sort the results so that A comes first, then B, C, F (using CASE in ORDER BY).",
            verify_hard, Level.HARD,
            hints=["ORDER BY CASE grade WHEN 'A' THEN 1 WHEN 'B' THEN 2 WHEN 'C' THEN 3 ELSE 4 END"])


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
