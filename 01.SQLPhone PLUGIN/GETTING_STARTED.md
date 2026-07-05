# 🚀 Getting Started — SQLPhone Emperor
**Phone-first SQL with Termux, Acode & SQLite**

Start here to go from zero to your first query in under 10 minutes.

---

## 1. What You Need
- Android phone (Android 7+ recommended)
- Termux (from F‑Droid – see Setup Guide)
- Acode editor (Play Store)
- 10 minutes of focused typing

---

## 2. Install Termux & SQLite
If you haven't already, follow the Setup Guide to install Termux and SQLite.
Once done, verify:
```bash
sqlite3 --version
```

---

## 3. Open SQLite
In Termux, type:
```bash
sqlite3
```
You'll see the SQLite prompt:
```
sqlite>
```

---

## 4. Your First Database
At the prompt, create a database and a table:
```sql
CREATE TABLE emperors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    reign_start INTEGER
);
```
Insert yourself:
```sql
INSERT INTO emperors VALUES (1, 'Emperor', 2026);
```
Query it:
```sql
SELECT * FROM emperors;
```
Exit:
```
.quit
```

---

## 5. Your First SQL File
Open Acode, create a new file `first.sql` inside your course folder.
Type the same commands you just ran, save it.
Then execute it from Termux:
```bash
sqlite3 my_empire.db < first.sql
sqlite3 my_empire.db "SELECT * FROM emperors;"
```

---

## 6. Daily Workflow
1. Read the lecture sheet (`.md`) in Acode.
2. Write the practice queries in a `.sql` file.
3. Run them in Termux.
4. Check the output. If wrong, fix and re‑run.
5. Once correct, move to the next lesson.
6. Push to GitHub after each module.

---

## 7. You’re Ready
Open Module 01, Lesson‑01, and start learning real SQL.
No laptop required. No shortcuts. Just pure skill.

*Everything entirely on a phone by Emperor.*