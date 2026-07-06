# 📘 SQLPhone Emperor · SQL Module 02
# 📖 L‑17 – IN

## 🎯 OBJECTIVE
Match a column against a list of values using `IN`.

## 🧱 BRICK 1 – The IN Operator
`IN` checks if a value belongs to a set.
```sql
SELECT * FROM customers
WHERE country IN ('USA', 'Canada', 'Mexico');
```
Equivalent to `country = 'USA' OR country = 'Canada' OR country = 'Mexico'`.

The list can be any comma‑separated values in parentheses.

## 🧱 BRICK 2 – NOT IN and Subquery Compatibility
`NOT IN` excludes values in the list.
```sql
SELECT * FROM customers
WHERE country NOT IN ('USA', 'Canada');
```

`IN` is often used with subqueries (future module), but for now
you can hard‑code the list.

**Performance tip:** When the list is large, consider using
a temporary table or an indexed lookup if performance matters.

## 💡 Real‑world Usage
- Filter by multiple status codes.
- Select specific product categories.
- Exclude test accounts.

## 📌 Key Takeaway
`IN` simplifies multiple `OR` conditions.
It’s cleaner and easier to read.
Use `NOT IN` to exclude unwanted values.

*In a list of possibilities, IN finds the match.*