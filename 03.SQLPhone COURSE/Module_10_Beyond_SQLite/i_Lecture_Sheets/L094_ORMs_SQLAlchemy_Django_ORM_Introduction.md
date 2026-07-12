# 📘 SQLPhone Emperor v3.0 · Module 10
# 📖 L94 – ORMs – SQLAlchemy & Django ORM Introduction

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, you’ll understand how Object‑Relational Mapping transforms database rows into Python objects — and why this is the standard approach in modern web frameworks.

- 🧱 **What an ORM is** – tables become classes, rows become instances  
- 🧠 **SQLAlchemy** – the most powerful standalone ORM in Python  
- 🧪 **Django ORM** – the built‑in, rapid‑development ORM  
- ⚡ **Trade‑offs** – when raw SQL wins, when ORMs shine  
- 🧰 **Real‑world patterns** – defining models, querying, relationships  

---

## 🧱 THE ORM CONCEPT

Without an ORM, you write raw SQL and manually map results to Python objects:

```python
cursor.execute("SELECT * FROM soldiers WHERE rank = 'General'")
generals = [{"id": r[0], "name": r[1]} for r in cursor.fetchall()]
```

With an ORM, the same operation reads like natural Python:

```python
generals = session.query(Soldier).filter(Soldier.rank == 'General').all()
```

The ORM generates the SQL, executes it, and returns Python objects — complete with attributes and methods.

---

## 🧱 SQLALCHEMY – THE FLEXIBLE POWERHOUSE

SQLAlchemy offers two modes: **Core** (closer to SQL) and **ORM** (full object mapping). Here’s the ORM approach:

```python
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class Soldier(Base):
    __tablename__ = 'soldiers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rank = Column(String)
    salary = Column(Float)

engine = create_engine('sqlite:///empire.db')
Base.metadata.create_all(engine)

session = Session(engine)
session.add(Soldier(name="Emperor", rank="General", salary=5000))
session.commit()
```

Querying is Pythonic and composable:

```python
high_paid = session.query(Soldier).filter(Soldier.salary > 4000).all()
for s in high_paid:
    print(s.name, s.rank)
```

---

## 🧱 DJANGO ORM – RAPID DEVELOPMENT

Django’s ORM is built into the Django web framework. It uses a model‑class definition and automatically generates migrations.

```python
from django.db import models

class Soldier(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

# Querying
generals = Soldier.objects.filter(rank='General')
```

Django’s ORM handles relationships elegantly:

```python
class Regiment(models.Model):
    name = models.CharField(max_length=100)

class Soldier(models.Model):
    name = models.CharField(max_length=100)
    regiment = models.ForeignKey(Regiment, on_delete=models.CASCADE)

# Accessing related data
soldier = Soldier.objects.get(id=1)
print(soldier.regiment.name)
```

---

## 🧱 ORM VS RAW SQL – WHEN TO USE WHAT

| Criteria | Raw SQL | ORM |
|----------|---------|-----|
| Simple CRUD | Verbose | Concise |
| Complex joins & subqueries | Full control | Often still possible |
| Performance tuning | Direct | May need raw snippets |
| Learning curve | Requires SQL knowledge | Requires ORM knowledge |
| Portability across databases | More effort | Handled by ORM |

> 💡 **INSIGHT:** Master raw SQL first, then embrace ORMs. You’ll write better ORM code because you understand the SQL it generates.

---

## 💡 Real‑world Usage

**Banking – ORM with transactional safety**
```python
with session.begin():
    acc1 = session.query(Account).get(1)
    acc2 = session.query(Account).get(2)
    acc1.balance -= 500
    acc2.balance += 500
```

**E‑commerce – Django ORM for product catalog**
```python
products = Product.objects.filter(category='Electronics', price__lt=100)
```

**Logistics – SQLAlchemy for complex route queries**
```python
routes = session.query(Route).filter(Route.distance > 500).all()
```

**Companion – defining memory entries as SQLAlchemy models**
```python
class Memory(Base):
    __tablename__ = 'memories'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
```

---

## 🔍 Practice Preview
You will work with both ORMs and compare them to raw SQL.

| Level | Task |
|-------|------|
| Easy | Define a SQLAlchemy model for `soldiers` and insert one row. |
| Medium | Query all soldiers with salary above 3000 using SQLAlchemy ORM. |
| Hard | Define the same schema in Django models and write a query that joins soldiers to regiments. |

Run the coach:
```bash
python ii_Practice_Sheets/L94_ORMs_SQLAlchemy_Django_ORM_Introduction.py
```

---

## 📌 Key Takeaway
- ORMs map tables to classes and rows to objects.  
- SQLAlchemy provides flexibility; Django ORM provides speed.  
- Knowing both raw SQL and ORMs makes you a complete backend developer.  
- The ORM is a tool — your SQL knowledge ensures you use it wisely.

*For Emperor.*