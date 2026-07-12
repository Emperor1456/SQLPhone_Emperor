# 📘 SQLPhone Emperor v3.0 · Module 2
# 📖 L18 – Date & Time Functions – date(), time(), strftime()

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll manipulate dates and times directly in SQLite — essential for reports, logs, scheduling, and any data that changes over time.

- 📅 **date()** – extract or compute dates
- ⏰ **time()** – extract or compute times
- 🧪 **datetime()** – combined date and time
- 🧙 **strftime()** – format and transform date/time values
- 🧮 **Date arithmetic** – add/subtract days, months, years
- ⚡ **Real‑world** – age calculation, deadlines, monthly reports

---

## 🧱 THE THREE CORE FUNCTIONS

SQLite gives you three simple functions that return strings in ISO‑8601 format:

| Function | Output example |
|----------|----------------|
| `date()` | `'2026-07-12'` |
| `time()` | `'14:30:00'` |
| `datetime()` | `'2026-07-12 14:30:00'` |

All accept modifiers to shift time forward or backward:

```sql
SELECT date('now');                     -- today
SELECT date('now', '+7 days');          -- one week from now
SELECT date('now', '-1 month');         -- one month ago
SELECT datetime('now', 'start of month'); -- first day of current month
```

---

## 🧱 STRFTIME – POWERFUL FORMATTING

`strftime(format, datetime_string)` converts a date/time value into any format you need. Common placeholders:

| Placeholder | Meaning |
|-------------|---------|
| `%Y` | 4‑digit year |
| `%m` | 2‑digit month |
| `%d` | 2‑digit day |
| `%H` | Hour (00–23) |
| `%M` | Minute (00–59) |
| `%S` | Second (00–59) |
| `%w` | Day of week (0=Sunday) |
| `%j` | Day of year (001‑366) |

```sql
SELECT strftime('%Y-%m-%d', 'now') AS today;
SELECT strftime('%H:%M', 'now') AS current_time;
SELECT strftime('%A, %B %d, %Y', 'now') AS formatted;
```

---

## 🧱 DATE ARITHMETIC

Compute age, deadline, or overdue status:

```sql
-- Age in years
SELECT (strftime('%Y','now') - strftime('%Y', birth_date)) AS age FROM citizens;

-- Days until deadline
SELECT julianday(deadline) - julianday('now') AS days_left FROM tasks;

-- Shipments overdue
SELECT tracking_id FROM shipments
WHERE julianday('now') > julianday(due_date);
```

> 💡 **INSIGHT:** `julianday()` returns a fractional day count, ideal for precise date math. It's the only way to get exact differences between dates.

> ⚠️ **WARNING:** SQLite date functions return TEXT, not a native date type. When ordering by date, the ISO‑8601 format (`YYYY-MM-DD`) sorts correctly alphabetically. But for arithmetic, use `julianday()` or `strftime('%s')`.

---

## 💡 Real‑world Usage

**Banking – transactions this month**
```sql
SELECT COUNT(*) FROM transactions
WHERE strftime('%Y-%m', transaction_date) = strftime('%Y-%m', 'now');
```

**E‑commerce – products added in the last 30 days**
```sql
SELECT product_name FROM products
WHERE added_date >= date('now', '-30 days');
```

**Logistics – deliveries scheduled for today**
```sql
SELECT tracking_id FROM shipments
WHERE date(delivery_date) = date('now');
```

**HR – employees hired this year**
```sql
SELECT name FROM employees
WHERE strftime('%Y', hire_date) = strftime('%Y', 'now');
```

**Companion – memories from the last 7 days**
```sql
SELECT content FROM memories
WHERE created_at >= datetime('now', '-7 days');
```

---

## 🔍 Practice Preview
You will query date‑based business reports using SQLite’s date functions.

| Level | Task |
|-------|------|
| Easy | Select today’s date using `date('now')`. |
| Medium | Count how many soldiers were registered this month using `strftime`. |
| Hard | List all shipments overdue by comparing `due_date` with today’s date. |

Run the coach:
```bash
python ii_Practice_Sheets/L18_Date_Time_Functions_date_time_strftime.py
```

---

## 📌 Key Takeaway
- `date()`, `time()`, `datetime()` give you the current moment or compute offsets.
- `strftime()` formats dates/times into any representation you need.
- Date arithmetic powers reports, deadlines, and age calculations.
- Always use ISO‑8601 strings for reliable sorting and comparison.

*For Emperor.*