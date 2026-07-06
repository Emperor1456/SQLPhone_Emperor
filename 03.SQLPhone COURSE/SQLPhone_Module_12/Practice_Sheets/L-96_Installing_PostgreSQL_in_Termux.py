# L-96_Installing_PostgreSQL_in_Termux.py
# SQLPhone Emperor – SQL Module 12
# Practice: Install PostgreSQL (if you can) and report.

import subprocess, sys

def task():
    print("=" * 50)
    print("🧱 TASK: This practice is informational.")
    print("If you have installed PostgreSQL via proot-distro, run a quick query in psql and capture the output.")
    print("Otherwise, write a Python script that prints the version of SQLite you're using as a placeholder.")
    print("We'll check that your script runs and prints something.")
    print("=" * 50)
    code = input("Enter your Python code (can just print sqlite3.sqlite_version):\n> ")
    try:
        exec(code)
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    # We can't verify version because output depends on execution; we just trust they printed something.
    print("✅ Script ran. If it showed a version, you're good.")
    return True

def main():
    while True:
        if task():
            break
        retry = input("Try again? (y/n): ")
        if retry.lower() != 'y':
            break

if __name__ == "__main__":
    main()