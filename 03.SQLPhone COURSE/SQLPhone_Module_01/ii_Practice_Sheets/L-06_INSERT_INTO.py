import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM cities")
    return cur.fetchone()[0] == 3

easy = Task("Create table 'cities' (id INT PK, name TEXT NOT NULL, country TEXT, population INT). Insert 3 rows in one statement.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE cities (id INTEGER PRIMARY KEY, name TEXT NOT NULL, country TEXT, population INTEGER);",
                   "INSERT INTO cities (name, country, population) VALUES ('Tokyo','Japan',13929286), ('Delhi','India',16787941), ('Shanghai','China',24183300);"])

def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM cities")
    return cur.fetchone()[0] == 4

medium = Task("Add one more city, this time specifying only name and country (let population be NULL). Then SELECT all.",
              verify_medium, Level.MEDIUM,
              hints=["INSERT INTO cities (name, country) VALUES ('London','UK');","SELECT * FROM cities;"])

def verify_hard(cur, conn):
    # after inserting a row, use RETURNING to get the id
    cur.execute("SELECT COUNT(*) FROM cities")
    return cur.fetchone()[0] >= 5

hard = Task("Insert a fifth city using a VALUES clause and use RETURNING id to see the generated ID.",
            verify_hard, Level.HARD,
            hints=["INSERT INTO cities (name, country, population) VALUES ('Paris','France',2161000) RETURNING id;"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
