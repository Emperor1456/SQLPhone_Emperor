# 📘 SQLPhone Emperor v3.0 · Module 8
# 📖 L74 – fetchone(), fetchall(), fetchmany()

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll retrieve query results with surgical precision – one row, all rows, or a custom batch size – and learn when to use each method for performance and memory efficiency.

- 🧱 **fetchone()** – return the next single row (or `None`)  
- 🧠 **fetchall()** – return all remaining rows as a list  
- 🧪 **fetchmany(size)** – return a batch of rows  
- ⚡ **Memory trade‑offs** – why `fetchall()` can crash on huge datasets  

---

## 🧱 FETCH ONE ROW

```python
cursor.execute("SELECT * FROM soldiers WHERE id = ?", (1,))
row = cursor.fetchone()
if row:
    print(row["name"], row["rank"])
else:
    print("Soldier not found.")
```

`fetchone()` is ideal when you expect exactly one result (e.g., lookup by primary key).

---

## 🧱 FETCH ALL ROWS

```python
cursor.execute("SELECT * FROM soldiers")
rows = cursor.fetchall()
for row in rows:
    print(row["name"])
```

`fetchall()` loads every row into memory at once. For a small table, it’s fine. For a million‑row table, it will consume a huge amount of RAM.

---

## 🧱 FETCH MANY ROWS (BATCHED)

```python
cursor.execute("SELECT * FROM soldiers")
while True:
    batch = cursor.fetchmany(10)
    if not batch:
        break
    for row in batch:
        print(row["name"])
    print("--- next batch ---")
```

This processes rows in groups of 10, keeping memory usage low regardless of table size.

---

## 🧱 COMPARISON TABLE

| Method | Use case | Memory impact |
|--------|----------|---------------|
| `fetchone()` | Single‑row lookup | Minimal |
| `fetchall()` | Small result sets | High for large sets |
| `fetchmany(n)` | Large result sets, streaming | Controllable |

> 💡 **INSIGHT:** For web APIs, never call `fetchall()` on a query that could return thousands of rows. Use `fetchmany()` with pagination (`LIMIT`/`OFFSET`).

---

## 💡 Real‑world Usage

**Banking** – fetch account balance by ID
```python
row = cursor.fetchone(); balance = row["balance"] if row else 0
```

**E‑commerce** – stream a product export to CSV without loading all into memory
```python
while batch := cursor.fetchmany(100):
    writer.writerows(batch)
```

**Logistics** – process all pending shipments in chunks
```python
while True:
    batch = cursor.fetchmany(50)
    if not batch: break
    for shipment in batch:
        process(shipment)
```

**Companion** – retrieve the last N conversation entries
```python
cursor.execute("SELECT * FROM conversations WHERE user_id=? ORDER BY ts DESC LIMIT ?", (uid, n))
rows = cursor.fetchall()  # safe because of LIMIT
```

---

## 🔍 Practice Preview
You will retrieve query results using all three fetch methods.

| Level | Task |
|-------|------|
| Easy | Insert 3 rows, then fetch one row by ID with `fetchone()`. |
| Medium | Insert 10 rows, fetch all with `fetchall()`, and print the count. |
| Hard | Insert 50 rows, then write a loop that fetches in batches of 7 and prints each batch’s size. |

Run the coach:
```bash
python ii_Practice_Sheets/L74_fetchone_fetchall_fetchmany.py
```

---

## 📌 Key Takeaway
- `fetchone()` for single rows.  
- `fetchall()` for small, known result sets.  
- `fetchmany(n)` for large datasets – the production‑safe choice.  
- The cursor remembers its position; each fetch advances it.

*For Emperor.*