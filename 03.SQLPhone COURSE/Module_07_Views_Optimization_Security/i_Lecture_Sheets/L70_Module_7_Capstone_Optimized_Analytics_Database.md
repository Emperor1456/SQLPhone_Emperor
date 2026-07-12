# 📘 SQLPhone Emperor v3.0 · Module 7
# 📖 L70 – Module 7 Capstone: Optimized Analytics Database

---

## 🎯 OBJECTIVE — What You Will Master

> Design and build a complete analytics database that is fast, secure, and maintainable — integrating every Module‑7 concept into one deliverable.

- 🧱 **Schema design** – normalized tables with proper types and constraints
- 🧠 **Views** – materialized and secure reporting views
- 🧪 **Indexes** – strategic single and composite indexes
- ⚡ **Security** – parameterized queries, access control through views
- 🛡️ **Backup** – automated backup strategy
- 🧰 **Export** – CSV export for external analytics tools

---

## 🧱 THE IMPERIAL ANALYTICS SCHEMA

The Imperial Finance division needs to track branches, accounts, and transactions for monthly performance reports.

```sql
CREATE TABLE regions (region_id INTEGER PRIMARY KEY, region_name TEXT UNIQUE);
CREATE TABLE branches (branch_id INTEGER PRIMARY KEY, branch_name TEXT, region_id INTEGER REFERENCES regions);
CREATE TABLE accounts (account_id INTEGER PRIMARY KEY, branch_id INTEGER REFERENCES branches, balance REAL CHECK(balance >= 0));
CREATE TABLE transactions (txn_id INTEGER PRIMARY KEY, account_id INTEGER REFERENCES accounts, amount REAL, txn_date TEXT DEFAULT (date('now')));
```

---

## 🧱 SEED DATA

```sql
INSERT INTO regions VALUES (1, 'North'), (2, 'South');
INSERT INTO branches VALUES (1, 'Dhaka', 1), (2, 'Chittagong', 2);
INSERT INTO accounts VALUES (1, 1, 5000), (2, 2, 3000);
INSERT INTO transactions VALUES (1, 1, 1000, '2026-07-01'), (2, 1, -200, '2026-07-02');
```

---

## 🧱 REPORTING VIEWS

**Branch summary (materialized alternative)**
```sql
CREATE VIEW v_branch_summary AS
SELECT b.branch_name, r.region_name, COUNT(a.account_id) AS accounts, SUM(a.balance) AS deposits
FROM branches b
JOIN regions r ON b.region_id = r.region_id
LEFT JOIN accounts a ON b.branch_id = a.branch_id
GROUP BY b.branch_id;
```

**Monthly transaction volume (for analysts)**
```sql
CREATE VIEW v_monthly_volume AS
SELECT strftime('%Y-%m', txn_date) AS month, SUM(ABS(amount)) AS volume, COUNT(*) AS txns
FROM transactions
GROUP BY month;
```

---

## 🧱 STRATEGIC INDEXES

```sql
CREATE INDEX idx_accounts_branch ON accounts(branch_id);
CREATE INDEX idx_transactions_account ON transactions(account_id);
CREATE INDEX idx_transactions_date ON transactions(txn_date);
```

Verify:
```sql
EXPLAIN QUERY PLAN SELECT * FROM transactions WHERE account_id = 1;
```

---

## 🧱 MATERIALIZED SUMMARY TABLE

For the executive dashboard, pre‑compute monthly summaries:

```sql
CREATE TABLE monthly_summary (
    month TEXT,
    branch_id INTEGER,
    total_txns INTEGER,
    total_amount REAL,
    PRIMARY KEY (month, branch_id)
);

-- Refresh procedure
DELETE FROM monthly_summary;
INSERT INTO monthly_summary
SELECT strftime('%Y-%m', t.txn_date), a.branch_id, COUNT(*), SUM(ABS(t.amount))
FROM transactions t
JOIN accounts a ON t.account_id = a.account_id
GROUP BY month, a.branch_id;
```

---

## 🧱 BACKUP & EXPORT

**Backup:**
```bash
sqlite3 imperial_analytics.db ".backup analytics_backup.db"
```

**Export:**
```bash
sqlite3 imperial_analytics.db
sqlite> .headers on
sqlite> .mode csv
sqlite> .output monthly_report.csv
sqlite> SELECT * FROM v_monthly_volume;
```

---

## 💡 Real‑world Usage

This architecture powers:
- Banking analytics and regulatory reporting
- E‑commerce sales dashboards
- Logistics performance monitoring
- HR workforce analytics

---

## 🔍 Practice Preview
You will build the Imperial Analytics database.

| Level | Task |
|-------|------|
| Easy | Create all tables with constraints and seed data. |
| Medium | Create the `v_branch_summary` view and add the strategic indexes. |
| Hard | Create the `monthly_summary` materialized table, write its refresh query, and set up automated backup in Python. |

Run the coach:
```bash
python ii_Practice_Sheets/L70_Module_7_Capstone_Optimized_Analytics_Database.py
```

---

## 📌 Key Takeaway
- Analytics databases combine normalization, views, indexes, and materialized tables.
- Security and performance are designed in from the start, not bolted on later.
- Automated backup and CSV export make the system production‑ready.
- This capstone is a portfolio‑worthy project for any backend role.

*For Emperor.*