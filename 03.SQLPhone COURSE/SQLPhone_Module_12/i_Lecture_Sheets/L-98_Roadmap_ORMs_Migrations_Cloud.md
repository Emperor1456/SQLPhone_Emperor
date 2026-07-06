# 📘 SQLPhone Emperor · SQL Module 12
# 📖 L‑98 – Roadmap – ORMs, Migrations, Cloud

## 🎯 OBJECTIVE
Chart your next steps after mastering raw SQL: ORMs,
database migrations, cloud databases, and beyond.

## 🧱 BRICK 1 – Object‑Relational Mappers (ORMs)
ORMs like **SQLAlchemy** (Python) let you work with
databases using Python objects instead of writing SQL.

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine('sqlite:///app.db')
Base.metadata.create_all(engine)
session = Session(engine)
session.add(User(name='Emperor'))
session.commit()
```

ORMs automate many repetitive tasks, but you must
understand the underlying SQL to debug and optimise.

## 🧱 BRICK 2 – Migrations and Cloud Databases
**Migrations** (Alembic, Flyway) version‑control your schema
so you can safely change tables over time.

**Cloud Databases:**
- **Supabase** – PostgreSQL‑based, free tier.
- **PlanetScale** – MySQL‑compatible, serverless.
- **AWS RDS** / **Google Cloud SQL** – managed instances.

Deploying to the cloud means your database is accessible
from anywhere, backed up automatically, and scales with
your users.

## 💡 Your Full‑Stack Journey
1. SQL (you are here)
2. Backend framework (Flask, FastAPI, Django)
3. ORM + migrations
4. Frontend (HTML/CSS/JS + React/Vue)
5. Cloud deployment (Vercel, Railway, AWS)

## 📌 Key Takeaway
Raw SQL is the foundation; everything else builds on it.
You now have the skills to work with any database,
any language, any platform.

*The empire you built on a phone is ready for the world.*