# L-79_Interactive_Practice_Coach_Engine.py
# SQLPhone Emperor – SQL Module 09
# Practice: Understand the practice engine pattern.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: This practice sheet itself demonstrates the engine.")
    print("You are using it now! Study the `task()` function and the `main()` loop in this file.")
    print("We will ask you to write a simple `task()` that creates a table and returns True if the table exists.")
    print("=" * 50)
    # We'll just check if user can write a valid task function.
    user_code = input("Write a function `my_task(conn)` that creates a table 'checkpoint' and returns True if it exists:\n>>> ")
    try:
        exec(user_code)
    except Exception as e:
        print(f"❌ Error defining function: {e}")
        return False
    conn = sqlite3.connect(":memory:")
    try:
        result = my_task(conn)
    except NameError:
        print("❌ Function my_task not defined.")
        conn.close()
        return False
    if result:
        print("✅ Your task function works!")
        conn.close()
        return True
    else:
        print("❌ Function returned False. Did you create the table?")
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