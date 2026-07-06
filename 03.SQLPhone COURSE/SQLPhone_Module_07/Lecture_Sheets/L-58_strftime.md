# 📘 SQLPhone Emperor · SQL Module 07
# 📖 L‑58 – strftime()

## 🎯 OBJECTIVE
Format dates and times into custom string
representations using `strftime()`.

## 🧱 BRICK 1 – strftime Syntax
`strftime(format, timestring, modifiers...)` returns
a formatted string.

Common format codes:
- `%Y` – year (4 digits)
- `%m` – month (01‑12)
- `%d` – day of month (01‑31)
- `%H` – hour (00‑24)
- `%M` – minute
- `%S` – second
- `%w` – day of week (0=Sun)
- `%j` – day of year (001‑366)

```sql
SELECT strftime('%Y-%m-%d', 'now');
-- 2026-07-06
```

## 🧱 BRICK 2 – Advanced Formatting
Combine format codes with literals:
```sql
SELECT strftime('%d/%m/%Y %H:%M', 'now');
-- 06/07/2026 14:30
```

Extract components for grouping:
```sql
SELECT strftime('%Y-%m', order_date) AS month,
       COUNT(*) FROM orders GROUP BY month;
```

## 💡 Real‑world Usage
- Custom date displays for reports.
- Group by year, month, quarter.
- Generate file names with timestamps.

## 📌 Key Takeaway
`strftime()` is the Swiss Army knife of date formatting.
Memorise the common codes; the rest are a reference away.
Use it for grouping, display, and export.

*Format time to fit your purpose.*