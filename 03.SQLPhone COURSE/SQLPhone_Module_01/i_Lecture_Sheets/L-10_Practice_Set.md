# 📘 SQLPhone Emperor · Module 01  
# 📖 L‑10 – Module Challenge: Imperial Fitness DB (Full Database Design)

---

## 🎯 OBJECTIVE  
Architect, build, and query a complete relational database for **Imperial Fitness**, a gym chain serving the Emperor’s soldiers.  
You’ll integrate every Module‑01 skill — `CREATE TABLE` with constraints, `INSERT`, `SELECT` with joins, and professional formatting — into one deliverable.

---

## 🧱 BRICK 1 – The Business Requirement & Table Blueprint

Imperial Fitness tracks members, trainers, classes, and enrollments.

**Tables and their columns:**

| Table      | Columns                                                                 | Constraints                         |
|------------|-------------------------------------------------------------------------|-------------------------------------|
| Member     | member_id INTEGER PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, join_date TEXT DEFAULT (datetime('now')), membership_tier TEXT CHECK(membership_tier IN ('Basic','Elite','Supreme')) | PK, UNIQUE, NOT NULL, CHECK, DEFAULT |
| Trainer    | trainer_id INTEGER PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL, specialty TEXT, hourly_rate REAL CHECK(hourly_rate > 0) | PK, NOT NULL, CHECK                 |
| Class      | class_id INTEGER PRIMARY KEY, class_name TEXT NOT NULL, trainer_id INTEGER, schedule_time TEXT, max_capacity INTEGER CHECK(max_capacity > 0), FOREIGN KEY (trainer_id) REFERENCES Trainer(trainer_id) ON DELETE SET NULL | PK, NOT NULL, CHECK, FK             |
| Enrollment | enrollment_id INTEGER PRIMARY KEY, member_id INTEGER NOT NULL, class_id INTEGER NOT NULL, enrollment_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (member_id) REFERENCES Member(member_id) ON DELETE CASCADE, FOREIGN KEY (class_id) REFERENCES Class(class_id) ON DELETE CASCADE, UNIQUE(member_id, class_id) | PK, FKs, UNIQUE composite          |

**Relationships:**
- **Member 1 ── * Enrollment * ── 1 Class** (many‑to‑many through Enrollment)
- **Class * ── 1 Trainer** (each class has one trainer; a trainer can run many classes)

Enrollment prevents double‑booking with `UNIQUE(member_id, class_id)`.

> 💡 **INSIGHT:** This schema mirrors real‑world gym software. It enforces business rules at the database level — the application layer stays thin and reliable.

---

## 🧱 BRICK 2 – Building and Seeding the Database

**① Create all four tables (Easy practice)**
Write the `CREATE TABLE` statements in dependency order: Member and Trainer first (no foreign keys), then Class (references Trainer), then Enrollment (references both). Example for Member:

```sql
CREATE TABLE Member (
    member_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    join_date TEXT DEFAULT (datetime('now')),
    membership_tier TEXT CHECK(membership_tier IN ('Basic','Elite','Supreme'))
);
```

Repeat for Trainer, Class, Enrollment using the blueprint above.

**② Insert sample data (Medium practice)**
Seed at least 3 rows per table. Use realistic names and varied tiers.

```sql
INSERT INTO Member (first_name, last_name, email, membership_tier)
VALUES
    ('Emperor','SQLPhone','emperor@sqlphone.dev','Supreme'),
    ('Rahim','Khan','rahim@example.com','Elite'),
    ('Karim','Ali','karim@example.com','Basic');
```

Insert trainers, classes (linking `trainer_id` to existing trainers), and enrollments.

**③ Write a join query to verify relationships**
```sql
SELECT m.first_name, c.class_name
FROM Enrollment e
JOIN Member m ON e.member_id = m.member_id
JOIN Class c ON e.class_id = c.class_id
LIMIT 1;
```
This confirms members and classes connect.

**④ Business report query (Hard practice)**
The challenge requires a **Class Enrollment Report** with full names concatenated and clear aliases.

```sql
SELECT
    m.first_name || ' ' || m.last_name AS "Member Name",
    c.class_name AS "Class Name",
    t.first_name || ' ' || t.last_name AS "Trainer Name",
    e.enrollment_date AS "Enrollment Date",
    c.schedule_time AS "Schedule"
FROM Enrollment e
JOIN Member m ON e.member_id = m.member_id
JOIN Class c ON e.class_id = c.class_id
JOIN Trainer t ON c.trainer_id = t.trainer_id;
```

- `||` concatenates strings (first + space + last).  
- Aliases with spaces are wrapped in double quotes.  
- All four tables are joined to produce a single, human‑readable report.

> ⚠️ **WARNING:** Always create tables in dependency order. If you try to create Enrollment before Member, the foreign key reference will fail. Follow the sequence: Member, Trainer, Class, Enrollment.

> 💡 **ADVANCED TIP – Composite UNIQUE for Enrollment:**  
> `UNIQUE(member_id, class_id)` prevents the same member enrolling twice in the same class. This is a **composite key** — a real‑world pattern you’ll use constantly.

---

## 💡 Real‑world Usage

**Banking – account and transaction tables with foreign keys**
```sql
CREATE TABLE accounts (account_id INTEGER PRIMARY KEY, ...);
CREATE TABLE transactions (tx_id INTEGER PRIMARY KEY, account_id INTEGER REFERENCES accounts(account_id) ON DELETE CASCADE, ...);
```

**E‑commerce – orders and line items**
```sql
CREATE TABLE orders (order_id INTEGER PRIMARY KEY, customer_id INTEGER REFERENCES customers(customer_id), ...);
CREATE TABLE order_items (order_id INTEGER, product_id INTEGER, PRIMARY KEY(order_id, product_id), ...);
```

**HR – employees and departments**
```sql
CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, dept_id INTEGER REFERENCES departments(dept_id), ...);
```

---

## 🔍 Practice Preview
You will execute the entire Imperial Fitness project.

| Level  | Task | What You’ll Write |
|--------|------|-------------------|
| Easy   | Create all four tables (Member, Trainer, Class, Enrollment) with correct columns and primary keys. | Four `CREATE TABLE` statements with constraints |
| Medium | Insert at least 3 rows into each table. Then write a query showing each enrollment with the member’s first name and class name. | Multi‑row `INSERT` and a `JOIN` query |
| Hard   | Write the full business query: show Member Name, Class Name, Trainer Name, Enrollment Date, Schedule. | `SELECT` with `||` concatenation, four‑table `JOIN`, and column aliases |

Run the coach:
```bash
python ii_Practice_Sheets/L-10_Imperial_Fitness.py
```
Work through Easy to Hard. The engine verifies your schema, data, and query.

---

## 📌 Key Takeaway
- A database schema is a contract: constraints enforce business rules.
- Foreign keys create relationships; composite keys prevent duplicates.
- A single `SELECT` joining four tables answers real business questions.
- You’ve just completed a sprint‑1 backend task. The same pattern builds banking, e‑commerce, and Companion’s memory.