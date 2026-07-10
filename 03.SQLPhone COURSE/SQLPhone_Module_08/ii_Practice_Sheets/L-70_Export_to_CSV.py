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
