# 📘 SQLPhone Emperor · SQL Module 07
# 📖 L‑61 – Concatenation Operator (||)

## 🎯 OBJECTIVE
Combine strings using the SQL standard `||` operator.

## 🧱 BRICK 1 – Basic Concatenation
The double pipe `||` joins two or more strings.
```sql
SELECT first_name || ' ' || last_name AS full_name
FROM employees;
```

Works with any string value, including columns and literals.

## 🧱 BRICK 2 – Concatenation with NULL
If any operand is NULL, the result is NULL.
Use `COALESCE` to provide a fallback:
```sql
SELECT first_name || ' ' || COALESCE(middle_name, '') || ' ' || last_name
FROM employees;
```

Concatenation is also used to build dynamic messages,
construct file paths, or format output.

## 💡 Real‑world Usage
- Full name display.
- Address lines.
- Generate unique identifiers.

## 📌 Key Takeaway
`||` is the simplest way to merge strings.
Handle NULLs with `COALESCE` to avoid empty results.
It’s safe, standard, and readable.

*Join strings like data – with intention.*