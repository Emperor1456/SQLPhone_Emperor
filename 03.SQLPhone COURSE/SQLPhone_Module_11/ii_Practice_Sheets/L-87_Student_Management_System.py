import sys, sqlite3, os
sys.path.append("../..")
from practice_engine import Task, Level, run_task

DB = "student_mgmt.db"

def verify_easy(cur, conn):
    for tbl in ['Student','Course','Enrollment']:
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tbl}'")
        if not cur.fetchone():
            return False
    return True

easy = Task(
    "Build the Student Management System: create tables Student, Course, Enrollment with proper keys and constraints.",
    verify_easy, Level.EASY,
    hints=["CREATE TABLE Student(id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE, enrollment_year INTEGER);",
           "CREATE TABLE Course(id INTEGER PRIMARY KEY, title TEXT, credits INTEGER);",
           "CREATE TABLE Enrollment(student_id INTEGER, course_id INTEGER, grade TEXT, PRIMARY KEY(student_id, course_id), FOREIGN KEY(student_id) REFERENCES Student(id), FOREIGN KEY(course_id) REFERENCES Course(id));"]
)

def verify_medium(cur, conn):
    for tbl in ['Student','Course','Enrollment']:
        cur.execute(f"SELECT COUNT(*) FROM {tbl}")
        if cur.fetchone()[0] < 3:
            return False
    cur.execute("SELECT s.name, c.title FROM Enrollment e JOIN Student s ON e.student_id=s.id JOIN Course c ON e.course_id=c.id LIMIT 1")
    return cur.fetchone() is not None

medium = Task(
    "Insert at least 3 rows per table and write a query that shows each enrollment with student name and course title.",
    verify_medium, Level.MEDIUM,
    hints=["INSERT INTO Student VALUES (1,'Alice','a@a.com',2025), (2,'Bob','b@b.com',2025), (3,'Charlie','c@c.com',2026);",
           "INSERT INTO Course VALUES (1,'Math',3), (2,'Science',4), (3,'History',3);",
           "INSERT INTO Enrollment VALUES (1,1,'A'), (2,1,'B'), (3,2,'A');",
           "SELECT s.name, c.title FROM Enrollment e JOIN Student s ON e.student_id=s.id JOIN Course c ON e.course_id=c.id;"]
)

def verify_hard(cur, conn):
    cur.execute("SELECT c.title, AVG(CASE WHEN e.grade='A' THEN 4 WHEN e.grade='B' THEN 3 WHEN e.grade='C' THEN 2 ELSE 1 END) as gpa FROM Course c JOIN Enrollment e ON c.id=e.course_id GROUP BY c.id HAVING COUNT(e.student_id) > 1")
    return len(cur.fetchall()) > 0

hard = Task(
    "Calculate average GPA per course (A=4,B=3,C=2,...) for courses with at least 2 students enrolled.",
    verify_hard, Level.HARD,
    hints=["Use CASE inside AVG, GROUP BY, HAVING COUNT(*) >= 2"]
)

def main():
    if os.path.exists(DB): os.remove(DB)
    print("1 Easy  2 Medium  3 Hard")
    c = input("> ")
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))
if __name__ == "__main__": main()
