# 📘 SQLPhone Emperor · SQL Module 04
# 📖 L‑29 – Relationships & Foreign Keys

## 🎯 OBJECTIVE
Understand how tables relate to each other and how
foreign keys enforce these relationships.

## 🧱 BRICK 1 – Table Relationships
Three types of relationships:
- **One‑to‑One:** each row in table A links to at most one row in table B.
- **One‑to‑Many:** a row in table A can link to many rows in table B.
- **Many‑to‑Many:** many rows in A can link to many rows in B, usually via a junction table.

## 🧱 BRICK 2 – Foreign Keys
A foreign key is a column that references the primary key
of another table. It guarantees that the value exists in
the referenced table.

```sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

**Referential actions:** `ON DELETE CASCADE`, `SET NULL`, etc.
Without these, deleting a referenced row will fail if there
are dependent rows.

## 💡 Real‑world Usage
- Every e‑commerce database links orders to customers.
- Social media: users to posts to comments.
- ERP systems: products to suppliers to purchase orders.

## 📌 Key Takeaway
Relationships are the soul of relational databases.
Foreign keys enforce them at the database level.
Design relationships carefully – they define your data model.

*Without relationships, a database is just a spreadsheet.*