# 📘 SQLPhone Emperor · SQL Module 02
# 📖 L‑15 – LIMIT and OFFSET

## 🎯 OBJECTIVE
Control the number of rows returned and implement
pagination using `LIMIT` and `OFFSET`.

## 🧱 BRICK 1 – LIMIT
`LIMIT` restricts the result set to a maximum number of rows.
```sql
SELECT * FROM products ORDER BY price DESC
LIMIT 5;
```
This returns only the first 5 rows (after sorting).

`LIMIT` is evaluated after `ORDER BY`, so you get
the top‑N rows.

## 🧱 BRICK 2 – OFFSET
`OFFSET` skips a specified number of rows before starting
to return rows.

```sql
SELECT * FROM products ORDER BY price DESC
LIMIT 5 OFFSET 10;
```
Returns rows 11–15 (skips first 10, then takes 5).

Used for pagination: page `n` (1‑based) has
`LIMIT page_size OFFSET (page - 1) * page_size`.

**Note:** In SQLite, `LIMIT` and `OFFSET` can also be written
with a comma: `LIMIT 10, 5` means offset 10, limit 5,
but the `OFFSET` keyword is more readable.

## 💡 Real‑world Usage
- Display the top 10 most expensive items.
- Implement "Load more" in APIs.
- Paginate through large query results on a phone UI.

## 📌 Key Takeaway
`LIMIT` caps the number of rows.
`OFFSET` jumps ahead.
Together they give you precise control over result chunks.

*Page by page, row by row – LIMIT your data, not your ambitions.*