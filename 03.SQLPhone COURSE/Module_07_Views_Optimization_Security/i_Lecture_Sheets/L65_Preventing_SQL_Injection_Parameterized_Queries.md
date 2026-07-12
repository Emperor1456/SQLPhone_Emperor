# 📘 SQLPhone Emperor v3.0 · Module 7
# 📖 L65 – Preventing SQL Injection – Parameterized Queries

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll write SQL that hackers cannot break — using parameterized queries, the single most important security habit for any developer who touches a database.

- 🧱 **What SQL injection is** – malicious input that rewrites your query  
- 🧠 **The golden rule** – never concatenate user input into SQL strings  
- 🧪 **Parameterized queries in SQLite** – `?` placeholders  
- ⚡ **Beyond SQLite** – the same pattern works in PostgreSQL, MySQL, and all ORMs  
- 🛡️ **Real‑world attacks** – what happens when you ignore this  

---

## 🧱 WHAT IS SQL INJECTION?

If you build SQL by gluing strings together with user input, an attacker can inject their own SQL commands.

```sql
-- DANGEROUS: user_input = "'; DROP TABLE soldiers; --"
query = "SELECT * FROM soldiers WHERE name = '" + user_input + "'";
```

The attacker's input closes the quote and executes `DROP TABLE soldiers`. Your entire table is gone.

---

## 🧱 THE FIX: PARAMETERIZED QUERIES

Use `?` placeholders and pass values separately. The database treats them as pure data — never as executable code.

**In Python:**
```python
cursor.execute("SELECT * FROM soldiers WHERE name = ?", (user_input,))
```

**In pure SQL (shell), parameters are not supported directly, but you should always use them in application code.**

---

## 🧱 MULTIPLE PARAMETERS

```python
cursor.execute(
    "INSERT INTO soldiers (name, rank, salary) VALUES (?, ?, ?)",
    (name, rank, salary)
)
```

> ⚠️ **WARNING:** Never use f‑strings, `.format()`, or `%` substitution to embed user data into SQL. The database engine must receive the query and the data separately to prevent injection.

> 💡 **INSIGHT:** This single habit eliminates the most common and devastating web vulnerability. Every professional codebase enforces it.

---

## 💡 Real‑world Usage

**Banking – safe transaction lookup**
```python
cursor.execute("SELECT * FROM transactions WHERE account_id = ?", (account_id,))
```

**E‑commerce – safe product search**
```python
cursor.execute("SELECT * FROM products WHERE name LIKE ?", (f"%{query}%",))
```

**Logistics – safe status update**
```python
cursor.execute("UPDATE shipments SET status = ? WHERE tracking_id = ?", (status, tracking_id))
```

**HR – safe employee insert**
```python
cursor.execute("INSERT INTO employees (name, department) VALUES (?, ?)", (name, dept))
```

---

## 🔍 Practice Preview
You will write parameterized queries and compare them with unsafe concatenation.

| Level | Task |
|-------|------|
| Easy | Write a parameterized `SELECT` to find a soldier by name. |
| Medium | Write a parameterized `INSERT` to add a new soldier safely. |
| Hard | Explain why parameterized queries prevent SQL injection and demonstrate the danger with an example. |

Run the coach:
```bash
python ii_Practice_Sheets/L65_Preventing_SQL_Injection_Parameterized_Queries.py
```

---

## 📌 Key Takeaway
- Never concatenate user input into SQL strings.  
- Use parameterized queries with `?` placeholders.  
- This single habit eliminates SQL injection — the most common web vulnerability.  
- The pattern is identical across all databases and ORMs.

*For Emperor.*