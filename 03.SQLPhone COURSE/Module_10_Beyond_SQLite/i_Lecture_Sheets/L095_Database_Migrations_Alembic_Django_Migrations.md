# 📘 SQLPhone Emperor v3.0 · Module 10
# 📖 L95 – Database Migrations – Alembic & Django Migrations

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, you’ll evolve your database schema without losing data — the disciplined, professional way to manage change in any software project.

- 🧱 **What migrations are** – version‑controlled, incremental schema changes  
- 🧠 **Alembic** – the migration tool for SQLAlchemy  
- 🧪 **Django Migrations** – built‑in, auto‑generated, and powerful  
- ⚡ **Workflow** – generating, applying, and rolling back migrations  
- 🛡️ **Why migrations matter** – zero‑downtime deployments, team collaboration  

---

## 🧱 WHY MIGRATIONS?

Without migrations, changing a table requires manual SQL scripts that are error‑prone and untraceable. Migrations give you:

- A history of every schema change  
- The ability to upgrade or downgrade the database to any point  
- A safe, repeatable process that works across development, staging, and production  

---

## 🧱 ALEMBIC WORKFLOW (SQLALCHEMY)

Alembic watches your SQLAlchemy models and generates migration scripts automatically.

**Installation:**
```bash
pip install alembic
alembic init migrations
```

**Configure** `alembic.ini` to point to your database, then edit `migrations/env.py` to connect Alembic to your SQLAlchemy `Base`.

**Generate a migration:**
```bash
alembic revision --autogenerate -m "create soldiers table"
```

Alembic compares your models to the current database and creates a migration file with `upgrade()` and `downgrade()` functions.

**Apply the migration:**
```bash
alembic upgrade head
```

**Rollback one step:**
```bash
alembic downgrade -1
```

---

## 🧱 DJANGO MIGRATIONS WORKFLOW

Django automatically detects model changes and creates migration files.

**After modifying `models.py`:**
```bash
python manage.py makemigrations
```

This creates a migration file in the app’s `migrations/` folder. Review it, then apply:

```bash
python manage.py migrate
```

To see the current migration status:

```bash
python manage.py showmigrations
```

> 💡 **INSIGHT:** Django migrations are one of the framework’s killer features. They allow a team of developers to evolve the database in parallel without conflicts.

---

## 🧱 MIGRATION BEST PRACTICES

- Always commit migration files to version control.  
- Never edit a migration that has already been applied in production.  
- Test migrations on a copy of the production database before deploying.  
- Make migrations small and reversible where possible.

---

## 💡 Real‑world Usage

**Banking – adding a `tax_id` column to the customers table**
```bash
alembic revision -m "add tax_id to customers"
# Edit the migration to add the column
alembic upgrade head
```

**E‑commerce – creating a new `discounts` table**
```python
# Django models.py
class Discount(models.Model):
    code = models.CharField(max_length=20)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
```
```bash
python manage.py makemigrations && python manage.py migrate
```

**Logistics – rolling back a failed migration**
```bash
alembic downgrade -1
# Fix the migration file, then re‑apply
alembic upgrade head
```

**Companion – evolving the memory schema as features grow**

---

## 🔍 Practice Preview
You will create, apply, and roll back migrations with both tools.

| Level | Task |
|-------|------|
| Easy | Initialize Alembic and create a migration for a single table. |
| Medium | Apply the migration, insert data, then add a column and migrate again. |
| Hard | Create a Django project, define two related models, make and apply migrations. |

Run the coach:
```bash
python ii_Practice_Sheets/L95_Database_Migrations_Alembic_Django_Migrations.py
```

---

## 📌 Key Takeaway
- Migrations are version control for your database schema.  
- Alembic works with SQLAlchemy; Django has built‑in migrations.  
- Always test migrations before applying to production.  
- This is the professional standard for every backend team on earth.

*For Emperor.*