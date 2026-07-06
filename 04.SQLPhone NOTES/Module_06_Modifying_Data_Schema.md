# 04.SQLPhone NOTES/Module_06_Modifying_Data_Schema.md
# SQLPhone Emperor — The Best Phone‑First SQL Curriculum

# 📝 Module 06 – Modifying Data & Schema

## Data Modification
- `UPDATE table SET col=val WHERE condition;`
- `DELETE FROM table WHERE condition;`
- Always use `WHERE` to target specific rows.
- `DROP TABLE IF EXISTS` removes table entirely.

## Schema Changes
- `ALTER TABLE t ADD COLUMN col TYPE;`
- `ALTER TABLE t DROP COLUMN col;` (SQLite 3.35+)
- `ALTER TABLE t RENAME TO new_name;`
- `ALTER TABLE t RENAME COLUMN old TO new;`
- Cannot change column type directly; recreate table.

## Constraints & Indexes
- Primary key, composite key, foreign key.
- `CREATE INDEX idx_name ON t(col);` speeds queries.
- `AUTOINCREMENT` vs `INTEGER PRIMARY KEY` – autoincrement guarantees monotonic increase.

## Examples
```sql
UPDATE inventory SET quantity = quantity - 1 WHERE product_id = 42;

DELETE FROM logs WHERE created_at < '2024-01-01';

CREATE INDEX idx_email ON users(email);
```
