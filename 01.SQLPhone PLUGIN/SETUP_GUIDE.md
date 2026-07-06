# ⚙️ SQLPhone Emperor — Setup Guide
**Termux + SQLite + Acode + Interactive Engine**

A battle‑hardened phone lab for database mastery.  
Every tool here was chosen to work offline, on a 6‑inch screen,  
without compromising professional standards.

---

## 1. Install Termux
- Download from F‑Droid (the Play Store version is outdated):  
  [https://f-droid.org/repo/com.termux_118.apk](https://f-droid.org/repo/com.termux_118.apk)
- Open Termux. Wait for the bootstrap to finish.
- Grant storage permission when Termux asks:
  ```bash
  termux-setup-storage
  ```
- Update packages:
  ```bash
  pkg update && pkg upgrade -y
  ```

## 2. Install SQLite
```bash
pkg install sqlite -y
```
Confirm the installation:
```bash
sqlite3 --version
```
Expected output: `3.43.0` or higher.

## 3. Install Acode
- Install Acode from the Play Store (developer: Foxdebug).
- Open Acode once and allow file access when prompted.

## 4. Course Folder Setup
Create the main course directory:
```bash
mkdir -p ~/SQLPhone_Emperor
```
If you have cloned the repository, the folder already exists.  
The full course structure lives under `03.SQLPhone COURSE/`.

## 5. Verify Python + sqlite3
Python ships with the `sqlite3` module built in. Verify it:
```bash
python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
```
This must print the same version as `sqlite3 --version`.

## 6. Install the Interactive Practice Engine
The engine is a single Python file: `practice_engine.py`.  
It must be placed inside the course folder so all practice sheets can import it:
```bash
# If you cloned the repo, it is already there.
# Otherwise, create it from the provided content in the documentation.
```
Verify the engine is in place:
```bash
ls "03.SQLPhone COURSE/practice_engine.py"
```
All practice sheets import it with `from practice_engine import Task, Level, run_task`.

## 7. Quick Sanity Check
Create a test database and run a practice sheet to confirm everything works.

### Test SQLite directly
```bash
cd ~/SQLPhone_Emperor
sqlite3 test.db
```
Inside the prompt:
```sql
CREATE TABLE alive (status TEXT);
INSERT INTO alive VALUES ('Emperor is ready');
SELECT * FROM alive;
.quit
```
If you see the row, your SQLite lab is battle‑ready.

### Test the Practice Engine
```bash
cd "03.SQLPhone COURSE/SQLPhone_Module_01"
python Practice_Sheets/L-01_What_is_SQL.py
```
- Choose `1` (Easy).
- Type the required SQL (see the lecture sheet).
- You should see `✅ Correct! (1 attempts)`.
- Type `:hint` at any time to see clues.

## 8. Daily Workflow
1. Open the lecture sheet (`.md`) in Acode.
2. Run the practice sheet (`.py`) in Termux.
3. Choose a difficulty level and type your SQL.
4. Use `:hint` if stuck; `:quit` to exit.
5. Mark the Progress Tracker when done.
6. Repeat for the next lesson.

## 9. Troubleshooting
- `sqlite3: command not found` → reinstall with `pkg install sqlite`.
- `Error: unable to open database file` → check directory permissions; run `termux-setup-storage`.
- `ModuleNotFoundError: No module named 'practice_engine'` → ensure `practice_engine.py` is inside `03.SQLPhone COURSE/`.
- Keyboard not appearing → tap the Termux screen once.
- Acode cannot see Termux files → grant storage permissions and open the `~` folder in Acode.

---

Your phone is now a fully‑equipped database engineering lab.  
No server, no cloud, no excuses — just pure SQL forged from your own two hands.

*Built on a phone. Built like a future CTO.*