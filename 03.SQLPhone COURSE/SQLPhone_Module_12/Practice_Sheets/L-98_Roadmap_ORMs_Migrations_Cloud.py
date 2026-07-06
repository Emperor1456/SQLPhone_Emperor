# L-98_Roadmap_ORMs_Migrations_Cloud.py
# SQLPhone Emperor – SQL Module 12
# Practice: Reflect on your journey and plan next steps.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Write a brief Python script that prints a summary of what you’ve learned")
    print("and outlines your next steps (ORM, frontend, cloud).")
    print("We’ll simply run your script and confirm it prints something meaningful.")
    print("=" * 50)
    code = input("Enter your Python script:\n> ")
    try:
        exec(code)
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    print("✅ Your roadmap printed. The journey continues!")
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