# 📘 SQLPhone Emperor v3.0 · Module 10
# 📖 L96 – Cloud Databases – AWS RDS, Supabase, PlanetScale

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, you’ll deploy your database to the cloud — making it accessible from anywhere in the world, backed up automatically, and ready for real users.

- 🧱 **Cloud database concepts** – managed vs self‑hosted  
- 🧠 **AWS RDS** – enterprise‑grade PostgreSQL/MySQL  
- 🧪 **Supabase** – open‑source Firebase alternative with PostgreSQL  
- ⚡ **PlanetScale** – serverless MySQL with database branching  
- 🔌 **Connection strings** – how your backend reaches the cloud  

---

## 🧱 WHY CLOUD DATABASES?

A local database works for development, but production needs:
- 24/7 uptime  
- Automatic backups  
- Scalability  
- Access from any server  
- Monitoring and alerts  

Cloud providers handle all of this, letting you focus on building your application.

---

## 🧱 AWS RDS – THE ENTERPRISE STANDARD

Amazon RDS (Relational Database Service) supports PostgreSQL, MySQL, MariaDB, Oracle, and SQL Server. You get:

- Multi‑AZ deployment for high availability  
- Automated backups with point‑in‑time recovery  
- Encryption at rest and in transit  
- Read replicas for scaling reads  

**Connection string:**
```
postgresql://user:password@my-instance.xyz.us-east-1.rds.amazonaws.com:5432/empire
```

---

## 🧱 SUPABASE – THE MODERN BACKEND

Supabase is built on PostgreSQL and adds:
- Auto‑generated REST and GraphQL APIs  
- Real‑time subscriptions  
- Row‑level security policies  
- A generous free tier for side projects  

**Connection string:**
```
postgresql://postgres:password@db.xyz.supabase.co:5432/postgres
```

**Querying from Python:**
```python
import psycopg2
conn = psycopg2.connect("postgresql://postgres:password@db.xyz.supabase.co:5432/postgres")
```

---

## 🧱 PLANETSCALE – DATABASE BRANCHING

PlanetScale offers a serverless MySQL platform with a Git‑like branching workflow. You can:

- Create a branch of your database for development  
- Open a deploy request to merge schema changes  
- Scale automatically without managing servers  

**Connection string:**
```
mysql://user:password@aws.connect.psdb.cloud/empire?ssl={"rejectUnauthorized":true}
```

---

## 🧱 COMPARISON TABLE

| Feature | AWS RDS | Supabase | PlanetScale |
|---------|---------|----------|-------------|
| Database | PostgreSQL, MySQL | PostgreSQL | MySQL |
| Free tier | Limited (12 months) | Generous | Generous |
| API generation | No | Yes (REST/GraphQL) | No |
| Branching | No | No | Yes |
| Best for | Enterprise, full control | Side projects, mobile apps | Serverless, modern workflows |

---

## 💡 Real‑world Usage

**Banking – AWS RDS with Multi‑AZ for high availability**  
**E‑commerce – Supabase for a quick backend API**  
**Logistics – PlanetScale for serverless scaling during peak seasons**  
**Companion – start on Supabase (free), migrate to AWS RDS when you have 10,000+ users**

---

## 🔍 Practice Preview
You will explore cloud database offerings.

| Level | Task |
|-------|------|
| Easy | Sign up for a free Supabase account and locate your connection string. |
| Medium | Connect to your Supabase database from Python using psycopg2. |
| Hard | Design a deployment plan for Companion: which cloud database you’d choose at launch and which you’d migrate to at scale, with reasons. |

Run the coach:
```bash
python ii_Practice_Sheets/L96_Cloud_Databases_AWS_RDS_Supabase_PlanetScale.py
```

---

## 📌 Key Takeaway
- Cloud databases provide managed, scalable, backed‑up SQL.  
- AWS RDS is enterprise; Supabase is modern and developer‑friendly; PlanetScale is serverless and innovative.  
- Your choice depends on your project’s stage, budget, and scaling needs.  
- The connection string is your universal key to any cloud database.

*For Emperor.*