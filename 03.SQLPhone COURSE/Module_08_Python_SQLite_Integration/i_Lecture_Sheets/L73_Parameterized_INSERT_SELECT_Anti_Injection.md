# 📘 SQLPhone Emperor v3.0 · Module 8
# 📖 L73 – Parameterized INSERT & SELECT (Anti‑Injection)

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll insert and query data safely using parameterized SQL – the single most important security habit for any developer who touches a database.

- 🔒 **Parameterized queries** – `?` placeholders in SQLite  
- 🧱 **INSERT with parameters** – safe data entry  
- 🧠 **SELECT with parameters** – safe filtering  
- 🧪 **executemany()** – inserting multiple rows efficiently  
- ⚡ **SQL injection demo** – why concatenation is deadly  

---

## 🧱 INSERT SAFELY

```python
cursor.execute(
    "INSERT INTO soldiers (name, rank, salary) VALUES (?, ?, ?)",
    ("Emperor", "General", 5000)
)
conn.commit()
```

The three values are passed as a tuple. The database treats them as pure data, never as code.

---

## 🧱 SELECT WITH PARAMETERS

```python
cursor.execute(
    "SELECT * FROM soldiers WHERE rank = ?",
    ("General",)
)
rows = cursor.fetchall()
for row in rows:
    print(row["name"], row["salary"])
```

Note the trailing comma – `("General",)` makes it a tuple. Without it, `("General")` is just a string.

---

## 🧱 INSERT MANY ROWS (BATCH)

```python
soldiers = [
    ("Rahim", "Colonel", 4000),
    ("Karim", "Private", 2000),
    ("Ali", "Sergeant", 3000),
]
cursor.executemany(
    "INSERT INTO soldiers (name, rank, salary) VALUES (?, ?, ?)",
    soldiers
)
conn.commit()
print(f"Inserted {cursor.rowcount} soldiers.")
```

---

## 🧱 SQL INJECTION DEMO – THE DANGER

```python
# NEVER DO THIS
user_input = "'; DROP TABLE soldiers; --"
query = f"SELECT * FROM soldiers WHERE name = '{user_input}'"
cursor.execute(query)
# The attacker's input closes the quote and executes DROP TABLE!
```

**The attacker’s query becomes:**
```sql
SELECT * FROM soldiers WHERE name = ''; DROP TABLE soldiers; --'
```

> 💀 This deletes your entire table. Parameterized queries make this impossible.

---

## 💡 Real‑world Usage

**Banking** – record a transaction safely
```python
cursor.execute("INSERT INTO transactions (account_id, amount) VALUES (?, ?)", (acc_id, amt))
```

**E‑commerce** – search products by category
```python
cursor.execute("SELECT * FROM products WHERE category = ?", (category,))
```

**Logistics** – batch update shipment statuses
```python
cursor.executemany("UPDATE shipments SET status = ? WHERE tracking_id = ?", updates)
```

**Companion** – store a conversation line
```python
cursor.execute("INSERT INTO conversations (user_id, message) VALUES (?, ?)", (uid, msg))
```

---

## 🔍 Practice Preview
You will write safe, parameterized queries and compare them with the dangerous alternative.

| Level | Task |
|-------|------|
| Easy | Insert a single soldier using parameters. |
| Medium | Insert 5 soldiers with `executemany()`, then select those with salary above a parameterized threshold. |
| Hard | Demonstrate SQL injection with a malicious string, then show how the parameterized version prevents it entirely. |

Run the coach:
```bash
python ii_Practice_Sheets/L73_Parameterized_INSERT_SELECT_Anti_Injection.py
```

---

## 📌 Key Takeaway
- Never embed user input into SQL strings.  
- Use `?` placeholders and pass values as a tuple.  
- `executemany()` efficiently inserts batches.  
- This one habit eliminates the most common and devastating web vulnerability.

*For Emperor.*