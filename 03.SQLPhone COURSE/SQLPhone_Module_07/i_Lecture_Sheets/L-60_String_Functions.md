# 📘 SQLPhone Emperor · SQL Module 07
# 📖 L‑60 – String Functions

## 🎯 OBJECTIVE
Manipulate text data with SQLite’s string functions.

## 🧱 BRICK 1 – Core String Functions
- `LENGTH(str)` – number of characters
- `UPPER(str)`, `LOWER(str)` – case conversion
- `SUBSTR(str, start, length)` – extract substring
- `REPLACE(str, old, new)` – search and replace
- `TRIM(str)`, `LTRIM(str)`, `RTRIM(str)` – remove whitespace

```sql
SELECT UPPER(name), SUBSTR(name, 1, 3) FROM users;
```

## 🧱 BRICK 2 – Concatenation and Searching
- `||` operator joins strings (L‑61).
- `INSTR(str, sub)` – position of substring (1‑based, 0 if not found)

```sql
SELECT INSTR('hello world', 'world'); -- 7
```

There is no `SPLIT` function; use `SUBSTR` with `INSTR`
or process in Python.

## 💡 Real‑world Usage
- Normalise names to uppercase.
- Extract initials.
- Clean user input before storage.

## 📌 Key Takeaway
String functions transform text for display and logic.
Combine them to parse and clean data.
For complex string operations, Python is more powerful.

*Text is the universal interface – shape it well.*