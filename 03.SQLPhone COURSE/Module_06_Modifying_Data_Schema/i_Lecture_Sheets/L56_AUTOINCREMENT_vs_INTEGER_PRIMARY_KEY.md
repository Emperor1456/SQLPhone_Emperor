# 📘 SQLPhone Emperor v3.0 · Module 6
# 📖 L56 – AUTOINCREMENT vs INTEGER PRIMARY KEY

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll understand the subtle but critical difference between `AUTOINCREMENT` and `INTEGER PRIMARY KEY` — and when each one is the right choice for your database.

- 🧱 **INTEGER PRIMARY KEY** – the default auto‑generated ID in SQLite
- 🧠 **AUTOINCREMENT** – a stricter, slower variant
- 🧪 **Key differences** – behaviour on deletion, reuse of IDs
- ⚡ **Best practices** – which to use for most applications
- 🛡️ **Real‑world consequences** – when ID reuse can become a legal or security problem

---

## 🧱 INTEGER PRIMARY KEY (Default)

When you define a column as `INTEGER PRIMARY KEY`, SQLite treats it as an alias for the internal `rowid`. If you insert `NULL`, SQLite automatically assigns a unique integer — usually one greater than the current maximum `rowid`. However, if you delete the row with the highest `rowid`, that ID **may be reused** for a future insert.

```sql
CREATE TABLE soldiers (
    soldier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

INSERT INTO soldiers VALUES (NULL, 'Emperor');  -- assigned id = 1
DELETE FROM soldiers WHERE soldier_id = 1;
INSERT INTO soldiers VALUES (NULL, 'Rahim');    -- may reuse id = 1
```

This behaviour keeps the database compact and fast. For most applications, it’s perfect.

---

## 🧱 AUTOINCREMENT

Adding `AUTOINCREMENT` prevents ID reuse. SQLite guarantees that each new row gets an ID strictly larger than any previously used in that table, even if older rows are deleted. This guarantee comes at a small performance cost because SQLite must track the maximum ID in a separate system table called `sqlite_sequence`.

```sql
CREATE TABLE audit_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT NOT NULL,
    created_at TEXT DEFAULT (datetime('now'))
);

INSERT INTO audit_log (message) VALUES ('User login');
DELETE FROM audit_log WHERE log_id = 1;
INSERT INTO audit_log (message) VALUES ('User logout');  -- id will be 2, never 1
```

---

## 🧱 COMPARISON TABLE

| Feature | `INTEGER PRIMARY KEY` | `AUTOINCREMENT` |
|---------|-----------------------|-----------------|
| ID uniqueness | Yes | Yes |
| ID reuse after delete | Possible (if max row deleted) | Never |
| Performance | Faster | Slightly slower (writes to `sqlite_sequence`) |
| Storage overhead | None | Minimal (one extra table) |
| Use case | Most applications | Audit trails, legal records, public‑facing IDs |

---

## 🧱 WHEN ID REUSE BECOMES DANGEROUS

Imagine a hospital system where `patient_id` is reused. A doctor pulls up patient 42’s old record, thinking it’s the new patient. Or an e‑commerce system where a cancelled order ID is reassigned, and a customer service agent pulls up the wrong transaction. In these cases, `AUTOINCREMENT` is mandatory — not for performance, but for safety.

Similarly, any ID that appears in a URL, a printed invoice, or a legal document should never be reused. That’s the domain of `AUTOINCREMENT`.

> 💡 **INSIGHT:** For Companion’s memory system, `INTEGER PRIMARY KEY` is fine for internal IDs. For anything that a user might see (conversation IDs, shared memory references), use `AUTOINCREMENT` or a UUID.

> ⚠️ **WARNING:** If you use `AUTOINCREMENT`, never manually insert a value that could collide with the auto‑generated sequence. Let SQLite manage the ID.

---

## 💡 Real‑world Usage

**Banking – transaction IDs that auditors must never see repeated**
```sql
CREATE TABLE transactions (
    txn_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER,
    amount REAL,
    txn_date TEXT DEFAULT (datetime('now'))
);
```

**E‑commerce – shopping cart items (temporary, reuse acceptable)**
```sql
CREATE TABLE cart_items (
    item_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    quantity INTEGER
);
```

**Logistics – shipment tracking numbers generated externally (natural key)**
```sql
CREATE TABLE shipments (
    tracking_id TEXT PRIMARY KEY
);
```

**HR – employee IDs that must never be recycled**
```sql
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
```

**Companion – internal memory entries (reuse acceptable) vs. shared conversation IDs (reuse unacceptable)**

---

## 🔍 Practice Preview
You will create tables with both key strategies and observe the difference.

| Level | Task |
|-------|------|
| Easy | Create a table with `INTEGER PRIMARY KEY` and insert several rows. |
| Medium | Create a table with `AUTOINCREMENT`, insert, delete the max row, and insert again to compare ID assignment. |
| Hard | Explain a real‑world scenario where `AUTOINCREMENT` is necessary and implement it with justification in comments. |

Run the coach:
```bash
python ii_Practice_Sheets/L56_AUTOINCREMENT_vs_INTEGER_PRIMARY_KEY.py
```

---

## 📌 Key Takeaway
- `INTEGER PRIMARY KEY` is fast, simple, and sufficient for most use cases.
- `AUTOINCREMENT` guarantees IDs are never reused at a small performance cost.
- Choose based on whether ID reuse is acceptable in your domain.

*For Emperor.*
