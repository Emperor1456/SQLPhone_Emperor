# 📘 SQLPhone Emperor · SQL Module 01
# 📖 L‑01 – What is SQL?

## 🎯 OBJECTIVE
Understand what SQL is, what a relational database is,
and why SQL is the backbone of all data‑driven systems.

## 🧱 BRICK 1 – SQL: The Language of Data
SQL stands for **Structured Query Language**.
It is the universal language used to talk to relational databases.
With SQL you can:
- `CREATE` – build tables and define their structure
- `INSERT` – add new data
- `SELECT` – read data
- `UPDATE` – modify existing data
- `DELETE` – remove data

SQL is **declarative**: you tell the database *what* you want,
and the engine figures out *how* to get it.
You don’t write loops or logic – you state your intent.

## 🧱 BRICK 2 – Relational Databases
A relational database organises data into **tables** (relations).
Each table is like a sheet in a spreadsheet:
- **Rows** = records (e.g. one customer)
- **Columns** = fields (e.g. name, email, signup_date)

Tables are linked by **keys**.
Example:
- `customers` table has `customer_id`
- `orders` table also has `customer_id`
→ This links an order to the customer who placed it,
without copying the customer’s details into every order.

**SQLite** is a self‑contained relational database engine.
The entire database lives in a single `.db` file.
No server, no configuration – perfect for phone‑first development.

## 💡 Real‑world Usage
Every app that stores data uses a database:
- Banking: accounts, transactions, audit logs
- E‑commerce: products, inventory, orders, payments
- Social media: users, posts, comments, likes
- Logistics: shipments, tracking, warehouses

Behind every screen, there’s a `SELECT` or an `INSERT`.
SQL is the thread that holds it all together.

## 📌 Key Takeaway
SQL is the universal data language.
Relational databases store information in linked tables.
Master SQL, and you control the data layer of any application.

*Every empire starts with a single query.*