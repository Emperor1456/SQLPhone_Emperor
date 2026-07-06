# 📘 SQLPhone Emperor · SQL Module 11
# 📖 L‑88 – E‑commerce Inventory Tracker

## 🎯 OBJECTIVE
Model product inventory, categories, suppliers,
and sales for an e‑commerce store.

## 🧱 BRICK 1 – Requirements
Entities:
- **Category:** id, name
- **Supplier:** id, name, contact
- **Product:** id, name, category_id (FK), supplier_id (FK),
  unit_price, stock_quantity
- **Sale:** id, product_id, quantity_sold, sale_date

Relationships:
- One category has many products.
- One supplier supplies many products.
- Each sale references a product.

## 🧱 BRICK 2 – Deliverables
1. DDL with foreign keys and constraints (CHECK stock >= 0).
2. Seed data (at least 4 categories, 3 suppliers,
   8 products, multiple sales).
3. Queries:
   - List low‑stock products (stock < 10).
   - Show total units sold per product.
   - Find best‑selling product.
   - Calculate revenue per category.

## 💡 Real‑world Usage
Every online store, from Amazon to your local shop,
uses a variant of this schema.

## 📌 Key Takeaway
Inventory management is a core business database.
Design for accurate stock tracking and sales analysis.

*Stock, sell, repeat – the cycle of commerce.*