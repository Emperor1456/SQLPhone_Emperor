# 📘 SQLPhone Emperor · Module 01  
# 📖 L‑09 – SQL Syntax Rules & Best Practices (Imperial User Directory)

---

## 🎯 OBJECTIVE  
Master the formal syntax rules of SQL and adopt professional formatting conventions.  
You’ll build the Imperial User Directory — a `users` table of active and inactive accounts — while applying the exact style standards used by top engineering teams.  
Clean, readable SQL is not optional; it’s the signature of a craftsman.

---

## 🧱 BRICK 1 – Syntax Rules: The Language Itself

SQL is declarative: you state *what* you want, not *how* to get it.  
Its syntax is small, but every character matters.

**① Create the users table (Easy practice)**
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    email TEXT,
    active INTEGER
);
```
- Every SQL statement ends with a semicolon (`;`). Forgetting it in the CLI gives a continuation prompt (`...>`).  
- Keywords like `CREATE`, `TABLE`, `INTEGER` are case‑insensitive, but the professional convention is **UPPERCASE** for keywords.  
- Identifiers (table/column names) are case‑insensitive for ASCII. Avoid spaces or special characters; use `snake_case`.

**② Insert two users: one active, one inactive**
```sql
INSERT INTO users (username, email, active)
VALUES
    ('emperor', 'e@x.com', 1),
    ('test', 't@x.com', 0);
```
- String literals use single quotes (`'emperor'`). Double quotes are for identifiers — never mix them.  
- Multi‑row inserts batch values with commas; the final semicolon ends the statement.

**③ Verify the data**
```sql
SELECT * FROM users;
```
You’ll see two rows. The syntax is simple, but the precision is mandatory.

> 💡 **INSIGHT:** SQL is a declarative language. You don’t write loops to scan rows — you describe the result set, and the engine plans the execution. This separation is what makes SQL powerful and portable.

> ⚠️ **WARNING:** Never use double quotes for string values. `"emperor"` is treated as an identifier (column or table name), not a string. This is a leading cause of silent bugs.

---

## 🧱 BRICK 2 – Professional Formatting & Naming Conventions

Code is read far more than it is written. Formatting is not decoration — it’s communication.

**④ Write a formatted query for active users (Medium practice)**
```sql
SELECT username, email
FROM users
WHERE active = 1;
```
- Uppercase keywords (`SELECT`, `FROM`, `WHERE`) stand out from lowercase identifiers.  
- Each major clause starts on a new line, indented consistently.  
- The statement fits on a phone screen — no horizontal scrolling.

**⑤ Rewrite the same query, now sorted and with a comment (Hard practice)**
```sql
-- Active users, sorted alphabetically
SELECT username, email
FROM users
WHERE active = 1
ORDER BY username;
```
- The comment explains *why*, not *what*.  
- `ORDER BY` adds sorting without changing the query’s structure.  
- Even though column names are case‑insensitive, writing them in lowercase keeps the visual flow consistent with the data.

**⑥ Naming standards applied**
- Table names: singular, `snake_case` (`user`, `order_item`).  
- Primary key: `table_name_id` when used as a foreign key elsewhere.  
- Avoid reserved words as table names (e.g., `Order` requires quoting).  
- This directory will grow; consistent names prevent chaos when the empire scales.

**⑦ Formatting checklist for every query**
1. Keywords in UPPERCASE.  
2. Each clause (`SELECT`, `FROM`, `WHERE`, `ORDER BY`) on its own line.  
3. Use line breaks and indentation for readability.  
4. Keep lines under 80 characters for phone‑friendly code.  
5. Add a comment for business logic that isn’t obvious.

> 💡 **ADVANCED TIP – Comma‑first style:**  
> For large column lists, some teams use the comma‑first style to simplify diffs:
> ```sql
> SELECT username
>      , email
>      , active
> FROM users;
> ```
> This is optional, but know it — you’ll see it in production codebases.

---

## 💡 Real‑world Usage

**Banking – retrieve active accounts**
```sql
SELECT account_id, balance
FROM accounts
WHERE active = 1
ORDER BY balance DESC;
```

**E‑commerce – list products under $50**
```sql
SELECT name, price
FROM products
WHERE price < 50
ORDER BY name;
```

**Logistics – show pending shipments**
```sql
SELECT tracking_id, destination
FROM shipments
WHERE status = 'pending'
ORDER BY created_at;
```

**HR – active employees by department**
```sql
SELECT name, department
FROM employees
WHERE active = 1
ORDER BY department, name;
```

---

## 🔍 Practice Preview
You will build and query the Imperial User Directory with professional formatting.

| Level  | Task | What You’ll Write |
|--------|------|-------------------|
| Easy   | Create table `users` (id PK, username, email, active). Insert two users (one active=1, one active=0). | `CREATE TABLE users ...` and multi‑row `INSERT` |
| Medium | Write a nicely formatted SELECT (uppercase keywords, line breaks) that shows all active users. | `SELECT username, email FROM users WHERE active = 1;` |
| Hard   | Rewrite the query with a comment, sorted by username, and using lowercase for column names (still works). | `-- Active users sorted` `SELECT username, email FROM users WHERE active = 1 ORDER BY username;` |

Run the coach:
```bash
python ii_Practice_Sheets/L-09_Syntax_Rules.py
```

---

## 📌 Key Takeaway
- Every statement ends with `;`. Keywords are UPPERCASE by convention.
- String literals use single quotes. Identifiers use `snake_case`.
- Format clauses on separate lines for readability.
- Comments carry business context. Style is not optional — it’s the hallmark of a professional.