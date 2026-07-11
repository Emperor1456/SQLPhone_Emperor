# 📘 SQLPhone Emperor v3.0 · Module 1
# 📖 L10 – Module 1 Capstone: Imperial Registry Database

---

## 🎯 OBJECTIVE — What You Will Master

> After this capstone, you’ll have built a complete, normalized database from scratch, proving every Module‑1 skill in one project.

- 🏗️ **Multi‑table schema design** – citizens, households, registrations
- 🔒 **Full constraint usage** – `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`, `CHECK`, `DEFAULT`
- ➕ **Seeding** – multi‑row `INSERT` with realistic data
- 🔍 **Business queries** – joins, filters, sorting, aggregation preview
- 📄 **Professional formatting & documentation**

---

## 🧱 THE IMPERIAL REGISTRY – BUSINESS REQUIREMENT

The Emperor’s census bureau needs a registry database that tracks every
citizen, their household, and their registration events.

**Tables to create:**

| Table | Purpose |
|-------|---------|
| `households` | Address and head of household |
| `citizens` | Personal details, linked to a household |
| `registrations` | Tracks when a citizen was registered, by whom |

---

## 🧱 SCHEMA DESIGN

```sql
-- Households must exist before citizens can be assigned to them
CREATE TABLE households (
    household_id INTEGER PRIMARY KEY,
    address TEXT NOT NULL,
    head_of_household TEXT NOT NULL,
    registered_date TEXT DEFAULT (date('now'))
);

-- Each citizen belongs to exactly one household
CREATE TABLE citizens (
    citizen_id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    birth_date TEXT NOT NULL,
    gender TEXT CHECK(gender IN ('M','F','Other')),
    household_id INTEGER NOT NULL,
    FOREIGN KEY (household_id) REFERENCES households(household_id)
);

-- Registration events track who registered and when
CREATE TABLE registrations (
    registration_id INTEGER PRIMARY KEY,
    citizen_id INTEGER NOT NULL UNIQUE,
    registrar_name TEXT NOT NULL,
    registration_date TEXT DEFAULT (date('now')),
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id)
);
```

---

## 🧱 SEEDING THE DATABASE

Insert sample households, citizens, and their registrations.

```sql
-- Households
INSERT INTO households (household_id, address, head_of_household)
VALUES
    (1, '12 Imperial Way, Dhaka', 'Emperor'),
    (2, '45 Warrior Lane, Chittagong', 'Rahim');

-- Citizens
INSERT INTO citizens (citizen_id, full_name, birth_date, gender, household_id)
VALUES
    (101, 'Emperor', '2008-07-10', 'M', 1),
    (102, 'Rahim', '1995-03-22', 'M', 2),
    (103, 'Karim', '2000-11-05', 'M', 2);

-- Registrations
INSERT INTO registrations (citizen_id, registrar_name, registration_date)
VALUES
    (101, 'Officer Ali', '2026-01-15'),
    (102, 'Officer Begum', '2026-02-10'),
    (103, 'Officer Begum', '2026-02-10');
```

---

## 🧱 BUSINESS QUERIES

**① List all citizens with their household address**
```sql
SELECT c.full_name, h.address
FROM citizens c
JOIN households h ON c.household_id = h.household_id
ORDER BY c.full_name;
```

**② Count citizens per household**
```sql
SELECT h.address, COUNT(c.citizen_id) AS members
FROM households h
LEFT JOIN citizens c ON h.household_id = c.household_id
GROUP BY h.household_id;
```

**③ Find all citizens registered by a specific officer**
```sql
SELECT c.full_name, r.registration_date
FROM registrations r
JOIN citizens c ON r.citizen_id = c.citizen_id
WHERE r.registrar_name = 'Officer Begum';
```

**④ Households with more than one member**
```sql
SELECT h.address, COUNT(c.citizen_id) AS member_count
FROM households h
JOIN citizens c ON h.household_id = c.household_id
GROUP BY h.household_id
HAVING COUNT(c.citizen_id) > 1;
```

---

## 💡 Real‑world Usage

**Banking – accounts, customers, transactions**
```sql
CREATE TABLE customers ( … );
CREATE TABLE accounts ( … REFERENCES customers … );
CREATE TABLE transactions ( … REFERENCES accounts … );
```

**E‑commerce – products, orders, line items**
```sql
CREATE TABLE products ( … );
CREATE TABLE orders ( … REFERENCES customers … );
CREATE TABLE order_items ( … REFERENCES orders, products … );
```

**Logistics – warehouses, shipments, tracking events**
```sql
CREATE TABLE warehouses ( … );
CREATE TABLE shipments ( … REFERENCES warehouses … );
CREATE TABLE tracking_events ( … REFERENCES shipments … );
```

---

## 🔍 Practice Preview
You will create the entire Imperial Registry database — tables, constraints, seed data, and queries.

| Level | Task |
|-------|------|
| Easy | Create `households`, `citizens`, and `registrations` tables with all constraints. |
| Medium | Insert all seed data and run a join query showing citizens with their household address. |
| Hard | Write a query that counts citizens per household and filters to show only households with more than one member. |

Run the coach:
```bash
python ii_Practice_Sheets/L10_Module_1_Capstone_Imperial_Registry_Database.py
```

---

## 📌 Key Takeaway
- A multi‑table schema with foreign keys models real‑world relationships.
- Constraints protect data integrity across tables.
- Joining tables reveals the full picture stored across your database.
- This capstone mirrors the first sprint of a real backend project.

*For Emperor.*