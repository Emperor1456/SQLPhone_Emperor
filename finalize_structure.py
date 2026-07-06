#!/usr/bin/env python3
"""
Add Roman numeral folder prefixes and create module‑own review sheets.
"""

import os

BASE = "03.SQLPhone COURSE"

# Roman numerals for the four stages
ROMAN = {0: "i", 1: "ii", 2: "iii", 3: "iv"}

# Template for each module's own review sheet.
REVIEW_TEMPLATE = """# 🔁 Module {mod_num} – Final Review

You have completed the lectures, practice, and debugging challenges.  
Now consolidate your mastery with this final review.

## 🧪 Consolidation Task
Re‑run the **Hard** level of each practice sheet from this module.  
If you can solve them without hints, you truly own the material.

{lesson_list}

## 📌 Key Questions to Ask Yourself
- Can I explain the core concepts of this module to a colleague?
- Can I write the SQL from scratch without referring to notes?
- Do I understand the common mistakes from the debugging challenges?

If yes, mark the Progress Tracker as complete and move on.
"""

# Lesson titles per module (short form)
LESSONS = {
    "01": ["What is SQL?", "Installing SQLite in Termux", "First Database & Dot‑Commands",
           "Data Types in SQLite", "CREATE TABLE", "INSERT INTO", "Basic SELECT",
           "Comments in SQL", "SQL Syntax Rules & Best Practices", "Module Challenge: Imperial Fitness DB"],
    "02": ["SELECT DISTINCT", "WHERE Clause", "AND, OR, NOT", "ORDER BY", "LIMIT and OFFSET",
           "BETWEEN", "IN", "LIKE", "NULL Values", "Aliases (AS)"],
    "03": ["COUNT", "SUM and AVG", "MIN and MAX", "GROUP BY – Single Column",
           "GROUP BY – Multiple Columns", "HAVING", "WHERE, GROUP BY, HAVING", "Aggregation Challenge Set"],
    "04": ["Relationships & Foreign Keys", "INNER JOIN", "LEFT JOIN", "RIGHT JOIN (Simulated)",
           "FULL OUTER JOIN (Simulated)", "Self‑Join", "UNION and UNION ALL",
           "Joining More Than Two Tables", "Join Challenges", "Foreign Key Enforcement"],
    "05": ["Subqueries in WHERE", "Subqueries in SELECT", "IN and NOT IN Subqueries",
           "EXISTS and NOT EXISTS", "ANY and ALL", "Correlated Subqueries",
           "WITH Clause (CTEs)", "Subquery Practice"],
    "06": ["UPDATE – Modifying Rows", "DELETE – Removing Rows", "DROP TABLE",
           "ALTER TABLE", "Constraints Deep Dive", "DEFAULT Values",
           "PRIMARY KEY & Composite Keys", "FOREIGN KEY – Referential Integrity",
           "CREATE INDEX", "AUTOINCREMENT vs INTEGER PRIMARY KEY"],
    "07": ["Date and Time Functions", "strftime()", "Mathematical Functions",
           "String Functions", "Concatenation Operator (||)", "CAST",
           "COALESCE", "NULLIF"],
    "08": ["CASE – Simple and Searched", "CASE in ORDER BY, GROUP BY, WHERE",
           "Views – Create, Query, Drop", "Updatable Views",
           "Materialized Views (Alternatives)", "Export to CSV"],
    "09": ["import sqlite3 – First Connection", "Creating Tables via Python",
           "Parameterized Insert (Anti‑Injection)", "fetchone(), fetchall(), fetchmany()",
           "UPDATE and DELETE with Python", "Executing .sql Files from Python",
           "Database Error Handling", "Reusable Helper Module",
           "Interactive Practice Coach Engine", "Mini‑Project – Contact Book"],
    "10": ["Preventing SQL Injection Deep Dive", "Index Usage Strategy",
           "EXPLAIN QUERY PLAN", "Transactions – BEGIN, COMMIT, ROLLBACK",
           "Backup and Restore", "Schema Design Best Practices"],
    "11": ["Student Management System", "E‑commerce Inventory Tracker",
           "Library Management", "Employee Payroll Database",
           "Blog Database", "Expense Tracker", "Movie Rating System",
           "Custom Project"],
    "12": ["SQLite vs PostgreSQL vs MySQL", "Installing PostgreSQL in Termux",
           "Connecting Python to PostgreSQL", "Roadmap – ORMs, Migrations, Cloud"],
}

# ────────────────────────────────────────────────
# 1. Rename folders inside each module to have Roman numeral prefix
# ────────────────────────────────────────────────
for mod in range(1, 13):
    mod_str = f"{mod:02d}"
    module_dir = f"{BASE}/SQLPhone_Module_{mod_str}"
    if not os.path.isdir(module_dir):
        continue
    # Mapping of old folder names to new
    renames = {
        "Lecture_Sheets": "i_Lecture_Sheets",
        "Practice_Sheets": "ii_Practice_Sheets",
        "Debugging_Sheets": "iii_Debugging_Sheets",
        "Review_Sheets": "iv_Review_Sheets",
    }
    for old_name, new_name in renames.items():
        old_path = os.path.join(module_dir, old_name)
        new_path = os.path.join(module_dir, new_name)
        if os.path.isdir(old_path) and not os.path.exists(new_path):
            os.rename(old_path, new_path)
            print(f"Renamed {old_path} -> {new_path}")

# ────────────────────────────────────────────────
# 2. Create module‑own review sheet inside iv_Review_Sheets (if missing)
# ────────────────────────────────────────────────
for mod_num in LESSONS:
    mod_str = mod_num
    review_dir = f"{BASE}/SQLPhone_Module_{mod_str}/iv_Review_Sheets"
    os.makedirs(review_dir, exist_ok=True)
    review_file = os.path.join(review_dir, f"Module_{mod_str}_Review.md")
    if os.path.exists(review_file):
        print(f"Review file already exists: {review_file} – skipping.")
        continue
    # Build lesson list
    lesson_items = "\n".join(f"- {title}" for title in LESSONS[mod_str])
    content = REVIEW_TEMPLATE.format(mod_num=mod_num, lesson_list=lesson_items)
    with open(review_file, "w") as f:
        f.write(content)
    print(f"Created {review_file}")

print("\n✅ Structure finalised: Roman numeral folders and module‑own review sheets are in place.")
