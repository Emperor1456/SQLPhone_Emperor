# 📘 SQLPhone Emperor v3.0 · Module 8
# 📖 L75 – UPDATE & DELETE with Python

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll modify and delete rows from Python – the final two CRUD operations. You’ll also learn to verify how many rows were affected and to wrap dangerous operations in error handlers.

- ✏️ **UPDATE from Python** – change existing rows  
- 🗑️ **DELETE from Python** – remove rows  
- 🧱 **Parameterized WHERE** – safe, precise targeting  
- 🧠 **cursor.rowcount** – check how many rows were affected  
- ⚡ **Batch operations** – update/delete many rows at once  

---

## 🧱 UPDATE A SINGLE ROW

```python
cursor.execute(
    "UPDATE soldiers SET rank = ? WHERE id = ?",
    ("General", 1)
)
conn.commit()
print(f"Rows updated: {cursor.rowcount}")
```

`rowcount` tells you exactly how many rows matched the `WHERE` clause.

---

## 🧱 DELETE A ROW

```python
cursor.execute(
    "DELETE FROM soldiers WHERE id = ?",
    (5,)
)
conn.commit()
print(f"Rows deleted: {cursor.rowcount}")
```

---

## 🧱 BATCH OPERATIONS

Promote all soldiers in a specific regiment:

```python
cursor.execute(
    "UPDATE soldiers SET rank = 'Sergeant' WHERE regiment_id = ?",
    (3,)
)
conn.commit()
print(f"Promoted {cursor.rowcount} soldiers.")
```

Delete all soldiers discharged before 2020:

```python
cursor.execute(
    "DELETE FROM soldiers WHERE discharge_date < ?",
    ("2020-01-01",)
)
conn.commit()
print(f"Removed {cursor.rowcount} discharged soldiers.")
```

---

## 🧱 SAFE UPDATE/DELETE PATTERN

Always check the affected rows before committing, and wrap in try/except:

```python
try:
    cursor.execute("DELETE FROM soldiers WHERE id = ?", (soldier_id,))
    if cursor.rowcount == 0:
        print("No soldier found with that ID.")
    else:
        conn.commit()
        print(f"Soldier {soldier_id} removed.")
except sqlite3.Error as e:
    print(f"Database error: {e}")
    conn.rollback()
```

> ⚠️ **WARNING:** `UPDATE` or `DELETE` without a `WHERE` clause affects **every row** in the table. Always double‑check your conditions before executing.

> 💡 **INSIGHT:** For large batch deletes, consider breaking them into smaller chunks (`LIMIT 1000`) and committing each chunk to avoid locking the database for too long.

---

## 💡 Real‑world Usage

**Banking** – apply monthly interest to all savings accounts
```python
cursor.execute("UPDATE accounts SET balance = balance * 1.005 WHERE type = 'savings'")
```

**E‑commerce** – remove discontinued products
```python
cursor.execute("DELETE FROM products WHERE active = 0")
```

**Logistics** – mark all delayed shipments
```python
cursor.execute("UPDATE shipments SET status = 'delayed' WHERE delivery_date < date('now')")
```

**Companion** – delete old conversation logs for privacy
```python
cursor.execute("DELETE FROM conversations WHERE timestamp < date('now', '-90 days')")
```

---

## 🔍 Practice Preview
You will perform update and delete operations from Python.

| Level | Task |
|-------|------|
| Easy | Update a single soldier’s rank by ID and print the rowcount. |
| Medium | Insert 5 soldiers, then delete one and verify with `rowcount`. |
| Hard | Perform a batch salary increase for all soldiers in a regiment, wrapped in a transaction with rollback on error. |

Run the coach:
```bash
python ii_Practice_Sheets/L75_UPDATE_DELETE_with_Python.py
```

---

## 📌 Key Takeaway
- Use parameterized `UPDATE` and `DELETE` for safe, precise operations.  
- `cursor.rowcount` verifies how many rows were affected.  
- Always commit after writes; wrap in try/except for safety.  
- Batch operations can change millions of rows with a single statement.

*For Emperor.*