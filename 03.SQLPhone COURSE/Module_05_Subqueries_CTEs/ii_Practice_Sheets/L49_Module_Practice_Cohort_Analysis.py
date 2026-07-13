import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📅  Cohort Month – First Deployment\n\n"
        "Create a table `deployments` with columns:\n"
        "  • id INTEGER, soldier_id INTEGER, deployment_date TEXT.\n"
        "Insert 8 rows with varied soldiers and dates.\n"
        "Write a query that returns each soldier's id and\n"
        "their cohort month (the month of their FIRST deployment).\n"
        "Use MIN(strftime('%Y-%m', deployment_date)).\n"
        "Group by soldier_id.\n"
        "Sort by soldier_id.\n\n"
        "Expected output:\n[(1,'2026-01'), (2,'2026-01'), (3,'2026-02'), (4,'2026-03')]"
    ),
    expected_output="[(1, '2026-01'), (2, '2026-01'), (3, '2026-02'), (4, '2026-03')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE deployments (id INTEGER, soldier_id INTEGER, deployment_date TEXT);",
        "INSERT INTO deployments VALUES (1,1,'2026-01-15'), (2,2,'2026-01-20'), (3,1,'2026-02-10'), (4,3,'2026-02-05'), (5,2,'2026-03-01'), (6,1,'2026-03-15'), (7,3,'2026-03-20'), (8,4,'2026-03-01');",
        "SELECT soldier_id, MIN(strftime('%Y-%m', deployment_date)) AS cohort_month FROM deployments GROUP BY soldier_id ORDER BY soldier_id;"
    ]
)

easy2 = Task(
    description=(
        "📊  Cohort Size – Count Soldiers per Cohort\n\n"
        "The same `deployments` table.\n"
        "Write a query that returns each cohort month and\n"
        "the number of soldiers who belong to that cohort\n"
        "(i.e., whose first deployment was that month).\n"
        "Use the previous query as a subquery or CTE.\n"
        "Sort by cohort_month.\n\n"
        "Expected output:\n[('2026-01',2), ('2026-02',1), ('2026-03',1)]"
    ),
    setup_sql=(
        "CREATE TABLE deployments (id INTEGER, soldier_id INTEGER, deployment_date TEXT);"
        "INSERT INTO deployments VALUES (1,1,'2026-01-15'), (2,2,'2026-01-20'), (3,1,'2026-02-10'), (4,3,'2026-02-05'), (5,2,'2026-03-01'), (6,1,'2026-03-15'), (7,3,'2026-03-20'), (8,4,'2026-03-01');"
    ),
    expected_output="[('2026-01', 2), ('2026-02', 1), ('2026-03', 1)]",
    level=Level.EASY,
    hints=[
        "WITH first_deployments AS (SELECT soldier_id, MIN(strftime('%Y-%m', deployment_date)) AS cohort_month FROM deployments GROUP BY soldier_id) SELECT cohort_month, COUNT(*) AS cohort_size FROM first_deployments GROUP BY cohort_month ORDER BY cohort_month;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📈  Monthly Activity – Soldiers Active per Month\n\n"
        "The `deployments` table has 8 rows.\n"
        "Write a query that returns each month (from deployment_date)\n"
        "and the number of DISTINCT soldiers active in that month.\n"
        "Group by month (strftime '%Y-%m').\n"
        "Sort by month.\n\n"
        "Expected output:\n[('2026-01',2), ('2026-02',3), ('2026-03',4)]"
    ),
    setup_sql=(
        "CREATE TABLE deployments (id INTEGER, soldier_id INTEGER, deployment_date TEXT);"
        "INSERT INTO deployments VALUES (1,1,'2026-01-15'), (2,2,'2026-01-20'), (3,1,'2026-02-10'), (4,3,'2026-02-05'), (5,2,'2026-03-01'), (6,1,'2026-03-15'), (7,3,'2026-03-20'), (8,4,'2026-03-01');"
    ),
    expected_output="[('2026-01', 2), ('2026-02', 3), ('2026-03', 4)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT strftime('%Y-%m', deployment_date) AS month, COUNT(DISTINCT soldier_id) AS active_soldiers FROM deployments GROUP BY month ORDER BY month;"
    ]
)

medium2 = Task(
    description=(
        "🔗  Cohort Retention – Active in Next Month\n\n"
        "The `deployments` table has 8 rows.\n"
        "For each cohort month, count how many soldiers from\n"
        "that cohort were active in the month IMMEDIATELY after\n"
        "their cohort month (e.g., Feb for Jan cohort).\n"
        "Use CTEs: first_deployments and a join to deployments\n"
        "where the activity month = cohort_month + 1 month.\n"
        "Hint: use strftime('%Y-%m', deployment_date, '+1 month')\n"
        "to compute the next month.\n"
        "Sort by cohort_month.\n\n"
        "Expected output:\n[('2026-01',2), ('2026-02',2)]"
    ),
    setup_sql=(
        "CREATE TABLE deployments (id INTEGER, soldier_id INTEGER, deployment_date TEXT);"
        "INSERT INTO deployments VALUES (1,1,'2026-01-15'), (2,2,'2026-01-20'), (3,1,'2026-02-10'), (4,3,'2026-02-05'), (5,2,'2026-03-01'), (6,1,'2026-03-15'), (7,3,'2026-03-20'), (8,4,'2026-03-01');"
    ),
    expected_output="[('2026-01', 2), ('2026-02', 2)]",
    level=Level.MEDIUM,
    hints=[
        "WITH first_deployments AS (SELECT soldier_id, MIN(strftime('%Y-%m', deployment_date)) AS cohort_month FROM deployments GROUP BY soldier_id), next_month_activity AS (SELECT DISTINCT fd.soldier_id, fd.cohort_month FROM first_deployments fd JOIN deployments d ON fd.soldier_id = d.soldier_id WHERE strftime('%Y-%m', d.deployment_date) = strftime('%Y-%m', fd.cohort_month || '-01', '+1 month')) SELECT cohort_month, COUNT(*) AS retained FROM next_month_activity GROUP BY cohort_month ORDER BY cohort_month;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Full Cohort Retention Matrix\n\n"
        "The `deployments` table has 8 rows.\n"
        "Write a query that returns, for each cohort month\n"
        "and each activity month (activity_month >= cohort_month):\n"
        "  • cohort_month\n"
        "  • activity_month\n"
        "  • active_count (number of soldiers from that cohort\n"
        "    active in that month)\n"
        "Use CTEs: first_deployments, and a JOIN with deployments\n"
        "to find activity. Group by both months.\n"
        "Sort by cohort_month, then activity_month.\n\n"
        "Expected output:\n[('2026-01','2026-01',2), ('2026-01','2026-02',2), ('2026-01','2026-03',2), ('2026-02','2026-02',2), ('2026-02','2026-03',2), ('2026-03','2026-03',2)]"
    ),
    setup_sql=(
        "CREATE TABLE deployments (id INTEGER, soldier_id INTEGER, deployment_date TEXT);"
        "INSERT INTO deployments VALUES (1,1,'2026-01-15'), (2,2,'2026-01-20'), (3,1,'2026-02-10'), (4,3,'2026-02-05'), (5,2,'2026-03-01'), (6,1,'2026-03-15'), (7,3,'2026-03-20'), (8,4,'2026-03-01');"
    ),
    expected_output="[('2026-01', '2026-01', 2), ('2026-01', '2026-02', 2), ('2026-01', '2026-03', 2), ('2026-02', '2026-02', 2), ('2026-02', '2026-03', 2), ('2026-03', '2026-03', 2)]",
    level=Level.HARD,
    hints=[
        "WITH first_deployments AS (SELECT soldier_id, MIN(strftime('%Y-%m', deployment_date)) AS cohort_month FROM deployments GROUP BY soldier_id), monthly_activity AS (SELECT DISTINCT soldier_id, strftime('%Y-%m', deployment_date) AS activity_month FROM deployments) SELECT fd.cohort_month, ma.activity_month, COUNT(DISTINCT fd.soldier_id) AS active_count FROM first_deployments fd JOIN monthly_activity ma ON fd.soldier_id = ma.soldier_id WHERE ma.activity_month >= fd.cohort_month GROUP BY fd.cohort_month, ma.activity_month ORDER BY fd.cohort_month, ma.activity_month;"
    ]
)

hard2 = Task(
    description=(
        "📊  Retention Percentage – Cohort Analysis\n\n"
        "The `deployments` table has 8 rows.\n"
        "Write a query that returns, for each cohort month\n"
        "and each activity month (activity_month >= cohort_month):\n"
        "  • cohort_month\n"
        "  • cohort_size (initial count)\n"
        "  • activity_month\n"
        "  • active_in_month (count from that cohort)\n"
        "  • retention_pct (ROUND to 1 decimal)\n"
        "Use CTEs for first_deployments and monthly_activity.\n"
        "Compute cohort_size separately and join it.\n"
        "Sort by cohort_month, then activity_month.\n\n"
        "Expected output:\n[('2026-01',2,'2026-01',2,100.0), ('2026-01',2,'2026-02',2,100.0), ('2026-01',2,'2026-03',2,100.0), ('2026-02',2,'2026-02',2,100.0), ('2026-02',2,'2026-03',2,100.0), ('2026-03',2,'2026-03',2,100.0)]"
    ),
    setup_sql=(
        "CREATE TABLE deployments (id INTEGER, soldier_id INTEGER, deployment_date TEXT);"
        "INSERT INTO deployments VALUES (1,1,'2026-01-15'), (2,2,'2026-01-20'), (3,1,'2026-02-10'), (4,3,'2026-02-05'), (5,2,'2026-03-01'), (6,1,'2026-03-15'), (7,3,'2026-03-20'), (8,4,'2026-03-01');"
    ),
    expected_output="[('2026-01', 2, '2026-01', 2, 100.0), ('2026-01', 2, '2026-02', 2, 100.0), ('2026-01', 2, '2026-03', 2, 100.0), ('2026-02', 2, '2026-02', 2, 100.0), ('2026-02', 2, '2026-03', 2, 100.0), ('2026-03', 2, '2026-03', 2, 100.0)]",
    level=Level.HARD,
    hints=[
        "WITH first_deployments AS (SELECT soldier_id, MIN(strftime('%Y-%m', deployment_date)) AS cohort_month FROM deployments GROUP BY soldier_id), cohort_sizes AS (SELECT cohort_month, COUNT(*) AS cohort_size FROM first_deployments GROUP BY cohort_month), monthly_activity AS (SELECT DISTINCT soldier_id, strftime('%Y-%m', deployment_date) AS activity_month FROM deployments) SELECT fd.cohort_month, cs.cohort_size, ma.activity_month, COUNT(DISTINCT fd.soldier_id) AS active_in_month, ROUND(100.0 * COUNT(DISTINCT fd.soldier_id) / cs.cohort_size, 1) AS retention_pct FROM first_deployments fd JOIN monthly_activity ma ON fd.soldier_id = ma.soldier_id JOIN cohort_sizes cs ON fd.cohort_month = cs.cohort_month WHERE ma.activity_month >= fd.cohort_month GROUP BY fd.cohort_month, ma.activity_month ORDER BY fd.cohort_month, ma.activity_month;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L49.json",
        module_name="Module_05_Subqueries_CTEs",
        lesson_name="L49_Module_Practice_Cohort_Analysis"
    )
