# 📘 SQLPhone Emperor · SQL Module 08
# 📖 L‑70 – Export to CSV

## 🎯 OBJECTIVE
Export query results to CSV files for sharing or
analysis in other tools.

## 🧱 BRICK 1 – Using Dot‑Commands
In the SQLite CLI, set output mode and file:
```
sqlite> .headers on
sqlite> .mode csv
sqlite> .output report.csv
sqlite> SELECT * FROM employees;
sqlite> .output stdout   (to return to screen)
```
The file `report.csv` now contains the query result.

## 🧱 BRICK 2 – Export via Python
Using the `csv` module:
```python
import sqlite3, csv
conn = sqlite3.connect('mydb.db')
cur = conn.cursor()
cur.execute("SELECT * FROM employees")
with open('export.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([desc[0] for desc in cur.description])  # headers
    writer.writerows(cur.fetchall())
```

You can also use `.system` in CLI to run Python scripts.

## 💡 Real‑world Usage
- Share data with non‑technical colleagues.
- Import into spreadsheet applications.
- Back up query results.

## 📌 Key Takeaway
CSV is the universal data interchange format.
Dot‑commands are quick; Python gives full control.
Always include headers for clarity.

*Data is only valuable when it can be shared.*