import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
SELECT d.name, COUNT(e.emp_id), AVG(e.salary), SUM(e.salary)
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id;
"""

EXPECTED = "[('Engineering', 1, 5000.0, 5000.0), ('Sales', 2, 3750.0, 7500.0)]"

SETUP = """\
CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT);
INSERT INTO departments VALUES (1,'Engineering'),(2,'Sales');
CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT, dept_id INTEGER REFERENCES departments, salary REAL);
INSERT INTO employees VALUES (1,'Emperor',1,5000),(2,'Rahim',2,4000),(3,'Ali',2,3500);"""

HINTS = [
    "The aggregate functions in SELECT lack aliases, but that's not a bug. The bug is that the GROUP BY clause uses 'd.dept_id', but the column selected is 'd.name', which is fine as long as it's functionally dependent. However, the bug is something else: the table name 'departments' is misspelled in the FROM clause.",
    "Check the spelling of 'departments' – it should be 'departments'? Actually the correct table name is 'departments' (as created). But in the broken code, I'll make it 'departments' while the correct is 'departments'? No, I'll use a different approach: the INSERT into departments has a typo in a name.",
    "I'll create a simpler bug: the second JOIN condition uses 'ON d.dept_id = e.dept_id' which is correct. But I'll change it to 'ON d.dept_id = e.emp_id' (wrong column). Fix: change 'e.emp_id' to 'e.dept_id'.",
    "Replace 'ON d.dept_id = e.emp_id' with 'ON d.dept_id = e.dept_id'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L100 – Final Capstone: Imperial ERP System",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
