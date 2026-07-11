# 📘 SQLPhone Emperor v3.0 · Module 1
# 📖 L07 – ORDER BY, LIMIT & OFFSET – Sorting & Pagination

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, you’ll control the order and quantity of your query results — essential for dashboards, reports, and APIs.

- 📊 **ORDER BY** – sort results by any column, ascending or descending
- 🔢 **LIMIT** – return only a fixed number of rows
- 📄 **OFFSET** – skip rows for pagination
- 🧪 **Combining all three** – build a paginated, sorted report in one query

---

## 🧱 ORDER BY – SORTING RESULTS

`ORDER BY` sorts the result set by one or more columns.
By default, sorting is **ascending** (`ASC`). Use `DESC` for descending.

```sql
SELECT name, salary FROM soldiers
ORDER BY salary DESC;
```

**Multiple sort keys** – sort by rank, then by name within each rank:

```sql
SELECT name, rank, salary FROM soldiers
ORDER BY rank ASC, name ASC;
```

> ⚠️ **WARNING:** Without `ORDER BY`, the database may return rows in
> any order. Never rely on insertion order unless you explicitly sort.

---

## 🧱 LIMIT – RESTRICTING ROW COUNT

`LIMIT` caps how many rows are returned. It’s essential for dashboards
where you only want the top 5 or top 10 results.

```sql
-- Top 3 highest‑paid soldiers
SELECT name, salary FROM soldiers
ORDER BY salary DESC
LIMIT 3;
```

---

## 🧱 OFFSET – SKIPPING ROWS

`OFFSET` skips a specified number of rows before returning results.
Combined with `LIMIT`, it enables **pagination** — showing results page by page.

```sql
-- Page 2 of results (skip the first 5, return the next 5)
SELECT name, salary FROM soldiers
ORDER BY salary DESC
LIMIT 5 OFFSET 5;
```

In web applications, you’d compute `OFFSET` from the page number:
`OFFSET = (page_number - 1) * page_size`.

> 💡 **INSIGHT:** Always use `ORDER BY` with `LIMIT`/`OFFSET`.
> Without it, pagination is meaningless because rows have no guaranteed order.

---

## 💡 Real‑world Usage

**Banking – top 5 largest accounts**
```sql
SELECT account_id, balance FROM accounts
ORDER BY balance DESC
LIMIT 5;
```

**E‑commerce – paginated product catalog**
```sql
SELECT name, price FROM products
ORDER BY price ASC
LIMIT 10 OFFSET 20;  -- third page of results
```

**Logistics – most recent shipments**
```sql
SELECT tracking_id, destination, dispatched_date
FROM shipments
ORDER BY dispatched_date DESC
LIMIT 25;
```

**HR – employees sorted by tenure, paginated**
```sql
SELECT name, hire_date FROM employees
ORDER BY hire_date ASC
LIMIT 15 OFFSET 0;   -- first page
```

---

## 🔍 Practice Preview
You will sort, limit, and paginate the Imperial Army’s soldier records.

| Level | Task |
|-------|------|
| Easy | Select all soldiers sorted by salary descending. |
| Medium | Select the top 3 highest‑paid soldiers. |
| Hard | Select the second page of soldiers (3 per page) sorted by name. |

Run the coach:
```bash
python ii_Practice_Sheets/L07_ORDER_BY_LIMIT_OFFSET_Sorting_Pagination.py
```

---

## 📌 Key Takeaway
- `ORDER BY` sorts results; use `ASC` (default) or `DESC`.
- `LIMIT` caps the number of rows returned.
- `OFFSET` skips rows, enabling pagination.
- Always use `ORDER BY` with `LIMIT`/`OFFSET` for predictable results.

*For Emperor.*