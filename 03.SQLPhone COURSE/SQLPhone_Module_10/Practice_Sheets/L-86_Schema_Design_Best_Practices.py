import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    # User must create a schema with proper naming and constraints
    # We'll check if tables are singular and snake_case, and at least one constraint exists.
    user_sql = input("Enter your DDL (create tables):\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ {e}")
        return False
    # Check table names
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in cur.fetchall()]
    for t in tables:
        if t[-1] == 's' or ' ' in t or '-' in t:
            print(f"⚠️ Table '{t}' may violate singular/snake_case convention.")
    # Check for constraints
    has_constraint = False
    for t in tables:
        cur.execute(f"SELECT sql FROM sqlite_master WHERE name='{t}'")
        ddl = cur.fetchone()[0]
        if 'CHECK' in ddl or 'UNIQUE' in ddl or 'FOREIGN KEY' in ddl:
            has_constraint = True
            break
    if has_constraint:
        print("✅ Schema includes constraints. Good!")
        return True
    else:
        print("❌ Add at least one CHECK, UNIQUE, or FOREIGN KEY constraint.")
        return False

easy = Task(
    "Design a schema for a 'school' database with students, courses, enrollments. Use proper naming (snake_case, singular), primary keys, and at least one constraint.",
    verify_easy, Level.EASY,
    hints=["CREATE TABLE student(id INTEGER PRIMARY KEY, name TEXT NOT NULL); CREATE TABLE course(id INTEGER PRIMARY KEY, title TEXT); CREATE TABLE enrollment(student_id INTEGER, course_id INTEGER, grade TEXT, PRIMARY KEY(student_id, course_id), FOREIGN KEY(student_id) REFERENCES student(id), FOREIGN KEY(course_id) REFERENCES course(id));"]
)

def verify_medium(cur, conn):
    # Insert sample data and test referential integrity
    cur.execute("INSERT INTO student VALUES (1,'Alice'), (2,'Bob')")
    cur.execute("INSERT INTO course VALUES (1,'Math')")
    try:
        cur.execute("INSERT INTO enrollment VALUES (1,1,'A')")
        return True
    except:
        return False

medium = Task(
    "Insert sample data that respects foreign keys.",
    verify_medium, Level.MEDIUM,
    hints=["First insert into parent tables, then child tables."]
)

def verify_hard(cur, conn):
    try:
        cur.execute("INSERT INTO enrollment VALUES (3,1,'B')")
        return False
    except sqlite3.IntegrityError:
        return True

hard = Task(
    "Try inserting an enrollment for a non‑existent student (should fail).",
    verify_hard, Level.HARD,
    hints=["INSERT INTO enrollment VALUES (3,1,'B'); -- student 3 doesn't exist"]
)

def main():
    print("1 Easy  2 Medium  3 Hard")
    c = input("> ")
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))
if __name__ == "__main__": main()
