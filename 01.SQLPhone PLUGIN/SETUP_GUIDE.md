# ⚙️ SQLPhone Emperor — Setup Guide
**Termux + SQLite + Acode**

A battle‑hardened phone lab for database mastery.  
Every tool here was chosen to work offline, on a 6‑inch screen,  
without compromising professional standards.

---

## 1. Install Termux
- Download from F‑Droid (the Play Store version is outdated):
  [https://f-droid.org/repo/com.termux_118.apk](https://f-droid.org/repo/com.termux_118.apk)
- Open Termux. Wait for bootstrap.
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
Confirm:
```bash
sqlite3 --version
```
Expected output: `3.43.0` or higher.

## 3. Install Acode
- From Play Store: search “Acode” by Foxdebug.
- Open it once, allow file access.

## 4. Course Folder Setup
In Termux:
```bash
mkdir -p ~/PyPhone_Emperor/03.PyPhone\ COURSE/PyPhone_SQL/
```
(If you cloned the `SQLPhone_Emperor` repo, your path may differ — adapt accordingly.)

## 5. Verify Python + sqlite3
```bash
python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
```
This must print the same version as `sqlite3 --version`.
Python ships with sqlite3 built in — no extra install needed.

## 6. Quick Sanity Check
Create a test database:
```bash
cd ~/PyPhone_Emperor/03.PyPhone\ COURSE/PyPhone_SQL/
sqlite3 test.db
```
Inside the prompt:
```sql
CREATE TABLE alive (status TEXT);
INSERT INTO alive VALUES ('Emperor is ready');
SELECT * FROM alive;
.quit
```
If you see the row, your lab is battle‑ready.

## 7. Daily Workflow
1. Open lecture sheet (`.md`) in Acode.
2. Write your `.sql` practice file in Acode.
3. Run it in Termux with:
   ```bash
   sqlite3 <database.db> < script.sql
   ```
4. For interactive exploration, type `sqlite3 <database.db>` and query live.
5. After each module, commit and push to GitHub.

## 8. Troubleshooting
- `sqlite3: command not found` → `pkg install sqlite`
- `Error: unable to open database file` → check directory permissions or `cd` to correct folder.
- Acode can't see Termux files → grant storage permissions, then open `~` folder in Acode sidebar.

---

Your phone is now a fully‑equipped database engineering lab.  
No server, no cloud, no excuses — just pure SQL forged from your own two hands.

*Built on a phone. Built like a future CTO.*