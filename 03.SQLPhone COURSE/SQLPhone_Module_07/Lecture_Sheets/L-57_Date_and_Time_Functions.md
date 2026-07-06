# 📘 SQLPhone Emperor · SQL Module 07
# 📖 L‑57 – Date and Time Functions

## 🎯 OBJECTIVE
Use SQLite’s built‑in date/time functions to handle
temporal data efficiently.

## 🧱 BRICK 1 – Core Functions
SQLite provides three main functions:
- `date()` – returns the date in `YYYY-MM-DD`.
- `time()` – returns the time in `HH:MM:SS`.
- `datetime()` – returns `YYYY-MM-DD HH:MM:SS`.

All accept a time‑string argument and optional modifiers:
```sql
SELECT date('now');          -- current date
SELECT time('now');          -- current time
SELECT datetime('now');      -- current datetime
```

## 🧱 BRICK 2 – Modifiers
Modifiers adjust the value:
- `'+1 day'`, `'-1 month'`, `'+3 hours'`, etc.
- `'start of month'`, `'start of year'`
- `'weekday 0'` (Sunday of current week)

```sql
SELECT date('now', '+7 days');
SELECT datetime('now', 'start of month');
```

## 💡 Real‑world Usage
- Calculate due dates.
- Filter records for “last 30 days”.
- Schedule recurring events.

## 📌 Key Takeaway
`date()`, `time()`, `datetime()` plus modifiers
give you full control over temporal logic.
Always store dates in ISO‑8601 format.

*Time is data – learn to manipulate it.*