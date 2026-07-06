#!/usr/bin/env python3
"""
Fix and complete the Review_Sheets and Debugging_Sheets for all modules.
"""

import os

BASE = "03.SQLPhone COURSE"

# 1. Ensure Review_Sheets exist in Module 01
mod01_review = f"{BASE}/SQLPhone_Module_01/Review_Sheets"
os.makedirs(mod01_review, exist_ok=True)

precheck_content = """# 🔍 Pre‑Course Review – Module 01 Readiness Check

Before diving into Module 01, ensure you have:
- Termux installed with SQLite (`sqlite3 --version` works)
- Acode editor ready with storage permission
- A basic understanding of what a database and a table are

## 🧪 Quick Task (no engine)
1. Open Termux and type:
   ```bash
   sqlite3 test.db
   ```
2. Inside the SQLite prompt, create any table with at least two columns.
3. Insert one row.
4. Run `SELECT * FROM your_table;`
5. Exit with `.quit`

If you can do that without errors, you're ready for Module 01.  
If not, revisit the **Getting Started** guide in `01.SQLPhone PLUGIN/`.
"""

with open(f"{mod01_review}/Module_00_PreCheck.md", "w") as f:
    f.write(precheck_content)

# 2. Add two extra debugging files per module (if not existing)
for mod in range(1, 13):
    mod_str = f"{mod:02d}"
    debug_folder = f"{BASE}/SQLPhone_Module_{mod_str}/Debugging_Sheets"
    os.makedirs(debug_folder, exist_ok=True)
    
    file2 = f"{debug_folder}/L-{mod_str}_Broken_2.sql"
    if not os.path.exists(file2):
        with open(file2, "w") as f:
            f.write("""-- 🐛 BROKEN QUERY 2 – Common Mistake
-- This query tries to list all products with a price above average,
-- but the logic is flipped and the alias is misused.

-- Setup (run this first)
-- CREATE TABLE products (name TEXT, price REAL);
-- INSERT INTO products VALUES ('A',10),('B',30),('C',20);

-- Broken query:
SELECT name, price
FROM products
WHERE price < (SELECT AVG(price) FROM products);   -- ❌ uses < instead of >

-- Also, the alias 'avg_price' is defined but not used correctly.
-- Fix the comparison operator and remove the unused alias.
""")
    
    file3 = f"{debug_folder}/L-{mod_str}_Broken_3.sql"
    if not os.path.exists(file3):
        with open(file3, "w") as f:
            f.write("""-- 🐛 BROKEN QUERY 3 – Multiple Issues
-- This script is meant to create two tables with a foreign key,
-- insert data, and then perform a JOIN. It fails due to:
--   1. Missing PRIMARY KEY in the referenced table.
--   2. A typo in the JOIN condition.
--   3. A missing semicolon after the INSERT.

-- Broken script:
CREATE TABLE departments (
    id INTEGER,
    name TEXT
);

CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departments(id)
);

INSERT INTO employees VALUES (1, 'Alice', 1)

SELECT e.name, d.name
FROM employees e
JOIN departments d ON e.dept_id = d.id;   -- ❌ typo: d.id instead of d.id?
-- Fix all three issues to make the script run.
""")

print("✅ Structure fixed: Review_Sheets added to Module 01, and each module now has 3 debugging files.")
