# 📘 SQLPhone Emperor · SQL Module 09
# 📖 L‑75 – UPDATE and DELETE with Python

## 🎯 OBJECTIVE
Modify and remove rows using Python‑executed SQL.

## 🧱 BRICK 1 – Safe UPDATE
Use parameterized queries for updates as well:
```python
new_salary = 85000
employee_id = 2
cur.execute('UPDATE employees SET salary = ? WHERE id = ?', (new_salary, employee_id))
conn.commit()
```

## 🧱 BRICK 2 – Safe DELETE
Similarly, delete with placeholders:
```python
emp_id = int(input('ID to delete: '))
cur.execute('DELETE FROM employees WHERE id = ?', (emp_id,))
conn.commit()
```

Always commit to persist the changes.
Without a `WHERE` clause, all rows are affected – be careful.

## 💡 Real‑world Usage
- Editing records in admin panels.
- Removing outdated data.
- Archiving rows by flag instead of deleting.

## 📌 Key Takeaway
UPDATE and DELETE use the same parameterized pattern as INSERT.
Never hard‑code values; always use `?`.
Commit is necessary.

*Modify data with the same caution as in pure SQL.*