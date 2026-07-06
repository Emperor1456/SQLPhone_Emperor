# 🚀 Getting Started — SQLPhone Emperor
**Phone‑first SQL with Termux, Acode & SQLite**  

Turn your Android phone into a full SQL development lab.  
No laptop required. All tools are free and open‑source.  
Start here to go from zero to your first query in under 10 minutes.

---

## 1. What You Need
- Android phone (Android 7+ recommended)
- **Termux** (from F‑Droid – see the Setup Guide)
- **Acode** editor (from Play Store)
- A brain, two hands, and the willingness to type every command yourself

## 2. Install Termux & SQLite
If you haven't already, follow the **Setup Guide** (`SETUP_GUIDE.md`) to install Termux and SQLite.  
Once done, verify the installation:
```bash
sqlite3 --version
```
You should see a version number (e.g., `3.43.0`).

## 3. The Interactive Practice Engine (New – Elite Coaching)
Every practice sheet in the course now contains a **smart coaching system**:
- **Three difficulty levels** – Easy, Medium, Hard. Choose the one that fits your skill.
- **Instant feedback** – type your SQL, hit Enter, and get a ✅ or ❌ immediately.
- **Progressive hints** – stuck? Type `:hint` to receive a clue (up to 3 hints per task).
- **Safe sandbox** – all practice runs on a temporary in‑memory database. Zero risk.
- **Offline & private** – the engine works entirely inside Termux; no internet, no server, no data leakage.

The engine file (`practice_engine.py`) lives in the `03.SQLPhone COURSE/` folder and is imported by every practice sheet automatically.

## 4. Create Your First Database (Termux + SQLite)
Open Termux and start SQLite:
```bash
sqlite3 my_first.db
```
You are now inside the SQLite shell (`sqlite>`). Create a simple table:
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
);
```
Insert a test row:
```sql
INSERT INTO users (name, age) VALUES ('Emperor', 18);
```
Query it:
```sql
SELECT * FROM users;
```
Exit the shell:
```
.quit
```
Congratulations – you just ran your first SQL commands on a phone.

## 5. Your First SQL File & Practice Session
- Open Acode, navigate to `~/SQLPhone_Emperor/` (or your course root).
- Create a new file `first.sql`, paste the same commands you just ran, save.
- Execute it from Termux:
  ```bash
  sqlite3 my_first.db < first.sql
  sqlite3 my_first.db "SELECT * FROM users;"
  ```

Now run your first **interactive practice coach**:
```bash
cd "03.SQLPhone COURSE/SQLPhone_Module_01"
python Practice_Sheets/L-01_What_is_SQL.py
```
- Choose level `1` (Easy).
- Type the SQL statements needed (they're described in the lecture sheet).
- The engine will verify your answer instantly.
- Use `:hint` if you need a clue, `:quit` to exit.

## 6. Daily Workflow
1. **Open the lecture sheet** (`.md`) in Acode. Read it thoroughly.
2. **Run the practice sheet** (`.py`) in Termux.
3. **Pick a level** – start with Easy, then Medium, then Hard as you improve.
4. **Type your SQL** – never copy‑paste. Muscles must learn.
5. **Use hints sparingly** – the struggle builds lasting memory.
6. **Mark the Progress Tracker** when the task is complete.
7. **Move to the next lesson** – two bricks at a time.

## 7. The Grand Finale: Imperial ERP Capstone
After completing all 12 modules, head to `05.Final Capstone/`.  
There you'll find the full project brief (`IMPERIAL_ERP_BRIEF.md`) and a starter Python script (`imperial_erp.py`).  
This capstone challenges you to build a complete inventory‑sales‑HR‑reporting system using everything you've learned.  
The starter script already integrates the practice engine, so you can build it task‑by‑task with hints and verification.

## 8. Your Diploma: Personalized Certificate
When you finish the entire course and capstone, generate your official **SQLPhone Emperor Certificate**:
```bash
python generate_certificate.py
```
Answer the prompts (name, date, certificate ID) and a `GRADUATION.md` file will be created with a Harvard‑style diploma. Open it in Acode's preview to see your name in gold. This is your proof of mastery — frame it, share it, or print it.

## 9. Connect Acode to Your SQLite Files
- In Acode, use the "Open Folder" option and select `~` (Termux home).
- You'll see all your `.db` databases and `.sql` files.
- Edit `.sql` files in Acode, then run them in Termux with:
  ```bash
  sqlite3 database_name.db < script.sql
  ```

## 10. Troubleshooting
- `sqlite3: command not found` → reinstall with `pkg install sqlite`.
- `Error: unable to open database file` → check folder permissions; run `termux-setup-storage` if needed.
- Practice engine says `No module named 'practice_engine'` → ensure `practice_engine.py` is placed inside `03.SQLPhone COURSE/`.
- Keyboard not appearing in Termux → tap the screen once on the terminal area.
- Script not running → make sure you're in the correct folder (use `cd` to navigate).

---

Your phone is now a fully‑equipped, enterprise‑grade database engineering lab.  
No server, no cloud, no excuses. Pure SQL, forged from your own two hands.

*Built on a phone. Built like a future CTO.*