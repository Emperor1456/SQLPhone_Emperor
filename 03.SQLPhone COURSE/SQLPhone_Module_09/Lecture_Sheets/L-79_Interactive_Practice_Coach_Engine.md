# 📘 SQLPhone Emperor · SQL Module 09
# 📖 L‑79 – Interactive Practice Coach Engine

## 🎯 OBJECTIVE
Design the task engine that powers your practice
sheets – how to prompt, verify, and retry.

## 🧱 BRICK 1 – The task() Function Pattern
Each practice sheet follows this blueprint:
```python
def task():
    print("TASK: ...")
    user_input = input("> ")
    # Execute user input
    # Verify correctness
    if success:
        print("✅ Correct!")
        return True
    else:
        print("❌ Try again.")
        return False
```
The main loop calls `task()` and allows retries.

## 🧱 BRICK 2 – Verification Techniques
- Create a test database and pre‑insert data.
- Run the user’s SQL and compare results against expected.
- Use `try/except` to catch errors gracefully.
- Keep tasks small and focused on the lesson’s bricks.

## 💡 Real‑world Usage
- This engine is the core of SQLPhone Emperor.
- You will build it once in L‑79 and reuse it.

## 📌 Key Takeaway
A good practice engine gives immediate feedback.
The `task()` structure is simple but powerful.
Master it; you can create your own mini‑courses.

*Teaching yourself is the highest form of learning.*