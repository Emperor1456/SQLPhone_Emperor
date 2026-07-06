import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE students(id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("CREATE TABLE courses(id INTEGER PRIMARY KEY, title TEXT)")
    cur.execute("CREATE TABLE enrollments(student_id INTEGER, course_id INTEGER, grade TEXT)")
    cur.executemany("INSERT INTO students VALUES (?,?)", [(1,'S1'),(2,'S2'),(3,'S3')])
    cur.executemany("INSERT INTO courses VALUES (?,?)", [(1,'Math'),(2,'English'),(3,'Science')])
    cur.executemany("INSERT INTO enrollments VALUES (?,?,?)", [(1,1,'A'),(1,2,'B'),(2,1,'C')])
    return True

easy = Task("We have students, courses, enrollments. Write a query that lists all students and the courses they're enrolled in (include students with no enrollments).",
            verify_easy, Level.EASY,
            hints=["SELECT s.name, c.title FROM students s LEFT JOIN enrollments e ON s.id = e.student_id LEFT JOIN courses c ON e.course_id = c.id;"])

def verify_medium(cur, conn):
    cur.execute("SELECT s.name, c.title FROM students s LEFT JOIN enrollments e ON s.id = e.student_id LEFT JOIN courses c ON e.course_id = c.id")
    rows = cur.fetchall()
    return len(rows) >= 3 and any(r[1] is None for r in rows)

medium = Task("Your query should return at least 3 rows, with one student having NULL course.",
              verify_medium, Level.MEDIUM,
              hints=["Use two LEFT JOINs."])

def verify_hard(cur, conn):
    cur.execute("SELECT c.title FROM courses c LEFT JOIN enrollments e ON c.id = e.course_id WHERE e.student_id IS NULL")
    return cur.fetchall() is not None

hard = Task("Find courses that have no students enrolled (LEFT JOIN + IS NULL).",
            verify_hard, Level.HARD,
            hints=["SELECT c.title FROM courses c LEFT JOIN enrollments e ON c.id = e.course_id WHERE e.student_id IS NULL;"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
