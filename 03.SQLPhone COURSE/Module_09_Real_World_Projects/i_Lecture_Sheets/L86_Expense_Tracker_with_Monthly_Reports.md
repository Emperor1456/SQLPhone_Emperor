# 📘 SQLPhone Emperor v3.0 · Module 9
# 📖 L86 – Expense Tracker with Monthly Reports

---

## 🎯 OBJECTIVE — What You Will Master

> Build a personal finance database that categorizes expenses and produces monthly, category‑level, and period‑over‑period reports — the exact engine behind budgeting apps like Mint, YNAB, and every corporate expense system.

- 🧱 **Tables** – expenses, categories, payment methods
- 🧠 **Date grouping** – `strftime` for month, quarter, and year
- 🧪 **Advanced reports** – category breakdown, month‑over‑month variance, running totals
- ⚡ **Real‑world** – personal budgeting, startup burn rate, departmental budgets

---

## 🧱 THE IMPERIAL FINANCE TRACKER – BUSINESS REQUIREMENT

The Emperor’s treasury must log every expense with a category, amount, date, and optional payment method. At the end of each month, the treasury needs:
- Total spending
- Spending by category
- Month‑over‑month change (variance)
- A running total of spending across the year

---

## 🧱 SCHEMA

```sql
CREATE TABLE categories (
    cat_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE expenses (
    exp_id INTEGER PRIMARY KEY,
    amount REAL CHECK(amount > 0),
    cat_id INTEGER,
    description TEXT,
    exp_date TEXT DEFAULT (date('now')),
    FOREIGN KEY (cat_id) REFERENCES categories(cat_id)
);
```

---

## 🧱 SEED DATA

```sql
INSERT INTO categories VALUES (1, 'Food'), (2, 'Transport'), (3, 'Entertainment');
INSERT INTO expenses (amount, cat_id, description, exp_date) VALUES
(15.50, 1, 'Lunch', '2026-07-01'),
(30.00, 2, 'Bus pass', '2026-07-02'),
(12.00, 1, 'Snacks', '2026-08-01'),
(45.00, 3, 'Cinema', '2026-08-05'),
(8.00, 1, 'Breakfast', '2026-08-10');
```

---

## 🧱 KEY QUERIES

**① Monthly total spending**
```sql
SELECT strftime('%Y-%m', exp_date) AS month,
       SUM(amount) AS total_spent
FROM expenses
GROUP BY month
ORDER BY month;
```

**② Category breakdown for the current month**
```sql
SELECT c.name,
       COALESCE(SUM(e.amount), 0) AS total
FROM categories c
LEFT JOIN expenses e ON c.cat_id = e.cat_id
   AND strftime('%Y-%m', e.exp_date) = strftime('%Y-%m', 'now')
GROUP BY c.cat_id;
```

**③ Month‑over‑month variance**
```sql
WITH monthly AS (
    SELECT strftime('%Y-%m', exp_date) AS month,
           SUM(amount) AS spent
    FROM expenses
    GROUP BY month
)
SELECT month,
       spent,
       LAG(spent) OVER (ORDER BY month) AS prev_month,
       ROUND(spent - LAG(spent) OVER (ORDER BY month), 2) AS change
FROM monthly;
```

**④ Running total within each year**
```sql
SELECT exp_date,
       amount,
       SUM(amount) OVER (PARTITION BY strftime('%Y', exp_date)
                         ORDER BY exp_date) AS running_total
FROM expenses
ORDER BY exp_date;
```

**⑤ Top 3 spending categories all time**
```sql
SELECT c.name, SUM(e.amount) AS total
FROM expenses e
JOIN categories c ON e.cat_id = c.cat_id
GROUP BY c.cat_id
ORDER BY total DESC
LIMIT 3;
```

> 💡 **INSIGHT:** `LAG` and `SUM() OVER` are window functions that avoid complex self‑joins. They are available in SQLite 3.25+.

> ⚠️ **WARNING:** Always use `COALESCE` when LEFT JOINing categories, otherwise uncategorized months may show `NULL` instead of `0`.

---

## 💡 Real‑world Usage

- Personal finance apps (Mint, YNAB)
- Startup burn rate dashboards
- Corporate departmental expense tracking
- Grant budget monitoring for non‑profits

---

## 🔍 Practice Preview
You will build an expense tracker with advanced reporting.

| Level | Task |
|-------|------|
| Easy | Create the tables and seed data for 3 categories and 5 expenses. |
| Medium | Write a query that shows total spending per month. |
| Hard | Compute month‑over‑month variance and the running total for the year. |

Run the coach:
```bash
python ii_Practice_Sheets/L86_Expense_Tracker_with_Monthly_Reports.py
```

---

## 📌 Key Takeaway
- `strftime` groups by any time period.
- Window functions like `LAG` and `SUM() OVER` enable powerful trend analysis without subqueries.
- `LEFT JOIN` with `COALESCE` ensures complete category lists even when no expenses exist in a period.
- This schema is the heart of every financial dashboard.

*For Emperor.*