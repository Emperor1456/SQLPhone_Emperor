import sys, sqlite3, csv, io
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE contacts(name TEXT, email TEXT)")
    cur.executemany("INSERT INTO contacts VALUES (?,?)", [('Alice','a@a.com'),('Bob','b@b.com')])
    return True

easy = Task("We have 'contacts'. Write a Python code snippet (using the 'csv' module) that selects all rows and prints them as CSV to the screen. (We'll capture the output).",
            verify_easy, Level.EASY,
            hints=["import csv, io, sys; output = io.StringIO(); writer = csv.writer(output); writer.writerow(['name','email']); writer.writerows(cur.execute('SELECT * FROM contacts').fetchall()); print(output.getvalue())"])

def verify_medium(cur, conn):
    # We'll execute the user's code and check if output contains commas and both rows
    code = input("Enter your CSV export code:\n> ")
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        exec(code, {"conn": conn, "cur": conn.cursor(), "csv": csv, "io": io})
    except Exception as e:
        sys.stdout = old_stdout
        print(f"❌ Error: {e}")
        return False
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    lines = output.strip().split('\n')
    if len(lines) >= 3 and ',' in output and 'Alice' in output:
        print(f"✅ CSV output:\n{output}")
        return True
    else:
        print(f"❌ CSV not formatted correctly. Got:\n{output}")
        return False

medium = Task("Run your code; it should print a CSV with header and two rows.",
              verify_medium, Level.MEDIUM,
              hints=["Make sure you include the header row and use csv.writer."])

def verify_hard(cur, conn):
    # Challenge: add an export to a file
    try:
        with open('test_export.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['name','email'])
            writer.writerows(cur.execute("SELECT * FROM contacts").fetchall())
        with open('test_export.csv', 'r') as f:
            content = f.read()
        import os
        os.unlink('test_export.csv')
        return 'Alice' in content and 'a@a.com' in content
    except Exception as e:
        print(f"❌ {e}")
        return False

hard = Task("Export the contacts to a file 'test_export.csv' on disk, then verify its contents (we'll check existence and data).",
            verify_hard, Level.HARD,
            hints=["Use open('test_export.csv', 'w', newline='') and csv.writer."])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
