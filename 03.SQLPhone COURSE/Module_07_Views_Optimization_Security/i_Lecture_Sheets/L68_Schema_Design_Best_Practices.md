# 📘 SQLPhone Emperor v3.0 · Module 7
# 📖 L68 – Schema Design Best Practices

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll design databases that are fast, maintainable, and resilient — the mark of a senior backend engineer. This lesson distills decades of database design wisdom into actionable rules.

- 🧱 **Normalization (3NF)** – eliminate data duplication
- 🧠 **Naming conventions** – consistency across every table
- 🧪 **Choosing data types** – right‑size your columns
- ⚡ **Documentation** – comments and schema diagrams
- 🧰 **Performance patterns** – when to denormalize

---

## 🧱 NORMALIZATION (THIRD NORMAL FORM)

Normalization removes redundancy. The three normal forms are:

**1NF:** Each column contains atomic values; no repeating groups.
```sql
-- BAD: multiple products in one row
CREATE TABLE orders (id, product1, product2, product3);

-- GOOD: separate order_items table
CREATE TABLE order_items (order_id, product_id, quantity);
```

**2NF:** Every non‑key column depends on the whole primary key (relevant for composite keys).

**3NF:** No transitive dependencies – a non‑key column should not depend on another non‑key column.
```sql
-- BAD: department_name depends on dept_id, which depends on emp_id
CREATE TABLE employees (emp_id, dept_id, department_name);

-- GOOD: separate departments table, reference by foreign key
CREATE TABLE employees (emp_id, dept_id);
CREATE TABLE departments (dept_id, department_name);
```

---

## 🧱 NAMING CONVENTIONS

Consistent naming makes your schema self‑documenting:

| Object | Convention | Example |
|--------|------------|---------|
| Tables | Singular, `snake_case` | `soldier`, `order_item` |
| Primary keys | `table_name_id` or `id` | `soldier_id`, `id` |
| Foreign keys | Match referenced column exactly | `regiment_id` → `regiments.id` |
| Indexes | `idx_table_column` | `idx_soldiers_name` |
| Views | Descriptive, often with `v_` prefix | `v_active_soldiers` |

---

## 🧱 CHOOSING DATA TYPES

| Data | SQLite Type | Notes |
|------|-------------|-------|
| IDs, counts, years | `INTEGER` | Uses 1‑8 bytes dynamically |
| Prices, percentages | `REAL` | 8‑byte IEEE float |
| Names, emails, codes | `TEXT` | UTF‑8 encoded |
| Images, files | `BLOB` | Stored exactly as input |
| True/false flags | `INTEGER` with `CHECK(0,1)` | SQLite has no native BOOLEAN |

---

## 🧱 WHEN TO DENORMALIZE

Sometimes you break normalization for performance:

- **Materialized summaries** – pre‑compute aggregations for dashboards
- **Counters** – store `order_count` on a `customer` row to avoid counting on every page load
- **JSON columns** – store semi‑structured data that doesn’t need its own table

> ⚠️ **WARNING:** Denormalize only when you have measured a performance problem. Premature denormalization creates update anomalies.

---

## 🧱 DOCUMENT EVERY TABLE

Every `CREATE TABLE` should be preceded by a comment block:

```sql
/*
 * Table: soldiers
 * Purpose: Stores active and reserve personnel.
 * Related to: regiments (regiment_id), deployments
 * Notes: salary must be positive (CHECK constraint).
 *   rank is nullable for new recruits.
 */
CREATE TABLE soldiers ( ... );
```

> 💡 **INSIGHT:** A well‑designed schema is self‑documenting. Future you – and your teammates – will thank you for clear names, proper normalization, and explanatory comments.

---

## 💡 Real‑world Usage

**Banking – normalized customer → account → transaction chain**
**E‑commerce – product → category → supplier with proper foreign keys**
**Logistics – shipment → route → carrier with consistent naming**
**HR – employee → department → location with documented schema**

---

## 🔍 Practice Preview
You will review and improve schema designs.

| Level | Task |
|-------|------|
| Easy | Identify a table with repeating groups and normalize it. |
| Medium | Rename columns to follow `snake_case` conventions and add comments. |
| Hard | Design a normalized schema for a new business requirement from scratch with full documentation. |

Run the coach:
```bash
python ii_Practice_Sheets/L68_Schema_Design_Best_Practices.py
```

---

## 📌 Key Takeaway
- Normalize to eliminate duplication; denormalize only when measured.
- Consistent naming conventions make schemas self‑documenting.
- Choose the right data type for each column.
- Document every table with purpose, relationships, and constraints.

*For Emperor.*