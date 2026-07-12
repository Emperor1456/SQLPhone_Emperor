# 📘 SQLPhone Emperor v3.0 · Module 5
# 📖 L49 – Module Practice: Cohort Analysis

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll apply subqueries, CTEs, and correlated logic to perform a real‑world cohort analysis — the exact same technique used by startups to track user retention and growth.

- 🧱 **Cohort definition** – group users by their first activity month
- 🧠 **Retention calculation** – what fraction of each cohort returned in subsequent months
- 🧪 **Combining subqueries and CTEs** – the full analytical pipeline
- ⚡ **Business insight** – which cohorts are sticking, which are churning
- 🧰 **Real‑world deliverable** – a retention matrix ready for a CEO dashboard

---

## 🧱 WHAT IS COHORT ANALYSIS?

A cohort is a group of users who share a common starting event — for example, all soldiers first deployed in January 2026. Cohort analysis tracks these groups over time to measure retention: how many from each cohort are still active in months 1, 2, 3, and beyond.

This is the same technique used by:
- SaaS companies tracking monthly active users
- E‑commerce sites measuring repeat purchase rates
- Educational platforms monitoring student engagement
- The Imperial Army tracking soldier deployment frequency

---

## 🧱 THE IMPERIAL COHORT SCENARIO

The Imperial Army tracks soldier deployments. Each deployment has a `soldier_id` and `deployment_date`. A cohort is defined as soldiers first deployed in the same month.

```sql
CREATE TABLE deployments (
    deployment_id INTEGER PRIMARY KEY,
    soldier_id INTEGER NOT NULL,
    deployment_date TEXT NOT NULL
);
```

**Seed data:**
```sql
INSERT INTO deployments VALUES (1, 1, '2026-01-15');
INSERT INTO deployments VALUES (2, 2, '2026-01-20');
INSERT INTO deployments VALUES (3, 1, '2026-02-10');
INSERT INTO deployments VALUES (4, 3, '2026-02-05');
INSERT INTO deployments VALUES (5, 2, '2026-03-01');
INSERT INTO deployments VALUES (6, 1, '2026-03-15');
INSERT INTO deployments VALUES (7, 3, '2026-03-20');
INSERT INTO deployments VALUES (8, 4, '2026-03-01');
```

---

## 🧱 STEP‑BY‑STEP COHORT ANALYSIS

**Step 1: Identify each soldier's cohort month (first deployment)**
```sql
SELECT soldier_id,
       MIN(strftime('%Y-%m', deployment_date)) AS cohort_month
FROM deployments
GROUP BY soldier_id;
```

**Step 2: List every month a soldier was active**
```sql
SELECT DISTINCT soldier_id,
       strftime('%Y-%m', deployment_date) AS activity_month
FROM deployments;
```

**Step 3: Join cohort to activity, compute retention**
```sql
WITH first_deployments AS (
    SELECT soldier_id,
           MIN(strftime('%Y-%m', deployment_date)) AS cohort_month
    FROM deployments
    GROUP BY soldier_id
),
monthly_activity AS (
    SELECT DISTINCT soldier_id,
           strftime('%Y-%m', deployment_date) AS activity_month
    FROM deployments
)
SELECT
    fd.cohort_month,
    COUNT(DISTINCT fd.soldier_id) AS cohort_size,
    ma.activity_month,
    COUNT(DISTINCT ma.soldier_id) AS active_in_month,
    ROUND(100.0 * COUNT(DISTINCT ma.soldier_id) /
          COUNT(DISTINCT fd.soldier_id), 1) AS retention_pct
FROM first_deployments fd
LEFT JOIN monthly_activity ma
    ON fd.soldier_id = ma.soldier_id
   AND ma.activity_month >= fd.cohort_month
GROUP BY fd.cohort_month, ma.activity_month
ORDER BY fd.cohort_month, ma.activity_month;
```

The result shows, for each cohort, what percentage of soldiers remained active in each subsequent month.

---

## 🧱 READING THE COHORT TABLE

A typical output:

| cohort_month | cohort_size | activity_month | active_in_month | retention_pct |
|-------------|-------------|----------------|-----------------|---------------|
| 2026-01 | 2 | 2026-01 | 2 | 100.0 |
| 2026-01 | 2 | 2026-02 | 1 | 50.0 |
| 2026-01 | 2 | 2026-03 | 1 | 50.0 |
| 2026-02 | 2 | 2026-02 | 2 | 100.0 |
| 2026-02 | 2 | 2026-03 | 1 | 50.0 |
| 2026-03 | 2 | 2026-03 | 2 | 100.0 |

This tells you:
- The January cohort (2 soldiers) had 50% retention by month 2.
- The February cohort (2 soldiers) had 50% retention by month 1.
- The March cohort is brand new, so 100% are active in month 0.

> 💡 **INSIGHT:** The `LEFT JOIN` ensures we see all cohorts, even if they have zero activity in a given month. The `LEFT JOIN` condition `ma.activity_month >= fd.cohort_month` ensures we only count activity after the cohort's formation.

> ⚠️ **WARNING:** This query uses `COUNT(DISTINCT)` heavily. On very large datasets, consider materializing intermediate results into summary tables for performance.

---

## 💡 Real‑world Usage

**Banking – customer retention by account opening month**
**E‑commerce – repeat purchase rate by first order month**
**Logistics – carrier retention by first contract month**
**HR – employee retention by hire month**
**Companion – user engagement by signup cohort**

---

## 🔍 Practice Preview
You will perform a cohort analysis on the Imperial Army’s deployment data.

| Level | Task |
|-------|------|
| Easy | Compute each soldier’s cohort month (first deployment). |
| Medium | Count how many soldiers from each cohort were active in each subsequent month. |
| Hard | Calculate the retention percentage for each cohort over time and present it as a matrix. |

Run the coach:
```bash
python ii_Practice_Sheets/L49_Module_Practice_Cohort_Analysis.py
```

---

## 📌 Key Takeaway
- Cohort analysis tracks groups over time — fundamental to growth analytics.
- CTEs break the problem into manageable, testable steps.
- The pattern: first occurrence → monthly activity → retention rate.
- This is a CEO‑level deliverable, and now you can build it.

*For Emperor.*