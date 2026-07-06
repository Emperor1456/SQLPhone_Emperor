# 📘 SQLPhone Emperor · SQL Module 01
# 📖 L‑10 – Module Challenge: Imperial Fitness DB

## 🎯 OBJECTIVE
Architect, build, and validate a complete relational database
for a fictional gym chain. This challenge integrates all Module‑01
skills: DDL, DML, dot‑commands, and professional SQL style.

## 🧱 BRICK 1 – Business Requirements
**Imperial Fitness** needs a membership system to track:

- **Members** – name, email, join date, membership tier
- **Trainers** – name, specialty, hourly rate
- **Classes** – name, assigned trainer, schedule, max capacity
- **Enrollments** – which member takes which class and when

Your database must enforce:

- Primary keys for every table
- `NOT NULL` on mandatory fields
- `UNIQUE` on email
- Foreign keys with `ON DELETE CASCADE` where logical
- `CHECK` constraints on membership type and positive numbers
- Sensible defaults for date columns

## 🧱 BRICK 2 – Relationship Map
```
Member 1──* Enrollment *──1 Class *──1 Trainer
```
Enrollment is the join table.  
A composite unique key `(member_id, class_id)` prevents double‑booking.

## 📦 Deliverable: `imperial_fitness.sql`
One self‑contained script that does the following:

1. **Header comment** – author, date, purpose
2. **Drop existing tables** in correct dependency order
3. **Create all four tables** with full constraints
4. **Insert at least 3 rows per table** (real names, varied tiers)
5. **Write a business query** that joins all tables to produce a
   Class Enrollment Report:
   ```
   Member Name | Class Name | Trainer Name | Enrollment Date | Schedule
   ```
   Use `||` for full‑name concatenation and clear column aliases.
6. **Verification** – run `sqlite3 imperial_fitness.db < imperial_fitness.sql`,
   then check with `.tables`, `.schema`, and the report query.

## 🏆 Success Criteria
- Script runs without errors on a fresh SQLite instance.
- All constraints are enforced at the database level.
- Referential integrity holds – no orphan rows.
- The business query returns correct, readable results.
- Code is self‑documenting and professionally formatted.

## 💡 Professional Context
This challenge simulates the first sprint of a backend project
at any tech company: gather requirements → model data →
implement DDL → seed test data → validate with queries.

## 📌 Key Takeaway
Module‑01 gave you the tools.  
This challenge proves you can wield them.

*Design it. Build it. Query it. Own it.*