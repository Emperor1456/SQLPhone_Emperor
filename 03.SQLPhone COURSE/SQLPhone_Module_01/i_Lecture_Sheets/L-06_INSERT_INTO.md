# 📘 SQLPhone Emperor · SQL Module 01
# 📖 L‑06 – INSERT INTO

## 🎯 OBJECTIVE
Insert data into tables using single‑row and multi‑row inserts,
understand column ordering, and avoid common pitfalls.

## 🧱 BRICK 1 – Single‑Row INSERT
The basic syntax for adding a new tuple:

```sql
INSERT INTO customers (first_name, last_name, email)
VALUES ('Emperor', 'SQLPhone', 'emperor@sqlphone.dev');
```

If you omit the column list, SQLite expects values for all
columns in the order they were defined, including auto‑generated
ones. That’s error‑prone – always specify the column list.

**Inserting into `INTEGER PRIMARY KEY` column:**
Pass NULL or omit the column; SQLite will assign a unique id:
```sql
INSERT INTO customers (customer_id, first_name, last_name, email)
VALUES (NULL, 'John', 'Doe', 'john@example.com');
```

## 🧱 BRICK 2 – Multi‑Row INSERT & INSERT from SELECT
Insert multiple rows in one statement for performance:
```sql
INSERT INTO customers (first_name, last_name, email)
VALUES
    ('Alice', 'Smith', 'alice@example.com'),
    ('Bob', 'Brown', 'bob@example.com'),
    ('Carol', 'White', 'carol@example.com');
```

You can also copy data from another table:
```sql
INSERT INTO customers (first_name, last_name, email)
SELECT first_name, last_name, email FROM temp_customers;
```

**Returning clause (SQLite 3.35+):**
```sql
INSERT INTO customers (first_name, last_name, email)
VALUES ('Test', 'User', 'test@example.com')
RETURNING customer_id;
```
This retrieves the generated primary key in one round trip.

## 💡 Production Best Practices
- Always use explicit column lists.
- Use multi‑row inserts for bulk operations – it’s faster.
- When possible, use `RETURNING` to get auto‑generated IDs
  without an extra `SELECT` query.
- In applications, use parameterized queries (prepared statements)
  to prevent SQL injection.

## 📌 Key Takeaway
`INSERT INTO` creates data.
Specify columns explicitly, batch inserts for performance,
and use `RETURNING` to capture generated IDs.

*Data doesn’t exist until you insert it.*