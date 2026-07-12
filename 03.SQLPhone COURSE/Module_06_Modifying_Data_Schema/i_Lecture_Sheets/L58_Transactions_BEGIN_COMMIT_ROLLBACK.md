# 📘 SQLPhone Emperor v3.0 · Module 6
# 📖 L58 – Transactions – BEGIN, COMMIT, ROLLBACK

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll group multiple operations into atomic units — ensuring your database never ends up in a half‑finished state. This is the “A” in ACID, and it’s what separates a reliable database from a fragile one.

- 🧱 **Transaction concept** – all‑or‑nothing execution
- 🧠 **BEGIN / COMMIT** – start and confirm a transaction
- 🧪 **ROLLBACK** – undo all changes since the last `BEGIN`
- ⚡ **When to use** – money transfers, batch updates, schema migrations
- 🛡️ **Savepoints** – nested checkpoints within a transaction
- 💾 **Performance** – wrapping multiple writes in one transaction is much faster

---

## 🧱 WHAT IS A TRANSACTION?

A transaction bundles one or more SQL statements into a single unit. Either **all statements succeed** (`COMMIT`), or **none of them are applied** (`ROLLBACK`). This is the atomicity guarantee of ACID.

```sql
BEGIN;
UPDATE accounts SET balance = balance - 500 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 500 WHERE account_id = 2;
COMMIT;
```

If the second `UPDATE` fails (e.g., constraint violation), you can `ROLLBACK` and no money is lost. The database remains in a consistent state.

---

## 🧱 ROLLBACK ON ERROR

```sql
BEGIN;
UPDATE soldiers SET salary = salary * 1.5 WHERE regiment_id = 1;
-- Oops, wrong regiment
ROLLBACK;
```

The salary increase is completely undone, as if it never happened. No manual cleanup is required.

---

## 🧱 SAVEPOINTS – NESTED CHECKPOINTS

Savepoints allow you to roll back part of a transaction without discarding the entire thing. They are lightweight and can be created and released as needed.

```sql
BEGIN;
UPDATE soldiers SET salary = 5000 WHERE soldier_id = 1;

SAVEPOINT before_promotion;
UPDATE soldiers SET rank = 'General' WHERE soldier_id = 1;
-- Oops, wrong soldier – only roll back the promotion
ROLLBACK TO before_promotion;

UPDATE soldiers SET rank = 'Colonel' WHERE soldier_id = 1;
COMMIT;
```

The salary change persists; the mistaken promotion is rolled back. Savepoints are especially useful in long‑running migrations or complex batch operations.

---

## 🧱 IMPLICIT TRANSACTIONS

In SQLite, every single statement outside an explicit transaction runs in its own automatic transaction. This means:

```sql
INSERT INTO soldiers (name) VALUES ('Emperor');
```

is equivalent to:

```sql
BEGIN;
INSERT INTO soldiers (name) VALUES ('Emperor');
COMMIT;
```

Wrapping multiple writes in an explicit `BEGIN`…`COMMIT` is **much faster** because the database only writes to disk once, at commit time, instead of after every statement.

> ⚠️ **WARNING:** If you forget `COMMIT` and close the connection, SQLite automatically rolls back. Always explicitly commit successful transactions.

> 💡 **INSIGHT:** For bulk inserts, wrap 1000 rows in one transaction instead of committing each row individually. You’ll see a 10‑100x speed improvement.

---

## 🧱 TRANSACTIONS IN PYTHON

The same principles apply when working from Python:

```python
import sqlite3

conn = sqlite3.connect("empire.db")
try:
    conn.execute("BEGIN")
    conn.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (500, 1))
    conn.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (500, 2))
    conn.commit()
    print("Transfer successful.")
except sqlite3.Error as e:
    conn.rollback()
    print(f"Transfer failed, rolled back: {e}")
finally:
    conn.close()
```

Using `with` and a custom context manager (from L78) further simplifies this pattern.

---

## 💡 Real‑world Usage

**Banking – transfer between accounts**
```sql
BEGIN;
UPDATE accounts SET balance = balance - 1000 WHERE account_id = 101;
UPDATE accounts SET balance = balance + 1000 WHERE account_id = 202;
COMMIT;
```

**E‑commerce – place an order (reduce stock + create order record)**
```sql
BEGIN;
INSERT INTO orders (customer_id, order_date) VALUES (1, date('now'));
UPDATE inventory SET quantity = quantity - 1 WHERE product_id = 5;
COMMIT;
```

**Logistics – update multiple shipment statuses in one go**
```sql
BEGIN;
UPDATE shipments SET status = 'delivered' WHERE tracking_id = 'TRK-100';
UPDATE shipments SET status = 'delivered' WHERE tracking_id = 'TRK-101';
COMMIT;
```

**HR – batch salary increase with validation**
```sql
BEGIN;
UPDATE employees SET salary = salary * 1.1 WHERE department = 'Engineering';
-- If anything goes wrong, ROLLBACK
COMMIT;
```

**Companion – save a conversation turn and update memory atomically**
```sql
BEGIN;
INSERT INTO conversations (user_id, message) VALUES (1, 'Hello');
INSERT INTO memories (user_id, fact) VALUES (1, 'User greeted');
COMMIT;
```

---

## 🔍 Practice Preview
You will execute atomic operations on the Imperial Army database.

| Level | Task |
|-------|------|
| Easy | Begin a transaction, update a soldier's salary, and commit. |
| Medium | Begin a transaction, perform two updates, then rollback — verify nothing changed. |
| Hard | Simulate a fund transfer between two regiment budgets using a transaction with a savepoint for partial rollback. |

Run the coach:
```bash
python ii_Practice_Sheets/L58_Transactions_BEGIN_COMMIT_ROLLBACK.py
```

---

## 📌 Key Takeaway
- `BEGIN` starts a transaction; `COMMIT` saves it; `ROLLBACK` undoes it.
- Use transactions for any multi‑step operation where partial completion is unacceptable.
- Transactions also dramatically improve write performance.
- Savepoints let you roll back portions of a transaction without losing everything.

*For Emperor.*