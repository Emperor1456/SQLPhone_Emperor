# 📘 SQLPhone Emperor · SQL Module 02
# 📖 L‑18 – LIKE

## 🎯 OBJECTIVE
Perform pattern matching on text using the `LIKE` operator.

## 🧱 BRICK 1 – LIKE with Wildcards
`LIKE` compares a string against a pattern.
Two wildcards:
- `%` – matches any sequence of zero or more characters.
- `_` – matches exactly one character.

Examples:
```sql
SELECT * FROM users WHERE email LIKE '%@gmail.com';
-- All Gmail addresses

SELECT * FROM products WHERE name LIKE 'A%';
-- Names starting with 'A'

SELECT * FROM words WHERE word LIKE '_a%';
-- Words whose second letter is 'a'
```

## 🧱 BRICK 2 – Case Sensitivity and ESCAPE
In SQLite, `LIKE` is case‑insensitive for ASCII characters
by default. To force case‑sensitive, use `PRAGMA case_sensitive_like=ON;`
or the `GLOB` operator (different syntax).

To match a literal `%` or `_`, use the `ESCAPE` clause:
```sql
SELECT * FROM notes WHERE content LIKE '%10\%%' ESCAPE '\';
```
Matches strings containing "10%".

## 💡 Real‑world Usage
- Search users by partial name.
- Filter email domains.
- Validate patterns (phone numbers, codes).

## 📌 Key Takeaway
`LIKE` brings simple pattern matching to SQL.
Use `%` and `_` wisely.
For complex patterns, consider regular expressions (outside this course).

*LIKE opens the door to fuzzy searching.*