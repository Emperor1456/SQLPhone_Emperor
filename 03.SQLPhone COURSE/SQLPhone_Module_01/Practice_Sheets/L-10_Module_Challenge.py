import sys, sqlite3, os
sys.path.append("../..")
from practice_engine import Task, Level, run_task

DB = "imperial_fitness.db"

# Easy: create all 4 tables
def verify_easy(cur, conn):
    tables = ['Member','Trainer','Class','Enrollment']
    for t in tables:
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{t}'")
        if not cur.fetchone():
            return False
    return True

easy = Task("Create all four tables (Member, Trainer, Class, Enrollment) with correct columns and primary keys.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE Member (member_id INTEGER PRIMARY KEY, ...);",
                   "Remember foreign keys: Class.trainer_id -> Trainer, Enrollment.member_id -> Member, Enrollment.class_id -> Class."])

# Medium: insert 3 rows each + a simple join
def verify_medium(cur, conn):
    for t in ['Member','Trainer','Class','Enrollment']:
        cur.execute(f"SELECT COUNT(*) FROM {t}")
        if cur.fetchone()[0] < 3:
            return False
    # check a join query works
    cur.execute("SELECT m.first_name, c.class_name FROM Enrollment e JOIN Member m ON e.member_id=m.member_id JOIN Class c ON e.class_id=c.class_id LIMIT 1")
    return cur.fetchone() is not None

medium = Task("Insert at least 3 rows into each table. Then write a query showing each enrollment with the member's first name and class name.",
              verify_medium, Level.MEDIUM,
              hints=["INSERT INTO Member VALUES (1,'Emperor','SQLPhone','emperor@sqlphone.dev',datetime('now'),'Elite');",
                     "SELECT m.first_name, c.class_name FROM Enrollment e JOIN Member m ON e.member_id=m.member_id JOIN Class c ON e.class_id=c.class_id;"])

# Hard: business query with full names and schedule
def verify_hard(cur, conn):
    cur.execute("""
        SELECT m.first_name || ' ' || m.last_name AS MemberName,
               c.class_name,
               t.first_name || ' ' || t.last_name AS TrainerName,
               e.enrollment_date,
               c.schedule_time
        FROM Enrollment e
        JOIN Member m ON e.member_id = m.member_id
        JOIN Class c ON e.class_id = c.class_id
        JOIN Trainer t ON c.trainer_id = t.trainer_id
        LIMIT 1
    """)
    row = cur.fetchone()
    return row is not None and len(row) == 5

hard = Task("Write the full business query: show Member Name, Class Name, Trainer Name, Enrollment Date, Schedule.",
            verify_hard, Level.HARD,
            hints=["Use || to concatenate first and last names.",
                   "JOIN Enrollment to Member, Class, and Trainer.",
                   "Alias columns clearly."])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
