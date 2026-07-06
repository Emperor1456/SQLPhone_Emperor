# practice_engine.py — Hints & Levels Engine for SQLPhone Emperor

import sqlite3

class Level:
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"

class Task:
    def __init__(self, description, verify_func, level=Level.EASY, hints=None):
        self.description = description
        self.verify = verify_func
        self.level = level
        self.hints = hints or []
        self.hint_index = 0

    def next_hint(self):
        if self.hint_index < len(self.hints):
            hint = self.hints[self.hint_index]
            self.hint_index += 1
            return hint
        return None

def run_task(task):
    print("=" * 50)
    print(f"🧱 TASK [{task.level.upper()}]")
    print(task.description)
    print("=" * 50)
    attempts = 0
    while True:
        attempts += 1
        user_input = input("Enter your SQL (or :hint, :quit):\n> ")
        if user_input.strip().lower() == ":hint":
            hint = task.next_hint()
            if hint:
                print(f"💡 HINT: {hint}")
            else:
                print("No more hints.")
            continue
        if user_input.strip().lower() == ":quit":
            print("Exiting task.")
            return False
        # Execute and verify
        conn = sqlite3.connect(":memory:")
        cur = conn.cursor()
        try:
            cur.executescript(user_input)
            conn.commit()
        except Exception as e:
            print(f"❌ Error: {e}")
            conn.close()
            continue
        try:
            result = task.verify(cur, conn)
            conn.close()
            if result:
                print(f"✅ Correct! ({attempts} attempts)")
                return True
            else:
                print("❌ Not quite. Try again or type :hint for help.")
        except Exception as e:
            print(f"❌ Verification error: {e}")
            conn.close()

def main():
    print("Practice engine loaded. Use `run_task(task)` to start.")

if __name__ == "__main__":
    main()
