# L-85_Backup_and_Restore.py
# SQLPhone Emperor – SQL Module 10
# Practice: Perform a backup using .backup or .dump.

import sqlite3, os, subprocess

def task():
    print("=" * 50)
    print("🧱 TASK: Create a database 'source.db' with a table and row.")
    print("Then write Python code or CLI commands to back it up to 'backup.db'.")
    print("We'll check that 'backup.db' contains the same data.")
    print("=" * 50)
    # Create source db
    src = sqlite3.connect("source.db")
    src.execute("CREATE TABLE data (info TEXT)")
    src.execute("INSERT INTO data VALUES ('Emperor')")
    src.commit()
    src.close()
    user_code = input("Enter your Python backup code (or CLI command preceded by '!'):\n> ")
    if user_code.startswith('!'):
        # Shell command
        cmd = user_code[1:].strip()
        os.system(cmd)
    else:
        try:
            exec(user_code)
        except Exception as e:
            print(f"❌ Error: {e}")
            os.unlink("source.db")
            return False
    # Verify
    if os.path.exists("backup.db"):
        dst = sqlite3.connect("backup.db")
        cur = dst.cursor()
        try:
            cur.execute("SELECT info FROM data")
            row = cur.fetchone()
            if row and row[0] == 'Emperor':
                print("✅ Backup verified.")
                dst.close()
                os.unlink("source.db")
                os.unlink("backup.db")
                return True
            else:
                print("❌ Data not found in backup.")
                dst.close()
                os.unlink("source.db")
                os.unlink("backup.db")
                return False
        except Exception as e:
            print(f"❌ Backup file exists but table missing: {e}")
            dst.close()
            os.unlink("source.db")
            if os.path.exists("backup.db"): os.unlink("backup.db")
            return False
    else:
        print("❌ backup.db not created.")
        os.unlink("source.db")
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