# 🧠 Practice Engine Guide — SQLPhone Emperor

## What Is the Practice Engine?
A Python‑powered interactive coach embedded into every practice sheet.  
It transforms a static `.py` file into a smart, three‑level challenge system  
that runs entirely offline in Termux.

## Why It Makes SQLPhone Emperor Elite
- **Zero internet required** – works on a mountain, in a bunker, or in a basement.
- **Instant feedback** – no waiting for a grader; your SQL is executed and verified immediately.
- **Safe sandbox** – every attempt runs on a fresh in‑memory database; no risk to real data.
- **Adaptive difficulty** – you choose Easy, Medium, or Hard; match the challenge to your current skill.
- **Progressive hints** – up to 3 hints per task, from gentle nudge to near‑solution.
- **Deliberate practice** – you type every query, learn from errors, and build muscle memory.
- **Capstone‑ready** – the engine is already integrated into the Imperial ERP starter script; you can build the final project step‑by‑step with the same hint and verify system.

## How It Works
1. **You start a practice sheet** in Termux:
   ```bash
   python Practice_Sheets/L-01_What_is_SQL.py
   ```
2. **You pick a level** (1 = Easy, 2 = Medium, 3 = Hard).
3. **The engine shows the task description** and waits for your SQL input.
4. **You type your SQL statements** (multiple allowed, separated by `;`).
5. **The engine executes them** on a fresh in‑memory SQLite database.
6. **A verification function checks your result**:
   - Did the correct table get created?
   - Are the expected rows present?
   - Are the query results accurate?
7. **If correct** → `✅ Correct! (X attempts)` and the task ends.
8. **If wrong** → `❌ Try again.` You can retry or type `:hint` for a clue.

## Special Commands
- `:hint` – reveals the next available hint (up to 3 per task).
- `:quit` – exits the task without completing it.

## Difficulty Levels Explained
- **Easy** – mirror the exact pattern from the lecture sheet.  
  *Goal: build confidence and muscle memory.*
- **Medium** – apply the same concept with a twist (e.g., different column names, extra condition).  
  *Goal: demonstrate understanding, not just copying.*
- **Hard** – solve a novel problem that combines multiple concepts.  
  *Goal: prove mastery and prepare for real‑world engineering.*

## The Hints System
Each task has a list of hints ordered from general to specific.
- Hint 1: gentle nudge in the right direction.
- Hint 2: a more concrete clue (e.g., function name or syntax).
- Hint 3: near‑solution (still requires you to type it correctly).

Hints are revealed one at a time only when you explicitly request them with `:hint`.  
This prevents accidental spoilers and encourages genuine problem‑solving.

## The Verification Function
Every task has a custom `verify(cur, conn)` function written in Python.  
Examples of what it checks:
- Table existence via `sqlite_master`.
- Column count and names via `PRAGMA table_info`.
- Exact row values via `SELECT` and tuple comparison.
- Aggregate results (SUM, AVG, COUNT).
- Error handling (ensuring constraint violations are caught).

The verification logic is strict – your output must match the expected result precisely.

## Using the Engine for the Imperial ERP Capstone
The final capstone starter script (`05.Final Capstone/imperial_erp.py`) imports the practice engine.  
You can use it to build the ERP incrementally:
- Define a `Task` for each sub‑feature (e.g., “Add a category”, “Create a sales order”).
- Add hints for the SQL required.
- The engine will verify that your code successfully modifies the database.
- This turns a massive project into a series of guided, verifiable challenges.

## How to Use the Engine Effectively
1. **Start with Easy** when a concept is new.
2. **Move to Medium** once Easy feels comfortable.
3. **Attempt Hard** to solidify knowledge and prepare for capstone projects.
4. **Re‑run Hard tasks** from earlier modules as spaced repetition.
5. **Use hints only when truly stuck** – productive struggle builds long‑term memory.
6. **Retry after a wrong answer** – each attempt teaches something new.

## For Mentors & Self‑Learners
- The engine tracks **attempt count**; you can see how many tries each task took.
- Review tasks are already built into every module’s `Review_Sheets/` folder.
- Debugging challenges in `Debugging_Sheets/` teach you to fix broken queries.
- Self‑assessment rubrics in each `Progress_Tracker.md` ensure quality, not just correctness.
- The capstone can be completed with or without the engine – it’s your choice.

## Technical Details
- The engine file is `practice_engine.py` (lives in `03.SQLPhone COURSE/`).
- It defines three classes: `Level` (constants), `Task` (description + verify + hints + level), and the `run_task()` function.
- All practice sheets import it with:  
  `from practice_engine import Task, Level, run_task`
- The engine opens a fresh `:memory:` connection for every attempt, so no state leaks between tries.

## Summary
The practice engine turns SQLPhone Emperor from a static course into a **living, breathing mentor**.  
It’s patient, precise, and works anywhere your phone works.  
Use it daily, and you won’t just learn SQL – you’ll **become a database engineer**.

*The engine doesn’t teach you SQL. It makes you unbeatable at it.*