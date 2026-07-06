# 📘 SQLPhone Emperor · SQL Module 02
# 📖 L‑13 – AND, OR, NOT

## 🎯 OBJECTIVE
Combine multiple conditions using logical operators
to create complex filters.

## 🧱 BRICK 1 – AND Operator
`AND` requires **all** conditions to be true.
```sql
SELECT * FROM employees
WHERE department = 'Sales' AND salary > 60000;
```
Both conditions must hold for a row to be included.

## 🧱 BRICK 2 – OR and NOT Operators
`OR` requires **at least one** condition to be true.
```sql
SELECT * FROM employees
WHERE department = 'Sales' OR department = 'Marketing';
```

`NOT` negates a condition.
```sql
SELECT * FROM employees
WHERE NOT department = 'HR';
```
Equivalent to `<> 'HR'`.

**Precedence:** `NOT` has highest priority, then `AND`, then `OR`.
Use parentheses to control the order and avoid confusion:
```sql
SELECT * FROM employees
WHERE (department = 'Sales' OR department = 'Marketing')
  AND salary > 60000;
```

## 💡 Real‑world Usage
- Find customers from specific regions who purchased after a date.
- Exclude cancelled orders.
- Filter inventory for items in stock but below reorder level.

## 📌 Key Takeaway
Logical operators let you build precise filters.
Always use parentheses to make your intent clear.
`AND`, `OR`, `NOT` are the glue of complex conditions.

*Clarity in logic is clarity in business rules.*