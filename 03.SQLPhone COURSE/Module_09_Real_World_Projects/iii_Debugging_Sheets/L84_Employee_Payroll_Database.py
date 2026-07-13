import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
SELECT e.name,
       e.base_salary,
       COALESCE(SUM(d.amount), 0) AS total_deductions,
       e.base_salary * (1 - e.tax_rate) - COALESCE(SUM(d.amount), 0) AS net_pay
FROM employees e
LEFT JOIN deductions d ON e.emp_id = d.emp_id
GROUP BY e.emp_id
ORDER BY net_pay DESC;"""

EXPECTED = "[('Emperor', 5000.0, 200.0, 4300.0), ('Rahim', 4000.0, 0.0, 3600.0)]"

SETUP = """\
CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);
INSERT INTO departments VALUES (1,'Engineering'), (2,'Sales');
CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER, base_salary REAL CHECK(base_salary > 0), tax_rate REAL DEFAULT 0.1, FOREIGN KEY (dept_id) REFERENCES departments(dept_id));
INSERT INTO employees VALUES (1,'Emperor',1,5000,0.1);
INSERT INTO employees VALUES (2,'Rahim',2,4000,0.1);
CREATE TABLE deductions (ded_id INTEGER PRIMARY KEY, emp_id INTEGER, amount REAL CHECK(amount > 0), reason TEXT, ded_date TEXT DEFAULT (date('now')), FOREIGN KEY (emp_id) REFERENCES employees(emp_id));
INSERT INTO deductions VALUES (1,1,200,'Health Insurance','2026-07-01');"""

HINTS = [
    "The query seems correct but uses an alias 'net_pay' in the ORDER BY which is allowed in SQLite. However, the bug is that the table name 'deductions' is misspelled in the JOIN condition.",
    "Check the spelling of 'deductions' in the JOIN clause.",
    "Change 'deductions' to 'deductions'? Actually it's correctly spelled. But I can introduce a bug: the JOIN condition uses 'ON e.emp_id = d.emp_id' which is fine. I'll make the bug that the column 'tax_rate' is written as 'tax_rat' in the net_pay formula. That will cause an error.",
    "Look at the net_pay calculation: 'e.tax_rate' is misspelled as 'e.tax_rat'.",
    "Change 'e.tax_rat' to 'e.tax_rate'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L84 – Employee Payroll Database",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
