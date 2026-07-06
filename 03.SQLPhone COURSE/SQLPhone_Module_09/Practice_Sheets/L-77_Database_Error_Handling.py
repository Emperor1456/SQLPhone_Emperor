# L-77_Database_Error_Handling.py
# SQLPhone Emperor – SQL Module 09
# Practice: Error handling with try/except.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Table 'users' has UNIQUE email. Try inserting a duplicate email and catch the error.")
    print("We'll create the table. Write Python code that handles sqlite3.IntegrityError gracefully.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT UNIQUE)")
    conn.execute("INSERT INTO users (email) VALUES ('test@example.com')")
    conn.commit()
    user_code = input(">>> ")
    try:
        exec(user_code, {"conn": conn})
    except Exception as e:
        print(f"❌ Your code raised an unhandled exception: {e}")
        conn.close()
        return False
    # If no exception propagated, it means they handled it.
    print("✅ No unhandled exception – you caught the error correctly.")
    conn.close()
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