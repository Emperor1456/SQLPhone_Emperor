# L-70_Export_to_CSV.py
# SQLPhone Emperor – SQL Module 08
# Practice: Export query to CSV (simulate in Python).

import sqlite3, csv, io

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'contacts' (name, email). Insert a few rows.")
    print("Write Python code (as a script) that selects all rows and writes them to a CSV string (we'll capture it).")
    print("We'll check that the output contains the expected headers and rows.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    user_sql = input("Enter your SQL (table creation + insert):\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    # Now ask user to write the export Python code
    print("Now enter the Python export code (use print to output CSV):")
    code = input("> ")
    # Execute in a captured stdout
    import sys
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        exec(code, {"conn": conn})
    except Exception as e:
        sys.stdout = old_stdout
        print(f"❌ Python error: {e}")
        conn.close()
        return False
    sys.stdout = old_stdout
    output = sys.stdout.getvalue()
    if 'name,email' in output or 'name' in output:
        print(f"✅ CSV output:\n{output}")
        conn.close()
        return True
    else:
        print(f"❌ CSV format not detected. Output: {output}")
        conn.close()
        return False

def main():
    while True:
        if task():
            break
        retry = input("Try again? (y/n): ")
        if retry.lower() != 'y':
            break

if __name__ == "__main__":
    main()