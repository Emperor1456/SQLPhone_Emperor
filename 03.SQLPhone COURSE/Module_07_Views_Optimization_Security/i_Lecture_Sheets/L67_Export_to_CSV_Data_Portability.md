# 📘 SQLPhone Emperor v3.0 · Module 7
# 📖 L67 – Export to CSV – Data Portability

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll export query results to CSV — the universal format for spreadsheets, data analysis, and system integration. Every tool from Excel to Python pandas speaks CSV.

- 🧱 **`.mode csv`** – set output mode to CSV
- 🧠 **`.output`** – redirect results to a file
- 🧪 **`.headers on`** – include column names
- ⚡ **Python export** – using the `csv` module for full control
- 🧰 **Automation** – scheduled exports for reporting

---

## 🧱 EXPORTING FROM THE SQLITE SHELL

```bash
sqlite3 empire.db
sqlite> .headers on
sqlite> .mode csv
sqlite> .output soldiers.csv
sqlite> SELECT * FROM soldiers;
sqlite> .output stdout   # return to screen
sqlite> .quit
```

The file `soldiers.csv` now contains the query results in CSV format.

**Export a filtered subset:**
```bash
sqlite3 empire.db
sqlite> .headers on
sqlite> .mode csv
sqlite> .output generals.csv
sqlite> SELECT name, salary FROM soldiers WHERE rank = 'General';
sqlite> .quit
```

---

## 🧱 EXPORTING IN PYTHON

Using the `csv` module gives you complete control over the output:

```python
import sqlite3
import csv

conn = sqlite3.connect("empire.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM soldiers WHERE status = 'active'")

with open("active_soldiers.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # Write header
    writer.writerow([desc[0] for desc in cursor.description])
    # Write rows
    writer.writerows(cursor.fetchall())

conn.close()
print("Export complete.")
```

---

## 🧱 EXPORT WITH PANDAS (DATA SCIENCE WORKFLOW)

If you have pandas installed, exporting is even simpler and opens the door to data analysis:

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect("empire.db")
df = pd.read_sql("SELECT * FROM soldiers", conn)
df.to_csv("soldiers_export.csv", index=False)
conn.close()
```

Pandas handles headers, encoding, and data type conversion automatically.

---

## 🧱 SCHEDULED EXPORTS

Combine with Python’s `datetime` for automated monthly reports:

```python
from datetime import datetime

def export_monthly_sales():
    month = datetime.now().strftime("%Y-%m")
    conn = sqlite3.connect("empire.db")
    df = pd.read_sql(f"SELECT * FROM sales WHERE strftime('%Y-%m', sale_date) = '{month}'", conn)
    df.to_csv(f"sales_{month}.csv", index=False)
    conn.close()
```

> 💡 **INSIGHT:** CSV is the lowest common denominator for data exchange. Every analytics tool (Excel, Google Sheets, Python pandas, R, Tableau) reads CSV. Exporting to CSV makes your SQLite data universally accessible.

> ⚠️ **WARNING:** CSV does not preserve data types – everything becomes a string. For complex exports (dates, NULLs), consider using JSON or direct database replication.

---

## 💡 Real‑world Usage

**Banking – export monthly statement**
```sql
.mode csv
.output statement.csv
SELECT * FROM transactions WHERE account_id = 101 AND strftime('%Y-%m', date) = '2026-07';
```

**E‑commerce – export product catalog for supplier**
**Logistics – export delivery report for partner**
**HR – export employee directory for payroll**
**Companion – export conversation history for review**

---

## 🔍 Practice Preview
You will export Imperial Army data to CSV.

| Level | Task |
|-------|------|
| Easy | Export all soldiers to a CSV file using the shell. |
| Medium | Export active soldiers only, with headers and proper formatting. |
| Hard | Write a Python script that exports any SQL query result to a CSV file with a timestamped filename. |

Run the coach:
```bash
python ii_Practice_Sheets/L67_Export_to_CSV_Data_Portability.py
```

---

## 📌 Key Takeaway
- `.mode csv` + `.output` exports data from the SQLite shell.
- Python’s `csv.writer` gives programmatic control; pandas makes it effortless.
- CSV makes your data compatible with every analytics platform.
- Scheduled exports automate reporting.

*For Emperor.*