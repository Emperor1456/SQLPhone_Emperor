# 📘 SQLPhone Emperor v3.0 · Module 5
# 📖 L50 – Module 5 Capstone: Employee Performance Tracker

---

## 🎯 OBJECTIVE — What You Will Master

> Build a complete employee performance database that integrates every Module‑5 skill — subqueries, CTEs, correlated subqueries, and recursive hierarchy traversal — into a single, production‑ready system.

- 🧱 **Schema design** – employees, departments, evaluations, goals
- 🧠 **Correlated subqueries** – per‑employee metrics vs department averages
- 🧪 **CTEs** – modular score calculations and ranking
- ⚡ **Recursive CTE** – org chart with performance overlay
- 🧰 **Real‑world deliverable** – the exact system used by HR departments worldwide

---

## 🧱 THE IMPERIAL PERFORMANCE SYSTEM – BUSINESS REQUIREMENT

The Imperial Army needs to track every soldier’s performance evaluations, compare them against department averages, rank soldiers within their units, and display the full chain of command with performance scores.

**Tables:**
- `departments` – unit names
- `soldiers` – personnel with department and manager references
- `evaluations` – periodic performance scores (1‑10)
- `goals` – individual performance targets with completion status

---

## 🧱 SCHEMA

```sql
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT NOT NULL
);

CREATE TABLE soldiers (
    soldier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dept_id INTEGER,
    manager_id INTEGER,
    rank TEXT,
    hire_date TEXT DEFAULT (date('now')),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
    FOREIGN KEY (manager_id) REFERENCES soldiers(soldier_id)
);

CREATE TABLE evaluations (
    eval_id INTEGER PRIMARY KEY,
    soldier_id INTEGER NOT NULL,
    eval_date TEXT NOT NULL,
    score INTEGER CHECK(score BETWEEN 1 AND 10),
    reviewer_id INTEGER,
    FOREIGN KEY (soldier_id) REFERENCES soldiers(soldier_id),
    FOREIGN KEY (reviewer_id) REFERENCES soldiers(soldier_id)
);

CREATE TABLE goals (
    goal_id INTEGER PRIMARY KEY,
    soldier_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    target_date TEXT,
    completed INTEGER DEFAULT 0 CHECK(completed IN (0,1)),
    FOREIGN KEY (soldier_id) REFERENCES soldiers(soldier_id)
);
```

---

## 🧱 SEED DATA

```sql
INSERT INTO departments VALUES (1, 'Infantry'), (2, 'Cavalry'), (3, 'Intelligence');

INSERT INTO soldiers VALUES (1, 'Emperor', 1, NULL, 'General', '2025-01-01');
INSERT INTO soldiers VALUES (2, 'Rahim', 1, 1, 'Colonel', '2025-03-15');
INSERT INTO soldiers VALUES (3, 'Karim', 1, 2, 'Major', '2025-06-01');
INSERT INTO soldiers VALUES (4, 'Ali', 2, 1, 'Colonel', '2025-04-01');
INSERT INTO soldiers VALUES (5, 'Hasan', 2, 4, 'Private', '2026-01-10');
INSERT INTO soldiers VALUES (6, 'Fatima', 3, 1, 'Major', '2025-07-01');

INSERT INTO evaluations VALUES (1, 1, '2026-01-15', 9, 1);
INSERT INTO evaluations VALUES (2, 2, '2026-01-15', 7, 1);
INSERT INTO evaluations VALUES (3, 3, '2026-01-15', 6, 2);
INSERT INTO evaluations VALUES (4, 1, '2026-04-15', 8, 1);
INSERT INTO evaluations VALUES (5, 2, '2026-04-15', 8, 1);
INSERT INTO evaluations VALUES (6, 4, '2026-04-15', 9, 1);
INSERT INTO evaluations VALUES (7, 5, '2026-04-15', 5, 4);
INSERT INTO evaluations VALUES (8, 6, '2026-04-15', 7, 1);

INSERT INTO goals VALUES (1, 2, 'Complete leadership training', '2026-06-30', 1);
INSERT INTO goals VALUES (2, 2, 'Recruit 10 soldiers', '2026-12-31', 0);
INSERT INTO goals VALUES (3, 3, 'Improve tactical score to 8', '2026-09-30', 0);
INSERT INTO goals VALUES (4, 5, 'Complete basic training', '2026-03-31', 1);
```

---

## 🧱 KEY REPORTING QUERIES

**① Employee average score with department average (correlated subquery)**
```sql
SELECT s.name,
       AVG(e.score) AS avg_score,
       (SELECT AVG(e2.score)
        FROM evaluations e2
        JOIN soldiers s2 ON e2.soldier_id = s2.soldier_id
        WHERE s2.dept_id = s.dept_id) AS dept_avg
FROM soldiers s
JOIN evaluations e ON s.soldier_id = e.soldier_id
GROUP BY s.soldier_id;
```

**② Top performers ranking (CTE)**
```sql
WITH soldier_scores AS (
    SELECT soldier_id, AVG(score) AS avg_score
    FROM evaluations
    GROUP BY soldier_id
)
SELECT s.name, ss.avg_score,
       RANK() OVER (ORDER BY ss.avg_score DESC) AS rank
FROM soldiers s
JOIN soldier_scores ss ON s.soldier_id = ss.soldier_id;
```

**③ Goal completion rate per soldier (correlated subquery)**
```sql
SELECT s.name,
       COUNT(g.goal_id) AS total_goals,
       SUM(g.completed) AS completed,
       ROUND(100.0 * SUM(g.completed) / COUNT(g.goal_id), 1) AS completion_pct
FROM soldiers s
LEFT JOIN goals g ON s.soldier_id = g.soldier_id
GROUP BY s.soldier_id;
```

**④ Org chart with average performance scores (recursive CTE)**
```sql
WITH RECURSIVE org AS (
    SELECT soldier_id, name, manager_id, 1 AS level
    FROM soldiers WHERE manager_id IS NULL

    UNION ALL

    SELECT s.soldier_id, s.name, s.manager_id, o.level + 1
    FROM soldiers s
    JOIN org o ON s.manager_id = o.soldier_id
)
SELECT o.name, o.level,
       (SELECT AVG(score) FROM evaluations WHERE soldier_id = o.soldier_id) AS avg_score
FROM org o
ORDER BY o.level, o.name;
```

**⑤ Soldiers performing above department average (correlated EXISTS)**
```sql
SELECT s.name, AVG(e.score) AS avg_score
FROM soldiers s
JOIN evaluations e ON s.soldier_id = e.soldier_id
GROUP BY s.soldier_id
HAVING AVG(e.score) > (
    SELECT AVG(e2.score)
    FROM evaluations e2
    JOIN soldiers s2 ON e2.soldier_id = s2.soldier_id
    WHERE s2.dept_id = s.dept_id
);
```

**⑥ Low performers with overdue goals (CTE + subquery)**
```sql
WITH low_performers AS (
    SELECT soldier_id, AVG(score) AS avg_score
    FROM evaluations
    GROUP BY soldier_id
    HAVING AVG(score) < 6
)
SELECT s.name, lp.avg_score, g.description, g.target_date
FROM low_performers lp
JOIN soldiers s ON lp.soldier_id = s.soldier_id
JOIN goals g ON s.soldier_id = g.soldier_id
WHERE g.completed = 0
  AND g.target_date < date('now');
```

---

## 💡 Real‑world Usage

This system directly mirrors:
- Corporate performance management (Workday, BambooHR)
- Military personnel evaluation systems
- Sales team performance dashboards
- Academic student tracking systems

---

## 🔍 Practice Preview
You will build the Imperial Performance System and answer HR questions.

| Level | Task |
|-------|------|
| Easy | Create all four tables with constraints and seed data. |
| Medium | Show each soldier’s average score alongside their department’s average using a correlated subquery. |
| Hard | Build the org chart with each soldier’s average evaluation score using a recursive CTE, and identify low performers with overdue goals. |

Run the coach:
```bash
python ii_Practice_Sheets/L50_Module_5_Capstone_Employee_Performance_Tracker.py
```

---

## 📌 Key Takeaway
- Correlated subqueries enable per‑row comparisons against group metrics.
- CTEs modularize complex score calculations and rankings.
- Recursive CTEs overlay performance data onto hierarchical org structures.
- This capstone proves you can design, query, and analyze a complete HR analytics system.

*For Emperor.*